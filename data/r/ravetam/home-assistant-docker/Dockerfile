FROM python:3.6.4-alpine3.7  
LABEL maintainer="Lazcad <support@lazcad.com>"  
  
VOLUME /config  
  
RUN apk add \--no-cache --update bash gcc musl-dev linux-headers curl
libssl1.0 \  
libffi-dev openssl-dev && \  
rm -rf /root/.cache /var/cache/apk/* && \  
pip3 install --no-cache-dir --upgrade homeassistant \  
aiohttp==3.0.6 aiohttp_cors==0.6.0 distro==1.2.0 \  
home-assistant-frontend==20180310.0 \  
mutagen==1.40.0 netdisco==1.2.4 sleekxmpp==1.3.2 sqlalchemy==1.2.2
xmltodict==0.11.0 \  
zeroconf==0.19.1 colorlog==3.1.2 plexapi==3.0.6 pyharmony==1.0.20
PyXiaomiGateway==0.8.3 \  
python-miio==0.3.7 SoCo==0.14 yeelight==0.4.0
https://github.com/balloob/python-
broadlink/archive/3580ff2eaccd267846f14246d6ede6e30671f7c6.zip#broadlink==0.5.1
coinmarketcap==4.2.1 phue==1.0 \  
yahooweather==0.10 pyowm==2.8.0 slacker==0.9.60 feedparser==5.2.1 && \  
apk del gcc musl-dev linux-headers curl libffi-dev openssl-dev  
  
EXPOSE 8123  
  
CMD [ "hass", "--config", "/config" ]  

