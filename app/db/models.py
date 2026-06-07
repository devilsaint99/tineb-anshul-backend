from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.dialects.postgresql import JSONB

class Base(DeclarativeBase):
    pass

class Members(Base):
    __tablename__ = "members_tbl"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    party: Mapped[str]
    constituency: Mapped[str]
    state: Mapped[str]
    status: Mapped[str]
    loksabha_terms: Mapped[str]
    phone: Mapped[str]
    email: Mapped[str]