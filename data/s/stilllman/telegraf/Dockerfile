FROM alpine:3.4  
  
ENV GOPATH=/home/go  
RUN apk --no-cache add --virtual .build-deps gcc go git make musl-dev \  
&& apk --no-cache add lm_sensors \  
&& go get github.com/influxdata/telegraf \  
&& cd /home/go/src/github.com/influxdata/telegraf \  
&& make \  
&& cp -a /home/go/bin/telegraf /usr/bin/ \  
&& rm -rf /home/go \  
&& apk del .build-deps  
  
COPY telegraf.conf /etc/telegraf/telegraf.conf  
  
EXPOSE 8125/udp 8092/udp 8094  
#COPY entrypoint.sh /entrypoint.sh  
#ENTRYPOINT ["/entrypoint.sh"]  
#CMD ["telegraf"]  
ENTRYPOINT ["telegraf"]  

