FROM debian:jessie  
  
RUN ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime  
  
RUN apt-get update && apt-get install -y openssh-server  
RUN ( mkdir /var/run/sshd && \  
useradd -s /bin/bash worker && \  
mkdir /home/worker && \  
chown -R worker:worker /home/worker)  
  
RUN echo 'root:newpass' | chpasswd  
RUN echo 'worker:newpass' | chpasswd  
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
  
# SSH login fix. Otherwise user is kicked off after login  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
  
RUN apt-get install -y rtmpdump swftools libxml2-utils libav-tools gnome-
schedule vim sudo wget cron  
  
ADD rec_radiko.sh /usr/local/bin/rec_radiko.sh  
ADD rec2.sh /usr/local/bin/rec2.sh  
ADD crontab /home/worker/crontab  
ADD chan /home/worker/chan  
ADD startservice.sh /root/startservice.sh  
ADD ./sudoers /etc/sudoers.d/sudoers  
  
RUN mkdir -p /usr/local/rr; chmod 1777 /usr/local/rr  
RUN (cd /usr/local; \  
wget -O - "https://www.dropbox.com/download?plat=lnx.x86_64" | tar xzf -)  
#RUN su worker -c "crontab /home/worker/crontab"  
EXPOSE 22  
CMD ["/root/startservice.sh"]  
#CMD ["/usr/sbin/sshd", "-D"]  

