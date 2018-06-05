FROM hypriot/rpi-node  
  
LABEL maintainer "Aleksandr Bochev <red.avtovo@gmail.com>"  
  
#=============  
# Set WORKDIR  
#=============  
WORKDIR /root  
  
RUN apt-get update &&\  
apt-get install -y gammu-smsd && \  
npm update npm && \  
npm install -g boxcar-cli  
# npm cache clean && \  
# apt-get remove --purge -y npm && \  
# apt-get autoremove --purge -y && \  
# rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
# apt-get clean  
COPY scripts scripts/config.template.conf scripts/sendToBoxCar.sh\  
/root/  
  
RUN mkdir -p /var/spool/sms/inbox/ &&\  
mkdir -p /var/spool/sms/outbox/ &&\  
mkdir -p /var/spool/sms/sent/ &&\  
mkdir -p /var/spool/sms/error/ &&\  
chmod +x /root/*.sh  
ENTRYPOINT /root/entry-point.sh

