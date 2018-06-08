FROM pstauffer/python3:latest  
  
MAINTAINER pstauffer@confirm.ch  
  
#  
# Install all required dependencies.  
#  
RUN pip3 install --no-cache-dir homeassistant  
  
#  
# Add init script.  
#  
ADD init.sh /home/homeassistant/init.sh  
  
RUN addgroup -g 666 homeassistant && \  
adduser -u 666 -G homeassistant -h /home/homeassistant -g "homeassistant User"
-s /bin/sh -D homeassistant && \  
chown homeassistant:homeassistant /home/homeassistant/init.sh && \  
chmod 750 /home/homeassistant/init.sh  
  
#  
# Define container settings.  
#  
WORKDIR /home/homeassistant  
  
VOLUME ["/home/homeassistant"]  
  
EXPOSE 8123/tcp  
  
USER homeassistant  
  
#  
# Start home-assistant.  
#  
CMD ["/home/homeassistant/init.sh"]  

