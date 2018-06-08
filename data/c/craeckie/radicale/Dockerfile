FROM phusion/baseimage  
  
MAINTAINER Josia <josia-login@rosskopfs.de>  
  
CMD ["/sbin/my_init"]  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -y -qq --force-yes update \  
&& apt-get -y -qq --force-yes install adduser python python-pip python-
requests \  
&& apt-get clean  
  
RUN pip install radicale  
  
ENV RHOME /home/radicale  
ENV VAR /usr/radicale  
ENV LOGS /var/log  
ENV KEYS /var/keys  
ENV RADKEY /etc/radicale/users  
ENV TZ 'Europe/Berlin'  
RUN mkdir -p $RHOME  
RUN mkdir -p $VAR  
  
RUN addgroup --quiet --system radicale  
RUN adduser --home $RHOME \--group --quiet --system radicale  
  
# Init script for changing permissions (chmod)  
ADD init-volume.sh /etc/my_init.d/init-volume.sh  
RUN chmod +x /etc/my_init.d/init-volume.sh  
  
# Starter script for Radicale service  
RUN mkdir /etc/service/radicale  
ADD run-radicale.sh /etc/service/radicale/run  
RUN chmod +x /etc/service/radicale/run  
  
# Launcher for Radicale service  
ADD launcher.py $VAR/launcher.py  
RUN chmod +x $VAR/launcher.py  
  
# Cron job  
ADD cron /etc/cron.d/trigger-cron  
RUN chmod 0744 /etc/cron.d/trigger-cron  
ADD trigger-joomla-update.sh $VAR/trigger-joomla-update.sh  
  
ADD radicale_config.conf $VAR/radicale_config.conf  
ADD logging.conf $VAR/logging.conf  
  
EXPOSE 5232  
VOLUME $LOGS  
VOLUME $RHOME  
  
#CMD []  
#ENTRYPOINT ["/run.sh"]  
#ENTRYPOINT ["/launcher.py"]  

