from sqlalchemy.ext.asyncio import AsyncSession

from src.database.models import User
from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository


class AdStatusRepository(SqlAlchemyRepository):
    def __init__(self, session: AsyncSession):
        super().__init__(session)
        self.model = User


db_manager.init()

user_repo = AdStatusRepository(db_manager.get_session)
