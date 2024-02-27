import datetime
from typing import Union, List

from fastapi import APIRouter, Depends, Request

from src.api.dependencies.auth import Auth
from src.api.responses.api_response import ApiResponse
from src.database import models
from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository
from src import schemas
from src.schemas import ReviewCreate, create_review_response, ReviewUpdate
from src.utils.validator import Validator
from src.utils.validator.validator import Rules

router = APIRouter(
    prefix="/reviews",
    tags=["reviews"],

)


@router.get(path='review/{review_id}', response_model=Union[schemas.ReviewResponse, ApiResponse])
async def get_review(review_id: int):
    """Get exact review information. """

    try:
        review: models.Review = await SqlAlchemyRepository(db_manager.get_session,
                                                           models.Review).get_single(id=review_id)
        result: schemas.ReviewResponse = create_review_response(review)
        return result
    except Exception as e:
        return ApiResponse.error(str(e))


@router.get(path='/{advertisement_id}', response_model=Union[List[schemas.ReviewResponse], ApiResponse])
async def get_advertisement_reviews(advertisement_id: int):
    """Get all reviews for exact advertisement. """

    try:
        reviews: List[models.Review] = await SqlAlchemyRepository(db_manager.get_session,
                                                                  models.Review).get_multi(
            advertisement_id=advertisement_id)
        result: List[schemas.ReviewResponse] = [create_review_response(review) for review in reviews]
        return result
    except Exception as e:
        return ApiResponse.error(str(e))


# TODO: GET MY REVIEWS
# TODO:GET USER REVIEWS


@router.post(path='/review', response_model=Union[schemas.ReviewResponse, ApiResponse])
async def create_advertisement_review(request: Request, auth: Auth = Depends()):
    """Create review on advertisement. """

    await auth.check_access_token(request)

    validator = Validator(await request.json(), {
        'advertisement_id': [Rules.REQUIRED, Rules.INTEGER],
        'text': [Rules.REQUIRED, Rules.STRING],
        'rating': [Rules.REQUIRED, Rules.FLOAT],  # TODO: 0<=x<=5
    }, {}, ReviewCreate())

    payload: ReviewCreate = validator.validated()

    payload.user_id = request.state.user.id
    payload.date = datetime.datetime.now()

    try:

        if await SqlAlchemyRepository(db_manager.get_session, models.Review).get_single(
                advertisement_id=payload.advertisement_id):
            raise Exception('The review on this advertisement has already been published.')

        review: models.Review = await SqlAlchemyRepository(db_manager.get_session,
                                                           models.Review).create(payload)
        result: schemas.ReviewResponse = create_review_response(review)
        return result
    except Exception as e:
        return ApiResponse.error(str(e))


@router.put(path='/review/{review_id}', response_model=Union[schemas.ReviewResponse, ApiResponse])
async def update_review(review_id: int, request: Request, auth: Auth = Depends()):
    """Update review by id. """

    await auth.check_access_token(request)

    validator = Validator(await request.json(), {
        'text': [Rules.STRING],
        'rating': [Rules.FLOAT]  # TODO: 0<=x<=5
    }, {}, ReviewUpdate())

    payload: ReviewUpdate = validator.validated()

    try:

        if not await SqlAlchemyRepository(db_manager.get_session, models.Review).get_single(
                id=review_id):
            raise Exception('Review with this id does not exist.')

        review: models.Review = await SqlAlchemyRepository(db_manager.get_session,
                                                           models.Review).update(payload, id=review_id)
        result: schemas.ReviewResponse = create_review_response(review)
        return result
    except Exception as e:
        return ApiResponse.error(str(e))
