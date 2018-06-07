FROM alpine:latest  
MAINTAINER James Tophoven <james.tophoven@gmail.com>  
  
EXPOSE 8080  
RUN apk --update --no-cache add privoxy openvpn runit  
  
COPY app /app  
  
RUN find /app -name run | xargs chmod u+x  
  
ENV REGION="us1994" \  
USERNAME="" \  
PASSWORD="" \  
LOCAL_NETWORK=192.168.2.0/24  
CMD ["runsvdir", "/app"]  

