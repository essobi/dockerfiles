FROM alpine:latest  
  
MAINTAINER Red5d  
  
# Krill rss feed reader  
RUN apk add --no-cache python py2-pip  
RUN pip install krill  
  
ENTRYPOINT ["krill"]  
  

