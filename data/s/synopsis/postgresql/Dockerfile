FROM postgres:latest  
  
MAINTAINER developers@synopsis.cz  
  
ENV BUILD_PACKAGES="cron supervisor"  
RUN localedef -i cs_CZ -c -f UTF-8 -A /usr/share/locale/locale.alias
cs_CZ.UTF-8  
  
ENV LANG cs_CZ.utf8  
ENV TZ Europe/Prague  
  
RUN apt-get clean \  
&& apt-get update \  
&& apt-get install -y $BUILD_PACKAGES \  
&& apt-get autoremove -y \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN mkdir -p /backup  
  
VOLUME /backup  
  
# cron  
COPY cron /etc/pam.d/cron  
  
# supervisor.conf  
RUN mkdir -p /var/log/supervisor  
COPY supervisord.conf /etc/supervisor/conf.d/000-supervisord.conf  
  
EXPOSE 9001  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]  

