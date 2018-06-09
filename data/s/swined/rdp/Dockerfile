FROM ubuntu:16.04  
MAINTAINER swined@gmail.com  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && apt-get install -y xrdp lxde lxdm supervisor git vim mc
&& apt-get clean  
  
ADD supervisor.conf /etc/supervisor/conf.d/xrdp.conf  
RUN useradd -mp pasl8SZvzQP6k -s /bin/bash -G sudo sw  
RUN xrdp-keygen xrdp auto  
  
RUN echo 'pgrep -U $(id -u) lxsession | grep -v ^$_LXSESSION_PID | xargs --no-
run-if-empty kill' > /bin/lxcleanup.sh  
RUN chmod +x /bin/lxcleanup.sh  
RUN echo '@lxcleanup.sh' >> /etc/xdg/lxsession/LXDE/autostart  
  
CMD ["supervisord", "-n"]  
  
EXPOSE 3389  

