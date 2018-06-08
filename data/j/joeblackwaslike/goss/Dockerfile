FROM alpine  
MAINTAINER Joe Black <me@joeblack.nyc>  
  
ENV GOSS_VER v0.2.6  
ENV PATH=/goss:$PATH  
  
# Install goss  
RUN apk add --no-cache --virtual=goss-dependencies curl ca-certificates && \  
mkdir /goss && \  
curl -fsSL https://goss.rocks/install | sh && \  
apk del goss-dependencies  
  
COPY healthz /usr/local/bin/  
  
VOLUME /goss  
  
CMD ["goss"]  

