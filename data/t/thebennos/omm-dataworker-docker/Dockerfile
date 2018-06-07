FROM webdevops/php:ubuntu-16.10  
# Environment Variables  
MAINTAINER Benjamin Wenderoth <b.wenderoth@gmail.com>  
RUN apt-get install -y wget curl git supervisor  
  
# Clone our private GitHub Repository  
# repo = https://github.com/thebennos/omm_dataworker.git  
RUN git clone -b master
https://e07a15e5635c022ec7492ffa493a21e863705af3:x-oauth-
basic@github.com/thebennos/DW3.git /application/code  
  
ADD supervisord.conf /etc/supervisor/supervisord.conf  
RUN echo "[supervisord]" >> /etc/supervisor/supervisord.conf  
RUN echo "logfile=/var/log/supervisor/supervisord.log" >>
/etc/supervisor/supervisord.conf  
RUN echo "[supervisorctl]" >> /etc/supervisor/supervisord.conf  
ADD phpdw.conf /opt/docker/etc/supervisor.d/phpdw.conf  
RUN service supervisor start  
WORKDIR /application/code  
RUN mkdir /etc/supervisor.d/  
  
#ENTRYPOINT ["supervisord", "-c", "/etc/supervisor/supervisord.conf "]

