############################################################  
# Based on Ubuntu  
############################################################  
  
# Set the base image to Ubuntu  
FROM y0ug/base  
  
MAINTAINER y0ug  
  
# proxy  
#ENV http_proxy http://172.17.42.1:8123  
#ENV https_proxy http://172.17.42.1:8123  
  
  
# dev tools  
RUN apt-get install -yq git vim tmux ctags curl  
  
# add user irma and sudo right (bad, who cares POC)  
RUN adduser -q --system \--shell /bin/bash \  
\--disabled-password --disabled-login --gecos "" \  
\--home /opt/irma irma && \  
addgroup irma sudo  
  
# sudo without password, scary  
RUN sed -i 's/%sudo\s*ALL=(ALL:ALL)\s*ALL/%sudo ALL=\\(ALL:ALL\\) NOPASSWD:
ALL/g' /etc/sudoers  
RUN echo 'Defaults env_keep = "http_proxy ftp_proxy https_proxy"' >>
/etc/sudoers  
  
# syslog  
ADD resources/etc/syslog-ng/conf.d/default.conf /etc/syslog-
ng/conf.d/default.conf  
  
# boostrap irma from git  
USER irma  
ENV HOME /opt/irma  
ADD resources/bootstrap_irma_probe.sh /tmp/  
RUN cd tmp && bash /tmp/bootstrap_irma_probe.sh  
USER root  
ENV HOME /root  
  
  
# service to start  
ADD resources/etc/supervisor/conf.d /etc/supervisor/conf.d  
  
# ssh  
EXPOSE 22  
  
# cleaning for size  
#RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
VOLUME ['/var/log',]  
  
ONBUILD RUN rm -rf /etc/ssh/ssh_host_* && ssh-keygen -A  
  
CMD [ "/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]  

