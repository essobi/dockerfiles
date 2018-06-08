FROM node:4.4.5  
# Install designer  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
RUN apt update && apt install unzip  
  
COPY package.json /usr/src/app  
  
RUN npm install  
  
COPY . /usr/src/app  
  
RUN cd /usr/src/app/structure/template && npm install  
  
EXPOSE 1337  
ADD entrypoint.sh /  
# Setup for ssh onto github  
RUN mkdir -p /root/.ssh  
  
ADD id_rsa /root/.ssh/id_rsa  
RUN chmod 700 /root/.ssh/id_rsa  
  
ADD ssh_config /root/.ssh/config  
  
RUN chmod 777 /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

