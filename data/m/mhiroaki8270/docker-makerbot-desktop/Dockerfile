# The details can be found in the following web page.  
# https://support.makerbot.com/learn/makerbot-desktop-software/getting-
started/how-to-install-makerbot-desktop-for-linux_11262  
FROM ubuntu:14.04  
MAINTAINER Hiroaki Mikami "hiroaki8270@gmail.com"  
RUN apt-get update -y && \  
apt-get upgrade -y  
  
# Install apt-add-repository and wget  
RUN apt-get install software-properties-common wget -y  
  
# Add the repository  
RUN apt-add-repository 'http://downloads.makerbot.com/makerware/ubuntu' -y  
RUN wget
http://downloads.makerbot.com/makerware/ubuntu/dev@makerbot.com.gpg.key && \  
apt-key add dev@makerbot.com.gpg.key -y  
  
# Install makerware  
RUN apt-get update -y && apt-get install makerware -y  
  
# Add a user (makerbot)  
RUN useradd makerbot && \  
export uid=1000 gid=1000 && \  
mkdir -p /home/makerbot && \  
echo "makerbot:x:${uid}:${gid}:Makerbot,,,:/home/makerbot:/bin/bash" >>
/etc/passwd && \  
echo "makerbot:x:${uid}:" >> /etc/group && \  
touch /.Xauthority && \  
chmod 600 /.Xauthority && \  
chown makerbot:makerbot /.Xauthority  
  
# Add run.sh  
ADD run.sh /home/makerbot/run.sh  
RUN chmod 777 /home/makerbot/*.sh  
  
# Change the user to makerbot  
USER makerbot  
ENV XAUTHORITY /.Xauthority  
ENV HOME /home/makerbot  
  
# Start makerware  
CMD ["/home/makerbot/run.sh"]  

