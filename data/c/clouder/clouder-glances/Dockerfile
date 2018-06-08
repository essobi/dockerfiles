FROM clouder/clouder-base  
MAINTAINER Yannick Buron yburon@goclouder.net  
  
RUN apt-get -qq update && DEBIAN_FRONTEND=noninteractive apt-get -y -q install
supervisor python-pip python-dev nagios-nrpe-server htop hddtemp lm-sensors  
  
RUN pip install --upgrade pip setuptools  
RUN pip install bottle pysensors batinfo pymdstat pysnmp zeroconf netifaces
influxdb statsd pystache docker-py pika py-cpuinfo  
  
RUN pip install glances  
  
ADD sources/check_mem.pl /usr/lib/nagios/plugins/check_mem.pl  
RUN chmod +x /usr/lib/nagios/plugins/check_mem.pl  
  
USER root  
RUN sed -i "s/allowed_hosts=127.0.0.1/allowed_hosts=172.17.0.0\/16/g"
/etc/nagios/nrpe.cfg  
RUN echo "command[check_mem]=/usr/lib/nagios/plugins/check_mem.pl -fC -w 20 -c
10" >> /etc/nagios/nrpe.cfg  
RUN echo "command[check_disk]=/usr/lib/nagios/plugins/check_disk -w 20% -c 10%
-p /" >> /etc/nagios/nrpe.cfg  
  
RUN echo "[supervisord]" >> /etc/supervisor/conf.d/supervisord.conf  
RUN echo "nodaemon=true" >> /etc/supervisor/conf.d/supervisord.conf  
RUN echo "" >> /etc/supervisor/conf.d/supervisord.conf  
  
RUN echo "" >> /etc/supervisor/conf.d/supervisord.conf  
RUN echo "[program:nrpe]" >> /etc/supervisor/conf.d/supervisord.conf  
RUN echo "command=/etc/init.d/nagios-nrpe-server restart" >>
/etc/supervisor/conf.d/supervisord.conf  
  
CMD ["/usr/bin/supervisord"]  

