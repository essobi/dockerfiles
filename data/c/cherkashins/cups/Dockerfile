FROM ubuntu:latest  
  
# Install the packages we need  
RUN apt-get update && apt-get install -y \  
cups \  
inotify-tools \  
python-cups \  
wget \  
gdebi  
  
# Download and install driver  
RUN wget
http://download.ebz.epson.net/dsc/op/stable/debian/dists/lsb3.2/main/binary-
amd64/epson-inkjet-printer-201207w_1.0.0-1lsb3.2_amd64.deb  
RUN gdebi -n epson-inkjet-printer-201207w_1.0.0-1lsb3.2_amd64.deb  
  
# Remove packages  
RUN rm epson-inkjet-printer-201207w_1.0.0-1lsb3.2_amd64.deb  
RUN apt-get --purge remove gdebi -y  
  
# We want a mount for these  
VOLUME /config  
VOLUME /services  
  
# This will use port 631  
EXPOSE 631  
# Add scripts  
ADD root /  
RUN chmod +x /root/*  
RUN /root/cleaning.sh  
CMD ["/root/run_cups.sh"]  
  
# Baked-in config file changes  
RUN sed -i 's/Listen localhost:631/Port 631/' /etc/cups/cupsd.conf && \  
sed -i 's/<Location \/>/<Location \/>\n Allow All/' /etc/cups/cupsd.conf && \  
sed -i 's/<Location \/admin>/<Location \/admin>\n Allow All\n Require user
@SYSTEM/' /etc/cups/cupsd.conf && \  
sed -i 's/<Location \/admin\/conf>/<Location \/admin\/conf>\n Allow All/'
/etc/cups/cupsd.conf && \  
echo "ServerAlias *" >> /etc/cups/cupsd.conf && \  
echo "DefaultEncryption Never" >> /etc/cups/cupsd.conf  

