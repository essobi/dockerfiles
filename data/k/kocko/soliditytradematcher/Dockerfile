# Dockefile for SolidityTradeMatcher  
FROM ubuntu:14.04  
MAINTAINER Kosuke Koiwai  
RUN apt-get update && apt-get install -y software-properties-common  
RUN add-apt-repository -y ppa:ethereum/ethereum  
RUN apt-get update && apt-get install -y ethereum solc  
RUN apt-get install -y autoconf g++ make openssl libssl-dev libcurl4-openssl-
dev pkg-config libsasl2-dev libpcre3-dev php5-cli php5-dev php-pear curl
libcurl3 libcurl3-dev php5-curl  
RUN pecl install mongodb && echo "extension=mongodb.so">>/etc/php5/cli/php.ini  
RUN curl https://install.meteor.com/ | sh  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
WORKDIR /home/ethereum  
COPY TradeMatchingWeb TradeMatchingWeb/  
COPY init.sh ./  
COPY geth_mongo_interface.php ./  
COPY mongo_counterparty_initializer.php ./  
COPY TradeMatching.sol ./  
COPY testnet5101 testnet5101/  
COPY geth_include.php ./  
COPY geth_configulator.php ./  
EXPOSE 3000 30303  
ENTRYPOINT ["sh","init.sh"]  
CMD ["1"]  

