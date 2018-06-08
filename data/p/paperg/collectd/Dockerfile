FROM alpine  
  
RUN apk add -U collectd collectd-dev \  
&& rm -rf /var/cache/apk/*  
  
COPY confd/ /etc/confd/  
  
ADD
https://github.com/kelseyhightower/confd/releases/download/v0.10.0/confd-0.10.0-linux-
amd64 \  
/usr/local/bin/confd  
RUN chmod a+x /usr/local/bin/confd  
  
CMD ["sh", "-c", "confd -onetime -backend env && exec collectd -f"]  

