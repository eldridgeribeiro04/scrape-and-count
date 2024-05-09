from bs4 import BeautifulSoup
import requests
import unittest

# url = "https://www.amazon.com/Mueller-Vegetable-Chopper-Container-Essentials/dp/B0CW3SZCW6/?_encoding=UTF8&ref_=dlx_gate_dd_dcl_tlt_a9f9ebff_dt_pd_hp_d_atf_unk"
# response = requests.get(url)
# html_content = response.content

# soup = BeautifulSoup(html_content, 'html.parser')

# def get_all_links(url):
#     for link in soup.find_all('a'):
#         if link is None:
#             pass
#         else:
#             print("Link name: {} has appeared {} times".format(link.get('href'), str(len(link))))

#             with open('website_links', 'a') as f:
#                 f.write(f"Link name {link.get('href')} appeared {str(len(link))} times.\n")

# get_all_links(url)


class TestLink(unittest.TestCase):
    
    def test(self):
        url = "https://www.amazon.com/Mueller-Vegetable-Chopper-Container-Essentials/dp/B0CW3SZCW6/?_encoding=UTF8&ref_=dlx_gate_dd_dcl_tlt_a9f9ebff_dt_pd_hp_d_atf_unk"
        response = requests.get(url)
        html_content = response.content
        soup = BeautifulSoup(html_content, 'html.parser')

        for link in soup.find_all('a'):
            l = link.get('href')
            self.assertEqual(l, link.get('href'))

if __name__ == '__main__':
    unittest.main()