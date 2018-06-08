FROM node:6.4  
  
RUN echo "Setup..." && \  
curl https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - &&
\  
sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google.list' && \  
  
apt-get update && \  
apt-get install -y git ssh-client curl adduser build-essential xvfb google-
chrome-stable ; \  
  
# adding user which is used for volumes  
adduser 1000 \--force-badname && \  
  
echo "export LC_ALL=en_US.UTF-8" >> /home/1000/.bashrc && \  
echo "export LANG=en_US.UTF-8" >> /home/1000/.bashrc && \  
echo "export LANGUAGE=en_US.UTF-8" >> /home/1000/.bashrc && \  
  
# when removing adduser it removes ssh-client o_O  
apt-get purge -y curl adduser && \  
apt-get install -y ssh-client && \  
  
  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD xvfb.sh /etc/init.d/xvfb  
ADD entrypoint.sh /entrypoint.sh  
  
ENV DISPLAY :99  
#ENV CHROME_BIN /usr/bin/google-chrome  
  
ENTRYPOINT ["/entrypoint.sh"]  

