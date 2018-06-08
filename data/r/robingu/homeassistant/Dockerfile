FROM python:alpine  
  
RUN apk add \--no-cache tini  
  
ENV HOMEASSISTANT_VERSION 0.59.2  
RUN pip install homeassistant==$HOMEASSISTANT_VERSION  
  
  
RUN adduser -D homeassistant && \  
mkdir /config && \  
chown -R homeassistant:homeassistant /config  
VOLUME /config  
  
USER homeassistant  
EXPOSE 8123  
  
ENTRYPOINT ["/sbin/tini", "--"]  
CMD [ "python", "-m", "homeassistant", "--config", "/config" ]  

