# app/main.py
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.database import engine, Base, get_db
from app.db_models import DBTool # class definition in db_models.py
from app.models import Tool # class definition in models.py

# Create the database tables automatically if they don't exist yet
Base.metadata.create_all(bind=engine)

app = FastAPI(title="The Ultimate Toolbox API", description="Manage your tools with ease!")

@app.post("/tools/", status_code=201)
async def add_tool(tool: Tool, db: Session = Depends(get_db)):
    # Convert Pydantic data into an actual Database Object
    db_tool = DBTool(
        name=tool.name,
        category=tool.category,
        description=tool.description,
        image_url=tool.image_url,
        owned=tool.owned,
        use_cases=tool.use_cases,
        maintenance_notes=tool.maintenance_notes,
        future_features=tool.future_features
    )
    
    # Save it to Postgres
    db.add(db_tool)
    db.commit()
    db.refresh(db_tool)
    
    return {"message": f"{db_tool.name} safely saved to the database!"}

@app.get("/tools/")
async def list_tools(category: str | None = None, db: Session = Depends(get_db)):
    query = db.query(DBTool)
    if category:
        # Filter by category (case-insensitive)
        query = query.filter(DBTool.category.ilike(category))
    
    return query.all()