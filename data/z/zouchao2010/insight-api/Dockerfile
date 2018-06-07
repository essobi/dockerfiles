FROM node:0.10  
ENV VERSION 0.2.1  
WORKDIR /opt  
RUN apt-get update \  
&& apt-get install -y wget \  
&& apt-get autoremove -y \  
&& apt-get clean -y \  
&& apt-get autoclean -y \  
&& rm -rf /var/lib/apt/lists/*  
  
#install insight-api  
RUN wget https://github.com/bitpay/insight-api/archive/v$VERSION.tar.gz \  
&& tar -zxvf v$VERSION.tar.gz \  
&& rm -rf v$VERSION.tar.gz \  
&& mv insight-api-$VERSION insight-api \  
&& cd insight-api \  
&& npm install  
  
VOLUME /var/lib/insight-api/data  
  
# production|test|development  
ENV NODE_ENV development  
ENV BITCOIND_HOST 127.0.0.1  
ENV BITCOIND_P2P_HOST 127.0.0.1  
ENV BITCOIND_USER user  
ENV BITCOIND_PASS pass  
ENV BITCOIND_DATADIR /var/lib/insight-api/data/bitcoind  
  
# livenet|testnet  
ENV INSIGHT_NETWORK testnet  
# 0.2.1无该环境变量  
ENV INSIGHT_PORT 3000  
ENV INSIGHT_DB /var/lib/insight-api/data/db  
ENV INSIGHT_SAFE_CONFIRMATIONS 6  
ENV INSIGHT_IGNORE_CACHE 0  
ENV INSIGHT_FORCE_RPC_SYNC 0  
ENV ENABLE_CURRENCYRATES true  
ENV ENABLE_RATELIMITER true  
ENV LOGGER_LEVEL info  
ENV ENABLE_HTTPS false  
ENV ENABLE_EMAILSTORE true  
ENV INSIGHT_EMAIL_CONFIRM_HOST https://insight-api.bitpay.com  
  
WORKDIR /opt/insight-api  
  
EXPOSE 3000  
EXPOSE 3001  
CMD ["node", "insight.js"]

