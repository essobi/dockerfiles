FROM fedora  
  
WORKDIR /  
  
RUN yum -y upgrade  
RUN yum install -y make npm  
  
RUN npm install -g ldf-server  
  
ADD config.json .  
  
CMD ldf-server config.json 5000 4  

