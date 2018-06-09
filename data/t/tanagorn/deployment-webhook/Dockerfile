FROM tanagorn/docker-base:node-6.11.0-slim  
  
ENV HOME=/opt/app \  
TEMP=/tmp/app  
  
WORKDIR $HOME  
  
EXPOSE 3000  
# Set the default command to run when a container starts  
ENTRYPOINT ["pm2-docker", "start", "pm2-process.yml"]  
  
# Install app dependencies  
COPY . $TEMP  
  
# Build Application  
# Optimize images  
RUN mkdir -p /opt/app \  
&& mkdir -p /tmp/app \  
&& cd ${TEMP} \  
  
&& npm install --production --no-optional \  
&& npm install pm2 -g \  
&& npm run build \  
&& cp -a node_modules dist ${HOME} \  
&& export SOURCE_COMMIT="${SOURCE_COMMIT:-$(git rev-parse HEAD)}" \  
&& export SOURCE_BRANCH="${SOURCE_BRANCH:-$(git rev-parse --abbrev-ref HEAD)}"
\  
&& export SOURCE_TAG="${SOURCE_TAG:-$(git describe --tags --abbrev=0)}" \  
&& echo -n > version.txt \  
&& echo 'SOURCE_COMMIT='${SOURCE_COMMIT} >> version.txt \  
&& echo 'SOURCE_BRANCH='${SOURCE_BRANCH} >> version.txt \  
&& echo 'SOURCE_TAG='${SOURCE_TAG} >> version.txt \  
&& cp package.json pm2-process.yml version.txt robot-*.sh ${HOME} \  
  
&& apt-get purge -y --auto-remove git \  
&& apt-get clean \  
&& rm -rf /tmp/* /var/tmp/*  

