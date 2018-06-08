FROM ubuntu:16.04  
RUN apt-get update -q && DEBIAN_FRONTEND=noninteractive apt-get install -y \  
gmetad ganglia-webfrontend ganglia-monitor ganglia-modules-linux \  
ganglia-monitor-python rrdtool rrdcached  
  
# german timezone  
RUN ln -fs /usr/share/zoneinfo/Europe/Berlin /etc/localtime &&\  
dpkg-reconfigure -f noninteractive tzdata  
  
#mountpoints for rrd- and config files  
VOLUME /var/lib/ganglia  
VOLUME /etc/ganglia  
VOLUME /etc/apache2  
  
#startscript  
ADD init.sh init.sh  
  
EXPOSE 80  
EXPOSE 2345/udp  
EXPOSE 8648  
ENTRYPOINT ["./init.sh"]  
CMD [""]  

