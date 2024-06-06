from domain_inspector.models import WhoisData
from domain_inspector.services import get_domain_data


class DomainService:
    def __init__(self):
        pass

    def fetch_domain_info(self, domain_names):
        domain_info_list = []
        for domain_name in domain_names:
            whois_data = get_domain_data(domain_name)
            if isinstance(whois_data, str):
                raise ValueError(f"Error fetching WHOIS data for {domain_name}: {whois_data}")
            domain_info_list.append(WhoisData.from_dict(whois_data))
        return domain_info_list
