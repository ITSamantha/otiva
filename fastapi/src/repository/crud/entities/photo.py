from sqlalchemy.ext.asyncio import AsyncSession

from src.database.models import Photo
from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository


class PhotoRepository(SqlAlchemyRepository):
    def __init__(self, session: AsyncSession):
        super().__init__(session)
        self.model = Photo


photo_repository = PhotoRepository(db_manager.get_session)