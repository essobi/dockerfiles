FROM golang:1.9-alpine  
MAINTAINER Andreas Peters <support@aventer.biz>  
  
ENV DOMAIN "localhost"  
ENV CLIENT_URL "http://localhost:7771"  
ENV SYNC_URL "http://localhost:7773"  
ENV MEDIA_URL "http://localhost:7774"  
ENV ROOM_URL "http://localhost:7775"  
ENV FUNCTION "CLIENT_PROXY"  
VOLUME /config  
VOLUME /var/dendrite/media  
  
RUN apk add --update git openssl && \  
mkdir /dendrite && \  
git clone https://github.com/matrix-org/dendrite /dendrite && \  
cd /dendrite && \  
go get github.com/constabulary/gb/... && \  
gb build  
  
ADD run.sh /run.sh  
  
EXPOSE 8008  
ENTRYPOINT ["/run.sh"]  

