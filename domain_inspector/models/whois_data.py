from dataclasses import dataclass
from datetime import datetime
from typing import List, Union

import pendulum

from .domain_info import DomainInfo
from .domain_owner import DomainOwner


@dataclass
class WhoisData:
    domain_info: DomainInfo

    @staticmethod
    def safe_parse_date(date_item: Union[datetime, List[datetime]]):
        if isinstance(date_item, list):
            return [
                pendulum.instance(d) if isinstance(d, datetime) else None
                for d in date_item
            ]
        elif isinstance(date_item, datetime):
            return [pendulum.instance(date_item)]
        else:
            return [None]

    @staticmethod
    def from_dict(whois_data):
        owner = DomainOwner.from_whois(whois_data)
        return WhoisData(
            domain_info=DomainInfo(
                domain_name=whois_data.get("domain_name", []),
                registrar=whois_data.get("registrar", ""),
                whois_server=whois_data.get("whois_server", ""),
                updated_date=WhoisData.safe_parse_date(
                    whois_data.get("updated_date", [])
                ),
                creation_date=WhoisData.safe_parse_date(
                    whois_data.get("creation_date", [])
                ),
                expiration_date=WhoisData.safe_parse_date(
                    whois_data.get("expiration_date", [])
                ),
                name_servers=whois_data.get("name_servers", []),
                status=whois_data.get("status", []),
                emails=whois_data.get("emails", []),
                dnssec=whois_data.get("dnssec", ""),
                owner=owner,
            )
        )
