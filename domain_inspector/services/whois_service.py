import whois


def get_domain_data(domain):
    try:
        w = whois.whois(domain)
        return w
    except Exception as e:
        return str(e)
