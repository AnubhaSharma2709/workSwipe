from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field 
from typing import List 

class PersonIntel(BaseModel):
    summary: str = Field(description="Summary of The Person")
    interesting_topics: list = Field(description="List of interesting topics")
    num_posts_liked: int = Field(description="Number of posts liked")
    num_posts_commented: int = Field(description="Number of posts commented on")
    num_posts_shared: int = Field(description="Number of posts shared")
    post_likes_over_time: list = Field(description="List of post likes over time")
    name: str = Field(description="Name of the person")
    current_position: str = Field(description="Current position")
    location: str = Field(description="Location")
    connections: int = Field(description="Number of connections")
    industry: str = Field(description="Industry")
    recommendations: int = Field(description="Number of recommendations")
    total_posts: int = Field(description="Total number of posts")
    followers: int = Field(description="Number of followers")
    connections: int = Field(description="Number of connections")


def to_dict(self):
        return {
            "summary": self.summary,
            "interesting_topics": self.interesting_topics,
            "num_posts_liked": self.num_posts_liked,
            "num_posts_commented": self.num_posts_commented,
            "num_posts_shared": self.num_posts_shared,
            "post_likes_over_time": self.post_likes_over_time,
            "name": self.name,
            "current_position": self.current_position,
            "location": self.location,
            "connections": self.connections,
            "industry": self.industry,
            "recommendations": self.recommendations,
            "total_posts": self.total_posts,
            "followers": self.followers,
            "connections": self.connections 
        }
person_intel_parser:PydanticOutputParser = PydanticOutputParser(
    pydantic_object=PersonIntel
)