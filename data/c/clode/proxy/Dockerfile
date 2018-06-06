FROM phusion/baseimage  
#Install Node  
ENV NODE_VERSION 7.5.0  
RUN curl -o-
https://raw.githubusercontent.com/creationix/nvm/v0.32.1/install.sh | bash  
RUN /bin/bash -c '. /root/.nvm/nvm.sh && nvm install $NODE_VERSION && nvm
alias default $NODE_VERSION'  
ENV PATH /root/.nvm/versions/node/v$NODE_VERSION/bin:$PATH  
  
#Install Forever  
RUN npm install -g forever  
  
#Expose Ports  
EXPOSE 443  
EXPOSE 80  
#Update Packages  
RUN apt-get update  
  
RUN apt-get install -y build-essential  
  
#Install Let's Encrypt  
RUN apt-get install -y letsencrypt  
  
#Clean  
RUN apt-get clean  
RUN apt-get autoremove  
  
#Setup Cert Directory  
VOLUME /etc/letsencrypt  
  
#Add Application Code  
WORKDIR /root  
ADD ./ ./  
  
#Install Modules  
RUN npm install --loglevel=error  
  
ENTRYPOINT ["forever","-v","--sourceDir","/root","--spinSleepTime","3000","--
workingDir","/root","proxy.js"]  

