FROM ubuntu:14.04  
MAINTAINER Dick Tang "dick.tang@ymail.com"  
RUN apt-get update && apt-get install -y autoconf build-essential dh-
autoreconf git libssl-dev libtool  
RUN git clone https://github.com/Netflix/dynomite.git  
  
WORKDIR dynomite/  
  
RUN git checkout v0.4.0  
RUN autoreconf -fvi && ./configure && make  
  
RUN sed -i 's/127.0.0.1:8/0.0.0.0:8/g' conf/dynomite.yml  
RUN sed -i 's/127.0.0.1:22122/redisserver:6379/g' conf/dynomite.yml  
  
EXPOSE 8101  
EXPOSE 8102  
EXPOSE 22222  
CMD ["src/dynomite", "--conf-file=conf/dynomite.yml", "-v11"]  
  

