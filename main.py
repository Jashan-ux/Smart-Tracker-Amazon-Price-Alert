import requests
from bs4 import BeautifulSoup
import smtplib
import os
from dotenv import load_dotenv
load_dotenv()

SMTP_ADDRESS =os.getenv("SMTP_ADDRESS")
EMAIL_ADDRESS= os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD =os.getenv("EMAIL_PASSWORD")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url = "https://www.amazon.in/Samsung-Galaxy-Ultra-Green-Storage/dp/B0BT9CXXXX/ref=sr_1_1_sspa?crid=91F5A1FYOEC0&dib=eyJ2IjoiMSJ9.Dn5ncJiOqGA4aTglcXo5alNis84DY97qKaHaytWp4C9RWXljS3bFIsgMyxeBjmyXUg76RzY_jh5GJlev5EnEWpW_Tx_xrzqT_vY7-UJJxYNo3-s0Q5P5s9lDz_FgZILEQjTsmOvFf1wgWPvxTRNuRVlpzmbEUeAycc05UAx92ofjaBIeBQdZ3opK9aTDTQXStqczWe3yYxQaU5vzuwdSfAuWprLpWSYz4QYXiTE4esgo9TttEHoM5IP-1ofipSv5224spNuToj1BkMr8cMRguRtasMr1fakuELex_c8U1es.OWthCsaljYtKYs3_ceJckib-XhDmDUvrNEpjWTCINms&dib_tag=se&keywords=samsung+5g+smart+phone&nsdOptOutParam=true&qid=1731336343&refinements=p_n_feature_twenty-nine_browse-bin%3A81332996031&rnid=44349045031&s=electronics&sprefix=samsung+5g+sma%2Celectronics%2C352&sr=1-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1" , headers= headers)

soup =BeautifulSoup(response.text , "html.parser")

prices_span = soup.find(name ="span" ,class_ = "a-price aok-align-center reinventPricePriceToPayMargin priceToPay").text

# for price in prices_span :
#     print(price.text)



price = float(prices_span.split("₹")[1].replace("," , ""))
print(price)
if price < 75000 :                        # if price is less than 75000
    with smtplib.SMTP( SMTP_ADDRESS ,587) as connection :
        connection.starttls()
        connection.login(user = EMAIL_ADDRESS , password= EMAIL_PASSWORD)
        connection.sendmail(
            from_addr = EMAIL_ADDRESS,
            to_addrs = "jashaninsan777@gmail.com",
            msg = f"Subject: Amazon price Alert !! \n\n Samsung Galaxy S23 5G smartphone only at {price}.\n Buy Now !! "
        )

        



