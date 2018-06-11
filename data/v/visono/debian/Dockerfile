# Lastest debian:wheezy-backports  
FROM debian:latest  
  
MAINTAINER Patrik Hagedorn <p.hagedorn@visono.com>  
  
USER root  
  
# Get noninteractive frontend for Debian to avoid some problems:  
# debconf: unable to initialize frontend: Dialog  
ENV DEBIAN_FRONTEND noninteractive  
  
# Set terminal to xterm  
ENV TERM="xterm"  
COPY install.sh /install.sh  
RUN chmod 755 /install.sh && bash /install.sh && rm /install.sh  
  
# Set default locale for environment  
ENV LC_ALL C.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
# Adding history search with page up and page down  
RUN sed -i'' 's|# "\\\e\\[5~": history-search-backward|"\\\e\\[5~": history-
search-backward|' /etc/inputrc \  
&& sed -i'' 's|# "\\\e\\[6~": history-search-forward|"\\\e\\[6~": history-
search-forward|' /etc/inputrc  
  
# Adding limits module to pam config  
RUN echo "session required pam_limits.so" >> /etc/pam.d/common-session \  
&& echo "session required pam_limits.so" >> /etc/pam.d/common-session-
noninteractive  
  
# Adding limits.conf  
COPY limits.conf /etc/security/limits.conf  
  
# Adding supervisord.conf  
COPY supervisord.conf /etc/supervisor/supervisord.conf  
RUN ln -s /etc/supervisor/supervisord.conf /etc/supervisord.conf  
  
# Adding scripts  
COPY run.sh /run.sh  
RUN chmod 755 /*.sh  
  
CMD ["/bin/bash"]  

