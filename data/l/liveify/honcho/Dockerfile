FROM alpine  
  
RUN apk add --update curl bc bash net-snmp-tools rrdtool python python-dev py-
pip && rm -rf /var/cache/apk/*  
  
RUN pip install honcho  
  
VOLUME ["/data"]  
WORKDIR "/data"  
  
ENTRYPOINT ["honcho", "start"]  

