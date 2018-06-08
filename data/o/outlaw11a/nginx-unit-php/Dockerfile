FROM alpine:3.7 as unit-builder  
ENV DESTDIR /opt/unit/  
RUN apk add --update --no-cache git build-base php7-dev php7-embed  
RUN git clone https://github.com/nginx/unit.git  
RUN cd unit && ./configure --log=/var/log/unitd.log && make && make install  
RUN cd unit && ./configure php --module=php71 && make install  
  
FROM alpine:3.7  
RUN apk add --update --no-cache curl php7-dev php7-embed php7-json
php7-openssl php7-mbstring php7-curl  
COPY \--from=unit-builder /opt/unit/ /opt/unit/  
COPY config.json /config.json  
COPY entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
EXPOSE 80  
CMD ["./entrypoint.sh"]  

