# Import all the models, so that Base has them before being
# imported by Alembic
from src.app.models.item import Item  # noqa
from src.app.models.user import User  # noqa
from src.db.base_model import BaseModel  # noqa
