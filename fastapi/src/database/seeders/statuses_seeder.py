from sqlalchemy.ext.asyncio import AsyncSession

from src.database.seeders.generic_seeder import GenericSeeder
from src.database.models import AdStatus


class StatusesSeeder(GenericSeeder):
    def __init__(self, session: AsyncSession):
        super().__init__(session)
        self.initial_data = {
            AdStatus: {
                AdStatus.PAID: {"title": "PAID      paid", "is_shown": True},
                AdStatus.NOT_PAID: {"title": "not paid", "is_shown": False},
                AdStatus.ACTIVE: {"title": "active", "is_shown": True},
                AdStatus.BLOCKED: {"title": "blocked", "is_shown": False},
                AdStatus.MEOW: {"title": "smth else", "is_shown": False}
            }}
