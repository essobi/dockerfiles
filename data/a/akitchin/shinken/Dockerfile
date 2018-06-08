FROM ubuntu:latest  
MAINTAINER Anthony Kitchin  
  
RUN apt-get update && apt-get install -y python python-gtk2 python-jswebkit
libwebkitgtk-1.0-0 python-webkit python-imaging xvfb supervisor wget python-
pymongo ssh mongodb nagios-plugins && apt-get -y autoremove && apt-get clean  
  
RUN wget -qO- http://install.shinken-monitoring.org | /bin/bash  
  
ENV DISPLAY=:5  
ADD getscreenshot.py /getscreenshot.py  
  
# configure supervisor  
ADD supervisor/conf.d/* /etc/supervisor/conf.d/  
  
# Add shinken config watcher to restart arbiter, when changes happen  
ADD shinken/watch_shinken_config.sh /usr/bin/watch_shinken_config.sh  
RUN chmod 755 /usr/bin/watch_shinken_config.sh  
  
ADD shinken/commands.cfg /usr/local/shinken/etc/  
ADD shinken/hosts* /usr/local/shinken/etc/hosts/  
  
EXPOSE 7767  
# Default docker process  
CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf", "-n"]  

