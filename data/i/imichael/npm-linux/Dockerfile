FROM node:0.10.39  
WORKDIR /src  
  
MAINTAINER michaelmartinez@me.com  
  
RUN echo " IdentityFile /root/.ssh/id_rsa" >> /etc/ssh/ssh_config && \  
mkdir -p /root/.ssh/ && \  
touch /root/.ssh/known_hosts && \  
ip=$(node -e "require('dns').lookup('github.com', function(err, ip) {
console.log(ip);});") && \  
ssh-keyscan -H $ip >> ~/.ssh/known_hosts 2>/dev/null && \  
ssh-keyscan -H github.com >> ~/.ssh/known_hosts 2>/dev/null  
  
ENTRYPOINT ["npm", "install", "--loglevel", "verbose"]  
  

