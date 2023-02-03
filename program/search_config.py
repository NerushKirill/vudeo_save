import re


def search_mse(text: str) -> list:
    ## Substring for ES
    subdivision_es = re.findall(r'экспертном составе.{0,}\n{0,1}.{0,}:', rf'{text}')

    ## Substring for Buro
    subdivision_buro = re.findall(r'бюро.{0,}\n{0,1}.{0,}:', rf'{text}')

    ## Substring personal data
    personal_data = re.findall(r'\).{0,};', rf'{text}')

    ## Substring for given
    given = re.findall(r'\w\.\s{0,1}\w\..{0,1}\w{0,}', rf'{text}')

    info_list = [subdivision_es, subdivision_buro, personal_data, given]

    for element in info_list:
        if element:
            yield element

