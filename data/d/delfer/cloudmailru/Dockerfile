FROM ubuntu:14.04  
ADD entrypoint.sh /bin/entrypoint.sh  
  
RUN export DEBIAN_FRONTEND=noninteractive && \  
apt-get update && \  
apt-get -y --force-yes install wget apt-transport-https && \  
wget -qO - https://linuxdesktopcloud.mail.ru/mail.ru-cloud.gpg | sudo apt-key
add - && \  
echo 'deb https://linuxdesktopcloud.mail.ru/deb default free' >
/etc/apt/sources.list.d/mail.ru-cloud.list && \  
apt-get update && \  
apt-get -y --force-yes install mail.ru-cloud vnc4server python expect jwm && \  
mkdir -p /root/.vnc && \  
ln -s /usr/bin/jwm /root/.vnc/xstartup && \  
mkdir /root/Cloud\ Mail.Ru && \  
locale-gen ru_RU.UTF-8  
  
# Set environment variables.  
ENV LANG ru_RU.UTF-8  
ENV HOME /root  
ENV USER root  
ENV DISPLAY :0  
# Define working directory.  
WORKDIR /root  
  
# Define default command.  
# vncserver  
#CMD ["bash"]  
EXPOSE 5900  
ENTRYPOINT ["/bin/entrypoint.sh"]  

