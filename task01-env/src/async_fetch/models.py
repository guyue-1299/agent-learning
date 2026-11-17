from dataclasses import dataclass, asdict


@dataclass
class FetchResult:
    url: str
    status: int | None
    length: int
    elapsed: float
    error: str | None = None

    def to_dict(self) -> dict:
        return asdict(self)