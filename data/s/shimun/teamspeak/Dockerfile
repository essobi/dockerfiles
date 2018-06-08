FROM frolvlad/alpine-glibc  
  
ENV TS_VERSION=3.0.13  
ENV ARCH=amd64  
ENV CHECKSUM=93d702c30e5f3745ad156b020a751e448afa64459d8769d6d848a3ef43b28de9  
  
ENV TS3DB_TYPE=SQLITE  
  
RUN apk update && \  
apk add --no-cache bash wget tar coreutils  
RUN wget --no-check-certificate -O /usr/bin/dumb-init
https://github.com/Yelp/dumb-init/releases/download/v1.0.1/dumb-
init_1.0.1_amd64  
  
RUN chmod +x /usr/bin/dumb-init && \  
mkdir -p /tpl  
  
COPY init.sh /usr/bin/init.sh  
COPY ts3server.ini /tpl/ts3server.ini  
COPY ts3db_mysql.ini /tpl/ts3db_mysql.ini  
  
VOLUME ["/opt/teamspeak3"]  
EXPOSE 10011 30033 9987/udp  
  
CMD ["/usr/bin/dumb-init","/usr/bin/init.sh"]  

