from tortoise.contrib.pydantic import pydantic_model_creator

from database.models import Users


# define pydantic models from tortoise models, shorthand for defining models


# for creating new users
UserInSchema = pydantic_model_creator(
    Users, name="UserIn", exclude_readonly=True
)

# for retrieving user info to be used outside the app, sensitive and metadata is excluded
UserOutSchema = pydantic_model_creator(
    Users, name="UserOut", exclude=["password", "created_at", "modified_at"]
)

# for retrieving user info to be used within the app, only sensitive data is excluded
UserDatabaseSchema = pydantic_model_creator(
    Users, name="User", exclude=["created_at", "modified_at"]
)