FROM artworkad/alpine-node-nightly:latest  
  
MAINTAINER Artjom Zabelin <artjomzabelin@gmail.com>  
  
RUN apk update && \  
apk add --no-cache git supervisor openssh wget gcc g++ make linux-headers
python && \  
mkdir -p /var/log/supervisor /root/.ssh && \  
touch /root/.ssh/known_hosts  
  
# Copy supervisord.conf  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# Copy over private key, and set permissions  
COPY deploy-key/deploy-key /root/.ssh/id_rsa  
RUN chmod 400 /root/.ssh/id_rsa  
  
# Add githubs key  
RUN ssh-keyscan github.com >> /root/.ssh/known_hosts  
  
# Define working directory  
WORKDIR /app  
  
# Clone the conf files into the docker container  
RUN \  
cd /app && \  
git clone git@github.com:ArtworkAD/idea_generator_service.git && \  
cd idea_generator_service && \  
npm install  
  
CMD ["/usr/bin/supervisord", "--configuration",
"/etc/supervisor/conf.d/supervisord.conf"]  

