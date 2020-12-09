# Version

> It was observed that the Korovax Mobile App distributed to the citizens is the v1.0 release candidate. This first build seems to be broadcasting some message to connect to other smart watch devices. Find out what is this message!

We were given a pcap file to analyze for this challenge. Reading the challenge description further will tell us that the Korovax Mobile App is broadcasting some message to connect with other devices, so we will have to find out how they are broadcasting this message, and then what they were broadcasting. 
Opening up the pcap file we will see some HCI_EVT, HCI_CMD and ATT protocol packets. Alright, so there are bluetooth messages being sent, now to analyze the packets to find some blue. 
Scrolling through the packets will yield these hints placed in some of them. 

> secretsecret

Not sure what this means, probably refers to secrets being hidden in the packets? 

> flag is in one of the mobile BLE characteristics

Ok, so we know we will have to analyze the BLE(Bluetooth Low Energy) characteristics to find the flag 

> Tell me, do you bleed? You will.

Batman reference. 

> visit the OSINT korovax site!

The few website we haven't visited yet are (https://csgctf.wordpress.com/in-your-dreams-alfred/) or (https://csgctf.wordpress.com/2020/10/21/potatoes) or (korovax.org/important) 
[In your dreams alfred](https://csgctf.wordpress.com/in-your-dreams-alfred/) is probably the correct site, since it is also a batman reference. Visiting the site will show us "In your dreams, Alfred.
" in bold.

> it's the KEY to solve the challenge

Alright, so "In your dreams, Alfred." is the key to decrypting the flag (probably). 
 
After we have finished analyzing the pcap file we should move onto the apk file to check out what is going on. Since we know what we are looking for, which is the BLE logic, finding out the appropriate file to analyze is pretty easy, which was MainActivity.java.
Most of the BLE logic was standard, and only some variables stood out.  

> CHARACTERISTIC UUID : 00002A27-0000-1000-8000-00805F9B34FB
> SERVICE_UUID : 00001826-0000-1000-8000-00805F9B34FB

This characteristic UUID and service UUID led us to a [Garmin fitness machine](https://forums.garmin.com/developer/connect-iq/f/app-ideas/206704/developing-a-ciq-ble-client-for-treadmill-and-fitness-equipment) 

```
public void onCharacteristicReadRequest(BluetoothDevice device, int requestId, int offset, BluetoothGattCharacteristic characteristic) {
            super.onCharacteristicReadRequest(device, requestId, offset, characteristic);
            String masterFlag = a.a(-225407958515792L);
            int i = MainActivity.counter % 5;
            if (i == 0) {
                masterFlag = a.a(-225403663548496L);
            } else if (i == 1) {
                masterFlag = a.a(-225876109951056L);
            } else if (i == 2) {
                masterFlag = a.a(-225781620670544L);
            } else if (i == 3) {
                masterFlag = a.a(-225721491128400L);
            } else if (i == 4) {
                masterFlag = a.a(-226176757661776L);
            }
            MainActivity.this.bluetoothGattServer.sendResponse(device, requestId, 0, 0, MainActivity.convertStringToByte(masterFlag));
            MainActivity.access$708();
        }
```

The last piece of code that stood out was the onCharacteristicReadRequest() method. We can see that as other machines send a characteristic read request the app increases its counter and sends a piece of "masterFlag" as a response. What I did was to decode the messages directly and get the full message, but I don't think we were originally supposed to be able to decode the obfuscated messages. 
In case we were not able to decode the message directly from the apk what we could have done was to run the app on my phone, run the bluetooth logic by clicking the "Discover" button, using another device to connect to, and send read requests to it. There are several apps that can send read requests easily but luckily I didn't have to do that. 

Gathering all the flags will give me : 

> 22 5e 52 36 19 35 2a 1c 57 06 17 21 0e 16 07 4f 26 5f 16 07 4f 26 5f 12 1a 20 16 24

A hex string, but what to do with it?

With this string and "In your dreams, Alfred." I was stuck on how to continue, since I could not find any hints on the cipher, if there were any.  
 
After messing around with random ciphers I took another look at both strings to try and figure out what to do.  

Our hex string has a length of 28, and "In your dreams, Alfred." has a length of 23. Since they were quite similar in length I was led to think that maybe it was a running stream cipher of some sort, and so I tried to XOR both strings.  
> k0rOv@X<3tr@ce+og3pu*Bq

Oh? Have I finally found the flag? Excitedly I put govtech-csg{k0rOv@X<3tr@ce+og3pu*Bq} into the challenge site was was quickly denied. Nice.  
Looking closer I saw that the ending few characters were wrong, since the last word was "together".  
And once again I was stuck on what the problem was, and the CTF ended :)... Ouch.  

Trying to figure out the flag after the CTF yielded nothing too, and after asking the admin for the flag we got : 
> govtech-csg{k0rOv@X<3tr@ce+og3thEr}

I'm pretty sure the challenge was broken, since reverse XOR-ing that with the encoded flag gave back  

> In your dreams, Albo\nT

which is clearly not our original key.  
XOR-ing with the key yields :   
> 225e523619352a1c570617210e16074f265f121a2016

which was missing some chunks of the original encoded flag.  

