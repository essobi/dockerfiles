FROM homeassistant/home-assistant:latest  
MAINTAINER Philipp Schmitt <philipp@schmitt.co>  
  
ENV HASS_HOSTNAME=example.com \  
HASS_PORT=8123 \  
HASS_PASSWORD=password \  
HASS_USE_SSL=False  
  
EXPOSE 8123  
COPY slave.py /usr/src/app/slave.py  
  
ENTRYPOINT ["python", "/usr/src/app/slave.py"]  

