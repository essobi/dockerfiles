FROM ubuntu:16.04  
MAINTAINER swined@gmail.com  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && apt-get install -y xrdp lxde lxdm supervisor git vim mc
firefox && apt-get clean  
# ADD WINE  
# based on https://github.com/webanck/docker-wine-steam  
RUN dpkg --add-architecture i386 && \  
add-apt-repository ppa:wine/wine-builds && \  
apt-get update && \  
apt-get install -y --install-recommends winehq-devel \  
ADD supervisor.conf /etc/supervisor/conf.d/xrdp.conf  
RUN useradd --create-home -G sudo --shell /bin/bash admin && \  
echo "admin:admin" | chpasswd  
RUN xrdp-keygen xrdp auto  
  
RUN echo 'pgrep -U $(id -u) lxsession | grep -v ^$_LXSESSION_PID | xargs --no-
run-if-empty kill' > /bin/lxcleanup.sh  
RUN chmod +x /bin/lxcleanup.sh  
RUN echo '@lxcleanup.sh' >> /etc/xdg/lxsession/LXDE/autostart  
  
CMD ["supervisord", "-n"]  
  
EXPOSE 3389  

