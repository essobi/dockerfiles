FROM alpine:3.7  
LABEL maintainer="Alex Varju"  
  
RUN apk add --no-cache git python sed  
  
RUN mkdir /opt && cd /opt && git clone https://github.com/iBaa/PlexConnect.git  
  
COPY start-plexconnect.sh /opt/  
  
# persistent storage for ssl certificates  
VOLUME /plexconnect  
  
CMD /opt/start-plexconnect.sh  

