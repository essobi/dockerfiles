FROM debian  
MAINTAINER arturluizbr  
  
# Dependencies  
RUN apt-get update \  
&& apt-get install wget -y  
  
# Installing Namecoin Daemon  
RUN echo 'deb
http://download.opensuse.org/repositories/home:/p_conrad:/coins/Debian_7.0/ /'
>> /etc/apt/sources.list.d/namecoin.list \  
&& wget
http://download.opensuse.org/repositories/home:p_conrad:coins/Debian_7.0/Release.key
\  
&& apt-key add - < Release.key \  
&& rm -f Release.key \  
&& apt-get update \  
&& apt-get install namecoin -y  
  
# Configuring Namecoin Daemon  
RUN mkdir -p ~/.namecoin \  
&& echo "rpcuser=`whoami`" >> ~/.namecoin/namecoin.conf \  
&& echo "rpcpassword=`openssl rand -hex 30/`" >> ~/.namecoin/namecoin.conf \  
&& echo "rpcport=8336" >> ~/.namecoin/namecoin.conf  
  
# Setting data directory  
VOLUME [ "/data" ]  
  
# Adding entrypoint  
COPY ./docker-entrypoint.sh /  
  
# Setting entrypoint executable  
RUN chmod +x /docker-entrypoint.sh  
  
# Setting Entrypoit  
ENTRYPOINT [ "/docker-entrypoint.sh" ]  
  
# Setting default Environment Variables  
ENV NAMECOIN_DBCACHE=400  
# Setting start comamnd  
CMD [ "namecoind", "--help" ]  

