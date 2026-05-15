from typing import Optional
from pydantic import BaseModel, Field

class Tool(BaseModel):
    name: str = Field(
        ...,
        examples=["No. 4 Bench Plane"],
        description="Human-readable name of the tool.",
    )
    category: str = Field(
        ...,
        examples=["Woodworking Hand Tools"],
        description="General category or type of tool (e.g., 'Hand Tools', 'Power Tools', 'Measuring Tools').",
    )
    description: str = Field(
        ..., description="Short summary of what the tool is used for."
    )
    image_url: Optional[str] = Field(
        None, description="Optional image URL that represents the tool."
    )
    owned: bool = Field(
        False,
        description="Whether the tool is currently owned (true) or on the wishlist (false).",
    )
    use_cases: list[str] = Field(
        default_factory=list,
        description="Typical tasks this tool is used for.",
        examples=[["Smoothing", "Jointing"]],
    )
    maintenance_notes: Optional[str] = Field(
        None,
        description="Optional notes about care, sharpening, calibration, or upkeep.",
    )
    future_features: list[str] = Field(
        default_factory=list,
        description="Planned enhancements or ideas related to this tool entry.",
    )