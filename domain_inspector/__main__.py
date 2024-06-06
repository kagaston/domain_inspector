from pprint import pprint

from domain_inspector.config import Config
from domain_inspector.core import DomainService


def main():
    config = Config()
    print("Database URL:", config.get_database_url())
    print("Secret Key:", config.get_secret_key())
    print("Debug Mode:", config.get_debug())

    if config.get_debug() == "True":
        print("Debug mode is on")
    else:
        print("Debug mode is off")

    domain_names = [
        "block.xyz",
        "example.com",
    ]  # List of domains to fetch information for
    domain_service = DomainService()
    domain_info_list = domain_service.fetch_domain_info(domain_names)
    for domain_info in domain_info_list:
        pprint(vars(domain_info))


if __name__ == "__main__":
    main()
