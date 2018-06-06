FROM jambr/sn.nodejs:latest  
  
RUN dnf -y -q install tar sudo && \  
dnf -y -q clean all  
  
# Download docker, the version that is compatible with docker-clouds aws built
server  
RUN cd /tmp && \  
wget --quiet https://get.docker.com/builds/Linux/i386/docker-1.11.2.tgz && \  
tar -xzf docker-*.tgz && \  
mv ./docker/docker /usr/local/bin/docker && \  
rm -rf docker* && \  
ln -s /usr/local/bin/docker /bin/docker  
  
# Setup docker  
RUN groupadd docker  
RUN usermod -aG docker root  
  
# Hacky mc Hack Hack to ensure that docker is always run with sudo  
RUN mv /usr/local/bin/docker /usr/local/bin/docker_root  
ADD docker /usr/local/bin/docker  
  
# Add our image cleaner app  
COPY package.json /app/  
RUN npm install --production  
  
COPY . /app/  
  
ENTRYPOINT ["node", "index.js"]  

