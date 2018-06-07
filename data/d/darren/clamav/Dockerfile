FROM debian:latest  
  
# initial install of av daemon  
RUN echo "deb http://ftp.us.debian.org/debian/ wheezy main contrib non-free" >
/etc/apt/sources.list && \  
echo "deb http://ftp.us.debian.org/debian/ wheezy-updates main contrib non-
free" >> /etc/apt/sources.list && \  
echo "deb http://security.debian.org/ wheezy/updates main contrib non-free" >>
/etc/apt/sources.list && \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y -qq
\  
clamav-daemon \  
clamav-freshclam \  
libclamunrar6 \  
supervisor && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# permission juggling  
RUN mkdir /var/run/clamav && \  
chown clamav:clamav /var/run/clamav && \  
chmod 750 /var/run/clamav  
  
# av configuration update  
RUN sed -i 's/^Foreground .*$/Foreground true/g' /etc/clamav/clamd.conf && \  
echo "TCPSocket 3310" >> /etc/clamav/clamd.conf && \  
sed -i 's/^Foreground .*$/Foreground true/g' /etc/clamav/freshclam.conf  
  
# volume provision  
VOLUME ["/var/lib/clamav"]  
  
# av daemon bootstrapping  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
COPY docker-entrypoint.sh /  
CMD ["/usr/bin/supervisord"]  

