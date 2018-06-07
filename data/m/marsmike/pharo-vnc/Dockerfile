FROM debian:jessie  
  
MAINTAINER Mike Müller <mike@objektarium.de>  
ENV REFRESHED_AT 2016-05-03  
USER root  
  
RUN adduser --gecos "" \--disabled-password --home /home/pharo pharo  
  
RUN apt-get update  
RUN apt-get install -y unzip wget tightvncserver fvwm  
  
# add Pharo50 prerequisites  
RUN dpkg --add-architecture i386  
RUN apt-get update  
RUN apt-get install -y libx11-6:i386  
RUN apt-get install -y libgl1-mesa-glx:i386  
RUN apt-get install -y libfontconfig1:i386  
RUN apt-get install -y libssl1.0.0:i386  
  
EXPOSE 5901  
ENV HOME /home/pharo  
ENV USER pharo  
  
RUN mkdir -p /home/pharo/.vnc/  
RUN echo "mypassword123" | vncpasswd -f > /home/pharo/.vnc/passwd  
RUN chmod 600 /home/pharo/.vnc/passwd  
  
ADD xstartup /home/pharo/.vnc/xstartup  
RUN chmod 755 /home/pharo/.vnc/xstartup  
  
RUN chown -R pharo:users /home/pharo  
  
USER pharo  
RUN vncserver -kill :1 && rm -rfv /tmp/.X* ; echo "remove old vnc locks to be
a reattachable container"  
CMD vncserver :1 -geometry 2048x1536 -depth 24 && tail -F
/home/pharo/.vnc/*:1.log  

