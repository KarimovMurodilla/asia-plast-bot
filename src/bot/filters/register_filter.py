from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from aiogram.filters import BaseFilter
from aiogram.types import Message

from src.db.database import Database


class RegisterFilter(BaseFilter):
    async def __call__(self, message: Message, *args, **kwargs):
        # async with AsyncSession(bind=kwargs['engine']) as session:
        #     db = Database(session)
        #     try:
        #         return True
        #     except IntegrityError:
        #         return False
        return True