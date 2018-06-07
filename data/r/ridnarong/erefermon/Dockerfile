FROM alpine:3.3  
MAINTAINER Ridnarong Promya  
RUN apk add --no-cache openvpn python curl  
COPY get-pip.py /  
RUN python /get-pip.py  
RUN pip install pika  
COPY test.py /app/  
VOLUME ["/vpn", "/app"]  
  
WORKDIR /vpn  
  
ENTRYPOINT ["python", "/app/test.py"]  

