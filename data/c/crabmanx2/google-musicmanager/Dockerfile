FROM ubuntu:16.04  
MAINTAINER Kilian Lackhove <kilian@lackhove.de>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install -y xvfb x11vnc supervisor wget libflac8
libqt4-network libqtcore4 libqtgui4 libqtwebkit4 libvorbisfile3 xdg-utils  
  
RUN wget https://dl.google.com/linux/direct/google-musicmanager-
beta_current_amd64.deb \  
&& dpkg -i google-musicmanager-beta_current_amd64.deb \  
&& rm google-musicmanager-beta_current_amd64.deb  
  
ADD install-macspoof.sh /install-macspoof.sh  
RUN /install-macspoof.sh  
  
RUN mkdir /music  
VOLUME /music  
  
RUN mkdir -p /appdata /.config /root/.config \  
&& ln -s /appdata /.config/google-musicmanager \  
&& ln -s /appdata /root/.config/google-musicmanager  
VOLUME /appdata  
  
EXPOSE 5900  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
ADD google-musicmanager.sh /google-musicmanager.sh  
  
CMD ["/usr/bin/supervisord"]  

