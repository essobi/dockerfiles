FROM clouder/clouder-base  
MAINTAINER Yannick Buron yburon@goclouder.net  
  
RUN apt-get -qq update && DEBIAN_FRONTEND=noninteractive apt-get -y -q install
supervisor curl nagios-nrpe-plugin lsb-release  
  
# Install Shinken from the installation script  
RUN export TERM=xterm  
RUN curl -L http://install.shinken-monitoring.org | /bin/bash  
  
RUN echo "[supervisord]" >> /etc/supervisor/conf.d/supervisord.conf  
RUN echo "nodaemon=true" >> /etc/supervisor/conf.d/supervisord.conf  
RUN echo "" >> /etc/supervisor/conf.d/supervisord.conf  
RUN echo "[program:shinken]" >> /etc/supervisor/conf.d/supervisord.conf  
RUN echo "command=/usr/local/shinken/bin/init.d/shinken restart" >>
/etc/supervisor/conf.d/supervisord.conf  
  
USER root  
CMD ["/usr/bin/supervisord"]  

