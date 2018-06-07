FROM ubuntu  
RUN apt-get update  
RUN apt-get -y install bash git openssh-client g++ gcc libc6-dev make curl
sudo  
  
ADD ssh/ /root/.ssh  
RUN chmod 700 /root/.ssh/*  
RUN git config --global url."git@github.com:".insteadOf "https://github.com/"  
  
RUN curl --silent --location https://deb.nodesource.com/setup_4.x | sudo bash
-  
RUN apt-get -y install nodejs python  
RUN npm install -g npm@2.7.6  
  
WORKDIR /app  
ADD . /app  
  
RUN npm install  
RUN npm run build  
RUN mkdir -p /www/connect-next  
RUN cp -rf /app/build/* /www/connect-next/.  
  
VOLUME /www  

