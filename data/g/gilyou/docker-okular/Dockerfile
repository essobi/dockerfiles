FROM ubuntu:bionic  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get install -y \  
\--no-install-recommends \  
okular \  
kubuntu-desktop && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV HOME /home/xiaox  
RUN useradd --create-home --home-dir $HOME xiaox && \  
chown -R xiaox:xiaox $HOME  
  
RUN echo "QT_X11_NO_MITSHM=1" >> /etc/environment  
  
USER xiaox  
  
ENV QT_X11_NO_MITSHM=1  
ENTRYPOINT ["/usr/bin/okular"]  

