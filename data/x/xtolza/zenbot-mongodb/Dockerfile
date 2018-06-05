FROM ubuntu:latest  
  
RUN apt update  
RUN apt upgrade  
RUN apt install -y git npm curl  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
RUN npm install -g n  
RUN n 6.11.0  
RUN git clone https://github.com/carlos8f/zenbot.git /zenbot  
WORKDIR /zenbot  
RUN cd /zenbot  
RUN npm install -g node-gyp && npm install --unsafe-perm  
RUN cp conf-sample.js conf.js  
# RUN apt install -y mongodb  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv
0C49F3730359A14518585931BC711F9BA15703C6  
RUN echo "deb [ arch=amd64,arm64 ] http://repo.mongodb.org/apt/ubuntu
xenial/mongodb-org/3.4 multiverse" | tee /etc/apt/sources.list.d/mongodb-
org-3.4.list  
RUN apt update  
RUN apt install -y mongodb-org  
RUN mkdir /data/db -p  
RUN rm -R /zenbot/.git  
RUN apt purge -y git  
RUn apt autoremove -y  
RUN apt clean  
  
CMD mongod  

