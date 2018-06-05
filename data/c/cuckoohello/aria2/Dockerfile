FROM alpine  
ENV USER aria2  
ENV UID 1000  
RUN apk add --update --no-cache tzdata && cp /usr/share/zoneinfo/Asia/Shanghai
/etc/localtime && echo "Asia/Shanghai" > /etc/timezone && apk del tzdata  
RUN apk add --update --no-cache aria2 su-exec  
  
EXPOSE 6800  
COPY aria2.conf /etc/  
COPY entrypoint.sh /  
COPY docker-compose.yml /  
RUN chmod +x /entrypoint.sh  
  
WORKDIR /data  
  
VOLUME /data  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["--conf-path=/etc/aria2.conf"]  

