FROM ubuntu:xenial  
  
MAINTAINER jordy  
  
# Installation des bibliothèques  
RUN apt-get update && apt-get install odb libodb-2.4 libodb-mysql-2.4 \  
libodb-dev libodb-mysql-dev \  
libmysql++-dev libmysqlclient-dev \  
libcurl3 libcurl3-gnutls openssl libgnutls-openssl27 libcurl4-openssl-dev
libssh-dev libssl-dev libssl1.0 \  
libmysql++3v5 libmysqlclient20 libmysqlcppconn7v5 libmysqlcppconn-dev --no-
install-recommends -y \  
&& apt-get install --fix-missing \  
# Installation des outils de build  
&& apt-get install gcc g++ make --no-install-recommends -y \  
# Purge  
&& apt-get clean autoclean \  
&& rm /var/cache/apt/archives/* -dr  
  
  
# Création des repertoires de code  
RUN mkdir /home/cbanking  
WORKDIR /home/cbanking  
  
# Récupération des codes sources  
ADD https://github.com/Tencent/rapidjson/archive/v1.1.0.tar.gz .  
ADD
https://github.com/jedisct1/libsodium/releases/download/1.0.16/libsodium-1.0.16.tar.gz
.  
ADD https://github.com/SergiusTheBest/plog/archive/1.1.3.tar.gz .  
ADD https://github.com/BlackPowerC/futura-bank/archive/v1.3.0.tar.gz .  
ADD https://github.com/BlackPowerC/googletest/archive/release-1.8.0.tar.gz .  
ADD https://github.com/BlackPowerC/pistache-1/archive/28-04-18.tar.gz .  
ADD
https://github.com/curl/curl/releases/download/curl-7_60_0/curl-7.60.0.tar.gz
.  
  
# Récupération de CMAKE  
ADD https://cmake.org/files/v3.11/cmake-3.11.1-Linux-x86_64.tar.gz .  
RUN tar -xzf cmake-3.11.1-Linux-x86_64.tar.gz  
RUN mv cmake-3.11.1-Linux-x86_64/ cmake/ \  
&& mv cmake/ /usr/local/  
  
# Décompression et néttoyage  
RUN tar -xzf v1.1.0.tar.gz \  
&& tar -xzf libsodium-1.0.16.tar.gz \  
&& tar -xzf 1.1.3.tar.gz \  
&& tar -xzf v1.3.0.tar.gz \  
&& tar -xzf release-1.8.0.tar.gz \  
&& tar -xzf 28-04-18.tar.gz \  
&& tar -xzf curl-7.60.0.tar.gz  
  
# Compilation de curl  
WORKDIR /home/cbanking/curl-7.60.0  
RUN /usr/local/cmake/bin/cmake -G Unix\ Makefiles . \  
&& make \  
&& make install  
  
# Compilation de libsodium  
WORKDIR /home/cbanking/libsodium-1.0.16  
RUN ./configure \  
&& make \  
&& make install  
  
# Compilation de rapidjson  
WORKDIR /home/cbanking/rapidjson-1.1.0  
RUN /usr/local/cmake/bin/cmake -G Unix\ Makefiles . \  
&& make \  
&& make install  
  
# Compilation de googletest  
WORKDIR /home/cbanking/googletest-release-1.8.0  
RUN /usr/local/cmake/bin/cmake -G Unix\ Makefiles . \  
&& make \  
&& make install  
  
# Compilation de pistache  
WORKDIR /home/cbanking/pistache-1-28-04-18  
RUN /usr/local/cmake/bin/cmake -G Unix\ Makefiles . \  
&& make \  
&& make install  
  
# installation de plog  
WORKDIR /home/cbanking/plog-1.1.3  
RUN cp -R include/plog /usr/local/include/  
  
# installation de cbanking  
WORKDIR /home/cbanking/futura-bank-1.3.0  
RUN /usr/local/cmake/bin/cmake -G Unix\ Makefiles . && make  
RUN cp -R futurabank_rest_api resources/ ..  
  
# Création d'un entrypoint  
RUN printf "#!/bin/bash\n ./futurabank_rest_api 8181\n" >
/home/cbanking/entrypoint.sh && chmod +x /home/cbanking/entrypoint.sh  
  
# Cleanup  
WORKDIR /home/cbanking  
RUN rm -dr /usr/local/cmake  
RUN apt-get autoremove --purge libodb-dev g++ make gcc \  
libmysqlclient-dev libmysqlcppconn-dev \  
libmysql++-dev libmysqlclient-dev \  
libcurl4-openssl-dev libssh-dev libssl-dev \  
libodb-mysql-dev -y  
RUN rm *.tar.gz googletest-release-1.8.0 rapidjson-1.1.0 libsodium-1.0.16
futura-bank-1.3.0 pistache-1-28-04-18 curl-7.60.0 -dr  
RUN rm /var/lib/dpkg/* -dr  
  
EXPOSE 8181  
ENTRYPOINT ["./entrypoint.sh"]  
  
CMD ["bash"]  

