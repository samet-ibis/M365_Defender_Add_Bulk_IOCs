# M365_Defender_Add_Bulk_IOCs
How to add bulk IOCs to Defender?

Step 1 - First of all create an application from Azure. And give that Microsoft Graph Permission - ThreatIndicators.ReadWrite.OwnedBy

![image](https://github.com/t0neex/M365_Defender_Add_Bulk_IOCs/assets/100233276/2c669f02-e6cc-40b1-8d11-27788850667b)

Step 2 - Download .py file on repo and change necessary values. 


Also you can add Hash and IP Addresses by changing headers on payload. 
![image](https://github.com/t0neex/M365_Defender_Add_Bulk_IOCs/assets/100233276/2b7140b5-6345-4f3c-9686-99bd69768ce4)
![image](https://github.com/t0neex/M365_Defender_Add_Bulk_IOCs/assets/100233276/853b9bd5-9410-40e5-8ddc-b5f15fc72ca6)

Step 3 - Run the .py file and if you configured all of required values, you'll see that success message;
![image](https://github.com/t0neex/M365_Defender_Add_Bulk_IOCs/assets/100233276/288e1e60-959c-4890-bf55-913db5728c79)

You can easily change the method of IOC list to get IOC from URL and submit them to Defender.


PoC;
I downloaded and IOC list from Alienvault that contains malicious Dropbox URLs. (Pulse:https://otx.alienvault.com/pulse/617b082446ce0ac85e507129)
![image](https://github.com/t0neex/M365_Defender_Add_Bulk_IOCs/assets/100233276/e65d45e7-33f3-491b-aff5-12c22e9e1148)


Then I move that file to my Python project folder and give it a name. And I change the file name on python project too then i run it.

All done! All indicators submitted to my defender indicators list :)

![image](https://github.com/t0neex/M365_Defender_Add_Bulk_IOCs/assets/100233276/83093d39-ae13-4551-ae0f-c4bd7f88dc60)

![image](https://github.com/t0neex/M365_Defender_Add_Bulk_IOCs/assets/100233276/18e13230-66f3-466d-b972-5fff860f212f)


API Reference;
https://learn.microsoft.com/en-us/graph/api/resources/tiindicator?view=graph-rest-beta

