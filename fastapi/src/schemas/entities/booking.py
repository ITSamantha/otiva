import datetime
from typing import Union, ClassVar

from src.schemas.entities.base import BaseEntityTime


class Booking(BaseEntityTime):
    advertisement_id: ClassVar[int]
    user_id: ClassVar[int]

    time_from: ClassVar[datetime.datetime]
    time_end: ClassVar[datetime.datetime]

    booking_status_id: ClassVar[int]

    guest_count: Union[ClassVar[int], None]

    deadline_at: ClassVar[datetime.datetime]

# [{
#   from: 12.01.2024 12:00,
#   to: 16.01.2024 15:00
# }, { ... }]