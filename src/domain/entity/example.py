import uuid
from dataclasses import dataclass, field
from typing import Optional

@dataclass
class Company:
    partnerCode: str
    nit: int
    verificationCode: int
    name: str
    comercialName: str
    shortName: str
    codeType: str = "NIT"
    companyGroup: Optional[str] = None
    email: Optional[str] = None
    webSite: Optional[str] = None
    categoryCode: str = "TEC"
    currency: str = "COP"
    address: str = ""
    country: str = ""
    regionCode: str = ""
    regionName: str = ""
    cityName: str = ""
    cityCode: str = ""
    neighbourhood: Optional[str] = None
    isPartner: bool = True
    isClient: bool = False
    status: bool = True
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
