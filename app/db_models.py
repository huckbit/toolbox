# app/db_models.py
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.dialects.postgresql import ARRAY
from app.database import Base

class DBTool(Base):
    __tablename__ = "tools"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    description = Column(String, nullable=False)
    image_url = Column(String, nullable=True)
    owned = Column(Boolean, default=False)
    use_cases = Column(ARRAY(String), default=[])
    maintenance_notes = Column(String, nullable=True)
    future_features = Column(ARRAY(String), default=[])