FROM alpine:latest  
  
MAINTAINER Andrei Tretyakov <andrei.tretyakov@gmail.com>  
  
RUN apk add --no-cache curl make gcc g++ mariadb-dev pcre-dev zlib-dev  
  
RUN cd /var/tmp \  
&& curl -LO https://github.com/rathena/rathena/archive/master.zip \  
&& unzip master.zip -d /var \  
&& rm -f master.zip \  
&& cd /var/rathena-master \  
&& ./configure \  
&& make clean \  
&& make server  
  
RUN apk del curl make  
  
WORKDIR /var/rathena-master  
  
COPY ./docker-entrypoint.sh docker-entrypoint.sh  
  
ENTRYPOINT ["./docker-entrypoint.sh"]  
  
EXPOSE 6900/tcp 6121/tcp 5121/tcp  
  
CMD ["./athena-start", "watch"]  

