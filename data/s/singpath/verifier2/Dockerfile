FROM node:4.2-slim  
  
ENV SINGPATH_FIREBASE_SECRET=""  
ENV SINGPATH_FIREBASE_QUEUE="https://singpath-
play.firebaseio.com/singpath/queues/default"  
ENV SINGPATH_PUSH_USER_ID="#1"  
ENV SKIP_BUILD="0"  
# Update npm, the docker client (for developpement) and create expected
folders.  
RUN apt-get update -y && \  
apt-get install -y git && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
npm install npm -g && \  
npm -v && \  
curl -SL -O https://get.docker.com/builds/Linux/x86_64/docker-1.9.0 && \  
chmod +x docker-1.9.0 && \  
mv docker-1.9.0 /usr/local/bin/docker && \  
mkdir -p /app && \  
mkdir -p $SINGPATH_DOCKER_CERT_PATH \  
mkdir -p /app/bin  
  
ENV PATH="$PATH:/app/bin"  
# Install the app dependencies.  
WORKDIR /app  
COPY ./package.json /app/package.json  
RUN npm install && \  
npm cache clean  
  
RUN adduser --system verifier  
USER verifier  
  
# Add the rest of the app files.  
COPY ./src /app/src  
COPY ./tests /app/tests  
COPY ./bin /app/bin  
COPY ./verifiers /app/verifiers  
COPY .eslintrc images.json entrypoint.sh /app/  
  
LABEL com.singpath.verifier="master"  
  
ENTRYPOINT ["/app/entrypoint.sh"]  
CMD ["/app/bin/verifier", "run"]  

