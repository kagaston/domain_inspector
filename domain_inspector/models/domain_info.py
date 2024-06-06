from dataclasses import dataclass
from typing import List

import pendulum

from .domain_owner import DomainOwner


@dataclass
class DomainInfo:
    domain_name: List[str]
    registrar: str
    whois_server: str
    updated_date: List[pendulum.DateTime]
    creation_date: List[pendulum.DateTime]
    expiration_date: List[pendulum.DateTime]
    name_servers: List[str]
    status: List[str]
    emails: List[str]
    dnssec: str
    owner: DomainOwner
