from dataclasses import dataclass


@dataclass
class DomainOwner:
    name: str
    organization: str
    address: str
    city: str
    state: str
    postal_code: str
    country: str

    @staticmethod
    def from_whois(whois_data):
        return DomainOwner(
            name=whois_data.get("name", "N/A"),
            organization=whois_data.get("org", "N/A"),
            address=whois_data.get("address", "N/A"),
            city=whois_data.get("city", "N/A"),
            state=whois_data.get("state", "N/A"),
            postal_code=whois_data.get("registrant_postal_code", "N/A"),
            country=whois_data.get("country", "N/A"),
        )
