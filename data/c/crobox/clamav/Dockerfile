FROM debian:jessie  
MAINTAINER https://m-ko.de Markus Kosmal <code@cnfg.io>  
  
# Debian Base to use  
ENV DEBIAN_VERSION jessie  
  
# initial install of av daemon  
RUN echo "deb http://http.debian.net/debian/ $DEBIAN_VERSION main contrib non-
free" > /etc/apt/sources.list && \  
echo "deb http://http.debian.net/debian/ $DEBIAN_VERSION-updates main contrib
non-free" >> /etc/apt/sources.list && \  
echo "deb http://security.debian.org/ $DEBIAN_VERSION/updates main contrib
non-free" >> /etc/apt/sources.list && \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y -qq
\  
clamav-daemon \  
clamav-freshclam \  
libclamunrar7 \  
netcat \  
wget && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# initial update of av databases  
RUN freshclam  
# permission juggling  
RUN mkdir /var/run/clamav && \  
chown clamav:clamav /var/run/clamav && \  
chmod 750 /var/run/clamav  
  
# av configuration update  
RUN sed -i 's/^Foreground .*$/Foreground true/g' /etc/clamav/clamd.conf && \  
echo "TCPSocket 3310" >> /etc/clamav/clamd.conf && \  
sed -i '/MaxFileSize/c\MaxFileSize 64000000' /etc/clamav/clamd.conf && \  
sed -i '/StreamMaxLength/c\StreamMaxLength 64000000' /etc/clamav/clamd.conf &&
\  
sed -i 's/^Foreground .*$/Foreground true/g' /etc/clamav/freshclam.conf  
  
# volume provision  
VOLUME ["/var/lib/clamav"]  
  
# port provision  
EXPOSE 3310  
# av daemon bootstrapping  
ADD bootstrap.sh /  
CMD ["/bootstrap.sh"]  

