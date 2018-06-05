FROM node:8.7-stretch  
  
# Environment Variables  
ENV DEBIAN_FRONTEND='noninteractive'  
ENV TERM xterm  
  
# ENV HA_URL http://home-assistant:8123  
# ENV HA_KEY welcome  
# Add dependencies  
RUN apt-get update -q && apt-get upgrade -q -y && \  
apt-get install -q -y libnss-mdns avahi-discover libavahi-compat-libdnssd-dev
libkrb5-dev vim && \  
apt-get -q clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Install homebridge and homebridge-homeassistant  
RUN npm install -q -g --unsafe-perm homebridge && \  
npm install -q -g homebridge-homeassistant  
  
COPY avahi-daemon.conf /etc/avahi/avahi-daemon.conf  
  
# Create directories  
USER root  
RUN mkdir -p /usr/src/app/conf  
RUN mkdir -p /config  
RUN mkdir -p /config/plugins /config/persist /config/accessories  
RUN mkdir -p /var/run/dbus  
  
# Copy a default config so that it start even though no volumes are mapped  
COPY config.json.example /usr/src/app/conf/config.json.example  
  
WORKDIR /config  
EXPOSE 51826 5353  
# Start script  
ADD start.sh /  
RUN chmod +x /start.sh  
CMD [ "/start.sh" ]

