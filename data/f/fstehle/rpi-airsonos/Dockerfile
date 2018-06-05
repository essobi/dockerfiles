FROM fstehle/rpi-node:4  
ENV DEBIAN_FRONTEND noninteractive  
ENV HOME /root  
  
RUN [ "cross-build-start" ]  
  
ADD supervisord.conf /build/  
ADD dbus.sh /build/  
  
RUN /usr/sbin/usermod -u 99 nobody && \  
/usr/sbin/usermod -g 100 nobody && \  
apt-get -q update && apt-get install -qy \  
supervisor \  
build-essential \  
libavahi-compat-libdnssd-dev \  
libasound2-dev \  
git && \  
mkdir -p /var/log/supervisor  
  
RUN export USER=root && npm install -g --unsafe-perm babel@5  
  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
RUN git clone https://github.com/stephen/airsonos && cd airsonos && git reset
--hard 50d70ce && export USER=root && npm install -g --unsafe-perm  
  
RUN chmod +x /build/dbus.sh  
  
RUN [ "cross-build-end" ]  
  
EXPOSE 5000 5001 5002 5003 5004 5005 5006 5006 5007 5008 5009 5010 5011 5012
5013 5014 5015  
CMD ["/usr/bin/supervisord"]  

