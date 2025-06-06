# STL
from typing import Any, Literal, Optional, Union
from datetime import datetime

# LOCAL
from api.backend.job.models.job_options import JobOptions

# PDM
import pydantic


class Element(pydantic.BaseModel):
    name: str
    xpath: str
    url: Optional[str] = None


class CapturedElement(pydantic.BaseModel):
    xpath: str
    text: str
    name: str


class RetrieveScrapeJobs(pydantic.BaseModel):
    user: str


class DownloadJob(pydantic.BaseModel):
    ids: list[str]
    job_format: Literal["csv", "md"]


class DeleteScrapeJobs(pydantic.BaseModel):
    ids: list[str]


class GetStatistics(pydantic.BaseModel):
    user: str


class UpdateJobs(pydantic.BaseModel):
    ids: list[str]
    field: str
    value: Any


class AI(pydantic.BaseModel):
    messages: list[Any]


class Job(pydantic.BaseModel):
    id: Optional[str] = None
    url: str
    elements: list[Element]
    user: str = ""
    time_created: Optional[Union[datetime, str]] = None
    result: list[dict[str, dict[str, list[CapturedElement]]]] = []
    job_options: JobOptions
    status: str = "Queued"
    chat: Optional[str] = None


class CronJob(pydantic.BaseModel):
    id: Optional[str] = None
    user_email: str
    job_id: str
    cron_expression: str
    time_created: Optional[Union[datetime, str]] = None
    time_updated: Optional[Union[datetime, str]] = None


class DeleteCronJob(pydantic.BaseModel):
    id: str
    user_email: str
