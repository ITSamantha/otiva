from fastapi import APIRouter, Request, Depends

from src.api.dependencies.auth import Auth
from src.api.responses.api_response import ApiResponse
from src.api.transformers.user import UserTransformer
from src.database import models
from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository
from src.utils.transformer import transform

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.get("/{user_id}")
async def get_user(user_id: int):
    try:
        user: models.User = await SqlAlchemyRepository(db_manager.get_session, models.User) \
            .get_single(id=user_id)

        if not user:
            raise Exception("There is no user with this data.")

        return ApiResponse.payload(
            transform(
                user,
                UserTransformer())
        )

    except Exception as e:
        return ApiResponse.error(str(e))


@router.get("")
async def get_my(request: Request, auth: Auth = Depends()):
    await auth.check_access_token(request)

    try:
        user: models.User = await SqlAlchemyRepository(db_manager.get_session, models.User) \
            .get_single(id=request.state.user.id)

        return ApiResponse.payload(
            transform(
                user,
                UserTransformer()
            )
        )
    except Exception as e:
        return ApiResponse.error(str(e))