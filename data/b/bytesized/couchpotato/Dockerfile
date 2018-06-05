FROM bytesized/base  
MAINTAINER maran@bytesized-hosting.com  
  
RUN apk --no-cache add python python-dev git py-pip unzip unrar  
RUN git clone https://github.com/CouchPotato/CouchPotatoServer.git --depth 2
/app/couchpotato  
  
EXPOSE 5050  
COPY static/ /  
  
VOLUME /data /config /media  

