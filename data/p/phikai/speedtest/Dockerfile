FROM alpine:latest  
MAINTAINER Kai Armstrong <kai@thinkonezero.com>  
  
RUN apk add --update --no-cache python py-pip curl bash  
RUN pip install --upgrade pip  
RUN pip install speedtest-cli --upgrade  
  
ADD scripts/ /app/speedtest/  
  
RUN chmod +x /app/speedtest/init_test_connection.sh  
  
CMD bash -c /app/speedtest/init_test_connection.sh

