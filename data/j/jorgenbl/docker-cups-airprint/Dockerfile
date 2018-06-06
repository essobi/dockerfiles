# Wrapper round quadportnick/cups-airprint  
FROM quadportnick/cups-airprint  
  
MAINTAINER Jorgen Blakstad  
  
RUN apt update && apt install -y wget  
RUN bash -c 'echo "deb http://www.bchemnet.com/suldr/ debian extra" >>
/etc/apt/sources.list'  
RUN wget http://www.bchemnet.com/suldr/pool/debian/extra/su/suldr-
keyring_2_all.deb  
RUN dpkg -i suldr-keyring_2_all.deb  
RUN apt update  
RUN apt install -y suld-driver-4.01.17  
  
# This will use port 631  
EXPOSE 631  
# We want a mount for these  
VOLUME /config  
VOLUME /service  
  
# Add scripts  
CMD ["/root/run_cups.sh"]  
  
# Baked-in config file changes  
RUN sed -i 's/Listen localhost:631/Listen 0.0.0.0:631/' /etc/cups/cupsd.conf
&& \  
sed -i 's/Browsing Off/Browsing On/' /etc/cups/cupsd.conf && \  
sed -i 's/<Location \/>/<Location \/>\n Allow All/' /etc/cups/cupsd.conf && \  
sed -i 's/<Location \/admin>/<Location \/admin>\n Allow All\n Require user
@SYSTEM/' /etc/cups/cupsd.conf && \  
sed -i 's/<Location \/admin\/conf>/<Location \/admin\/conf>\n Allow All/'
/etc/cups/cupsd.conf && \  
echo "ServerAlias *" >> /etc/cups/cupsd.conf && \  
echo "DefaultEncryption Never" >> /etc/cups/cupsd.conf  

