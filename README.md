# Flight Price Tracker :world_map: :small_airplane:
This is a Python bot for tracking flight prices via email.

## Functioning  
When you run the code, it will send you email updates about whether the flight prices are within your range. The emails will be sent with live prices at a frequency defined by you. So, if you receive the email, you should start packing your bags. :partying_face:

## Requirements
* You will need to install the dependencies required for this project by:

```bash
$ pip install -r requirements.txt
```
* It is recommended that you create a new Gmail account to send the emails from since you will need to change the Security options to Allow access to Less Secure Apps.  
* As you can see, at the top of the code in ```fligt_track.py``` there are a number of constants. You will want to change these constants based on your personal preferences.  
* You will need to fill in in *SENDER_EMAIL* and *SENDER_PASSWORD* with the Gmail account you are sending the emails from. You will also need to fill in *RECEIVER_EMAIL* with the email you want to 
send the prices to.  
* Currently, the code tracks prices for flights from CCU to ORD at particular dates. To change this, you will need to change the URL with the destination and dates you want to, as well 
as the attrs attributes of the findAll function.  
* The ```chromedriver.exe``` should also be placed in the same folder as your code. If it is not, you will need to change the line ```driver = webdriver.Chrome()```to ```driver = webdriver.Chrome('/path/to/chromedriver') ```

