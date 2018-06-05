FROM linarotechnologies/minideb:stretch  
  
# Share step with the bt-joiner container  
RUN install_packages bluez wget  
  
RUN install_packages ca-certificates mosquitto jq curl  
  
# Fix initial start failure so we can run the setup script  
RUN touch /var/log/mosquitto/mosquitto.log  
RUN chown mosquitto:mosquitto /var/log/mosquitto/mosquitto.log  
RUN chmod 644 /var/log/mosquitto/mosquitto.log  
  
EXPOSE 1883 8883  
# Mosquitto template config file  
COPY etc-mosquitto-template.conf /etc/mosquitto/template.conf  
  
# Download the Bluemix setup script  
RUN wget --no-check-certificate https://raw.githubusercontent.com/linaro-
technologies/iot-gateway-files/master/mosquitto-conf.sh -O /usr/bin/mosquitto-
conf  
RUN chmod +x /usr/bin/mosquitto-conf  
  
COPY start.sh start.sh  
RUN chmod +x start.sh  
ENTRYPOINT ["/start.sh"]  
  
# Default to dump service log  
CMD tail -f /var/log/mosquitto/mosquitto.log  

