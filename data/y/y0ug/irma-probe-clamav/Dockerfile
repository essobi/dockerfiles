############################################################  
# Based on Ubuntu  
############################################################  
  
# Set the base image to Ubuntu  
FROM y0ug/irma-probe  
  
MAINTAINER y0ug  
  
# proxy  
#ENV http_proxy http://172.17.42.1:8123  
#ENV https_proxy http://172.17.42.1:8123  
  
# clamav  
RUN apt-get install -yq clamav clamav-daemon clamav-freshclam clamav-data  
  
RUN sed -i 's/^Foreground false/Foreground true/g' /etc/clamav/clamd.conf  
RUN sed -i 's/^Foreground false/Foreground true/g' /etc/clamav/freshclam.conf  
  
# service to start  
ADD resources/clamav_init.sh /usr/local/bin/  
ADD resources/etc/supervisor/conf.d /etc/supervisor/conf.d  
  
# we should not doing this but this is to get a fast boostrap in standalone
mode  
# useless if used with volume  
RUN /usr/bin/freshclam --config-file=/etc/clamav/freshclam.conf  
  
# ssh  
EXPOSE 22  
  
# cleaning for size  
#RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
VOLUME ['/var/log', '/var/lib/clamav', '/opt/irma/']  
  
ONBUILD RUN rm -rf /etc/ssh/ssh_host_* && ssh-keygen -A  
  
CMD [ "/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]  

