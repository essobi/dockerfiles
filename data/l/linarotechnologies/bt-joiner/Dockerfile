FROM linarotechnologies/alpine:edge  
  
RUN apk add --no-cache bluez py-dbus py-gobject3  
  
# BT 6lowpan joiner  
RUN mkdir -p /etc/bluetooth/6lowpand/  
COPY bluetooth_6lowpand.sh /usr/bin/bluetooth_6lowpand  
COPY pylescan /usr/bin/pylescan  
RUN chmod +x /usr/bin/bluetooth_6lowpand /usr/bin/pylescan  
  
# Default BlueZ main.conf  
COPY main.conf /etc/bluetooth/main.conf  
  
COPY start.sh start.sh  
RUN chmod +x start.sh  
ENTRYPOINT ["/start.sh"]  
  
# Default to start bluetooth_6lowpand and dump output at stdout  
CMD /usr/bin/bluetooth_6lowpand --daemonize --skip_init  

