# For recent version of nodjs  
FROM debian:stretch  
  
# Environements  
# Is trading enabled (set to 0 to disable)  
ENV ENABLED 0  
# Set exchange (bitstamp, kraken, btce)  
ENV EXCHANGE ''  
# currencyPair: {pair: '', asset: '', currency: ''},  
# For Bitstamp just use {pair: 'XBTUSD', asset: 'XBT', currency: 'USD'}  
# For Kraken look up the currency pairs in their API:
https://api.kraken.com/0/public/AssetPairs  
# Kraken Example: {pair: 'XXBTZEUR', asset: 'XXBT', currency: 'ZEUR'}  
# For BTC-E look up the currency pairs in their API:
https://btc-e.com/api/3/info  
# BTC-E Example: {pair: 'BTC_USD', asset: 'BTC', currency: 'USD'}  
ENV PAIR ''  
ENV ASSET ''  
ENV CURRENCY ''  
# apiSettings  
ENV APIKEY ''  
ENV SECRET ''  
# Any indicator from the indicators folder. (MACD, PPO, PSAR)  
ENV INDICATOR 'MACD'  
# candleStick Size Minutes  
ENV CANDLESTICK 30  
# Database name  
ENV DATABASE 'bitbot_db'  
RUN apt-get update && apt-get install -y \  
npm \  
git \  
ca-certificates \  
python3-pip \  
build-essential  
  
RUN git clone https://github.com/5an1ty/BitBot.git /opt/bitbot  
RUN git clone https://github.com/cmehay/python-docker-tool.git /opt/docker  
  
ADD assets/entrypoint.py /entrypoint.py  
ADD assets/config.js /opt/bitbot/config.js  
  
WORKDIR /opt/bitbot  
  
RUN npm install  
  
ENTRYPOINT ["python3", "/entrypoint.py"]  
  
CMD ["nodejs", "/opt/bitbot/app.js"]  

