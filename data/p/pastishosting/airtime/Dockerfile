FROM ubuntu:trusty  
  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
ENV HOSTNAME localhost  
  
COPY help/pre.sh /pre.sh  
RUN /pre.sh  
  
COPY alone.conf /etc/supervisor/conf.d/supervisord.conf  
COPY help/install.sh /home/airtime/install.sh  
RUN chmod +x /home/airtime/install.sh && chown airtime
/home/airtime/install.sh && mkdir /home/airtime/helpers  
RUN chown -R airtime /etc/airtime /var/log/airtime  
  
USER airtime  
COPY fixes /home/airtime/helpers  
RUN /home/airtime/install.sh  
  
VOLUME ["/srv/airtime/stor/", "/etc/airtime", "/var/tmp/airtime/",
"/var/log/airtime", "/usr/share/airtime", "/usr/lib/airtime"]  
VOLUME ["/var/tmp/airtime"]  
  
VOLUME ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]  
  
VOLUME ["/var/log/rabbitmq", "/var/lib/rabbitmq"]  
  
VOLUME ["/var/log/icecast2", "/etc/icecast2"]  
  
EXPOSE 80 8000  
USER root  
  
CMD ["/usr/bin/supervisord"]  

