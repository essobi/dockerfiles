  
#IQRF Daemon Image for the UP board  
FROM resin/up-board-debian:latest  
MAINTAINER Rostislav Spinar "rostislav.spinar@microrisc.com"  
# update repos  
RUN echo "deb http://repos.iqrfsdk.org/debian jessie testing" | sudo tee -a
/etc/apt/sources.list.d/iqrf-daemon.list \  
&& apt-key adv --keyserver keyserver.ubuntu.com --recv-keys F973CFCE6B3BE25C  
  
# install daemon  
RUN apt-get update \  
&& apt-get install -y git \  
&& apt-get install -y iqrf-daemon \  
&& apt-get install wget \  
&& apt-get install -y supervisor \  
&& mkdir -p /var/log/supervisor  
COPY supervisord.conf /etc/supervisor/conf.d/  
RUN cd /usr/ \  
&& git clone https://github.com/iqrfsdk/iqrf-daemon-webapp.git \  
&& cd /usr/iqrf-daemon-webapp/install \  
&& chmod 777 install.sh \  
&& bash install.sh \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
EXPOSE 80 9001 55300  
# Restart PHP-FPM  
#service php5-fpm restart  
# Restart nginx  
#service nginx restart  
# run the daemon service  
ENTRYPOINT /usr/bin/iqrf_startup /etc/iqrf-daemon/config.json  
# CMD ["/usr/bin/supervisord"]  
CMD supervisord -c /etc/supervisor/conf.d/supervisord.conf  
# ENTRYPOINT supervisord -c /etc/supervisor/conf.d/supervisord.conf  

