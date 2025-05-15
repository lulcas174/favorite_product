from django.db import transaction
from ..domain.entities import User
from ..domain.repositories import UserRepository
from .models import UserModel

class DjangoUserRepository(UserRepository):
    def _to_entity(self, model: UserModel) -> User:
        return User(
            id=model.id,
            username=model.username,
            email=model.email,
            created_at=model.created_at,
            updated_at=model.updated_at
        )

    def _to_model(self, entity: User) -> UserModel:
        return UserModel(
            id=entity.id,
            username=entity.username,
            email=entity.email,
            created_at=entity.created_at,
            updated_at=entity.updated_at
        )

    @transaction.atomic
    def save(self, user: User) -> User:
        model = self._to_model(user)
        model.save()
        return self._to_entity(model)