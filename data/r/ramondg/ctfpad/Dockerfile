FROM node  
MAINTAINER Ramon de Graaff  
  
ENV http_proxy=$http_proxy  
ENV https_proxy=$https_proxy  
  
RUN apt-get update  
RUN apt-get install -y openssl sqlite3  
RUN useradd -ms /bin/bash etherpad  
USER etherpad  
WORKDIR /home/etherpad/  
RUN git clone https://github.com/StratumAuhuur/CTFPad.git  
WORKDIR /home/etherpad/CTFPad/  
RUN git clone https://github.com/ether/etherpad-lite.git  
RUN npm install  
WORKDIR /home/etherpad/CTFPad/etherpad-lite/  
RUN mv settings.json.template settings.json  
WORKDIR /home/etherpad/CTFPad/  
RUN openssl genrsa -out key.pem 4096  
RUN openssl req -new -nodes -key key.pem -out csr.pem -subj "/C=US/ST=Some-
State/L=Springfield/O=Internet Widgits Pty Ltd/CN=etherpad"  
RUN openssl x509 -req -days 3650 -in csr.pem -signkey key.pem -out cert.pem  
RUN mv config.json.example config.json  
RUN sqlite3 ctfpad.sqlite < ctfpad.sql  
RUN mkdir uploads  
  
EXPOSE 1234  
EXPOSE 1235  
ENTRYPOINT ["/usr/local/bin/node", "/home/etherpad/CTFPad/main.js"]  
  

