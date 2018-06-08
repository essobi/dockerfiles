FROM xueshanf/awscli  
  
ENV DOCKER_VERSION 17.09.0-ce  
  
RUN apk add --no-cache openssh-client && \  
echo "StrictHostKeyChecking no" >> /etc/ssh/ssh_config  
  
RUN curl -O
https://download.docker.com/linux/static/stable/x86_64/docker-${DOCKER_VERSION}.tgz
&& \  
tar xvf docker-${DOCKER_VERSION}.tgz docker/docker && \  
mv docker/docker /usr/local/bin/ && \  
rm -rf docker  

