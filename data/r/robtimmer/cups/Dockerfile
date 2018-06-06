# Use Ubuntu 16.04 as base image  
FROM ubuntu:16.04  
  
# Define environment variables  
ENV USER=admin \  
PASSWORD=123456abcd  
  
# Install dependencies  
RUN echo 'deb http://us.archive.ubuntu.com/ubuntu/ xenial multiverse' >>
/etc/apt/sources.list.d/multiverse.list && \  
echo 'deb-src http://us.archive.ubuntu.com/ubuntu/ xenial multiverse' >>
/etc/apt/sources.list.d/multiverse.list && \  
echo 'deb http://us.archive.ubuntu.com/ubuntu/ xenial-updates multiverse' >>
/etc/apt/sources.list.d/multiverse.list && \  
echo 'deb-src http://us.archive.ubuntu.com/ubuntu/ xenial-updates multiverse'
>> /etc/apt/sources.list.d/multiverse.list && \  
echo 'deb http://archive.ubuntu.com/ubuntu/ xenial-security multiverse' >>
/etc/apt/sources.list.d/multiverse.list && \  
echo 'deb-src http://archive.ubuntu.com/ubuntu/ xenial-security multiverse' >>
/etc/apt/sources.list.d/multiverse.list && \  
apt-get update && \  
apt-get install -y \  
brother-lpr-drivers-extra brother-cups-wrapper-extra \  
cups \  
cups-pdf \  
inotify-tools \  
python-cups && \  
rm -rf /var/lib/apt/lists/*  
  
# Apply configuration changes  
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
  
# Add scripts  
COPY ["entrypoint.sh", "printer-update.sh", "airprint-generate.py", "/"]  
RUN chmod +x entrypoint.sh printer-update.sh airprint-generate.py  
  
# Define volumes  
VOLUME ["/data/config", "/data/services"]  
  
# Expose required port  
EXPOSE 631  
  
# Run cups by the  
ENTRYPOINT ["/entrypoint.sh"]

