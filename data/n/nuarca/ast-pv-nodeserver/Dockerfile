FROM nuarca/ast-pv-base  
MAINTAINER Hasnaeen Ferdous  
  
RUN mkdir /app && cd /app && \  
git clone https://noyonthe1:noyon333@github.com/raasiel/docker-stacks.git && \  
cd /app/docker-stacks/Deploy/Docker/node/proxy-voting && \  
npm install  
  
#ADD start.sh /app/docker-stacks/Deploy/Docker/node/proxy-voting  
#ENTRYPOINT cd /app/docker-stacks/Deploy/Docker/node/proxy-voting && sh
start.sh  

