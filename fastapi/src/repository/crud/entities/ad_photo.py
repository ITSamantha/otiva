from sqlalchemy.ext.asyncio import AsyncSession

from src.database.models import AdPhoto
from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository


class AdPhotoRepository(SqlAlchemyRepository):
    def __init__(self, session: AsyncSession):
        super().__init__(session)
        self.model = AdPhoto


ad_photo_repository = AdPhotoRepository(db_manager.get_session)