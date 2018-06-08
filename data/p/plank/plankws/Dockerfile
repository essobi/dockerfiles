#  
# In order to run this file, you will need to be able to git clone from
getplank provate repositories  
#  
FROM plank/node:latest  
MAINTAINER rajesh@getplank.com  
  
# Make ssh dir. Create known_hosts. add github host key. chmod  
RUN mkdir -p /root/.ssh/ && \  
touch /root/.ssh/known_hosts && \  
ssh-keyscan github.com >> /root/.ssh/known_hosts  
  
# Copy over private key, and set permissions  
ADD .ssh/docker-builder-plank-utils .ssh/docker-builder-plank-server
.ssh/config /root/.ssh/  
RUN chmod -R 700 /root/.ssh  
  
# Create app directory  
RUN mkdir -p /logs/plank /usr/src/app/  
RUN cd /usr/src/app/ && \  
git clone \--depth=1 git-plank-server:getplank/plank-server.git plank-server
&& \  
git clone \--depth=1 git-plank-utils:getplank/plank-utils.git plank-utils && \  
rm -rf plank-server/.git plank-utils/.git  
  
WORKDIR /usr/src/app/plank-server  
  
RUN npm install  
  
CMD ["/usr/bin/supervisord"]  

