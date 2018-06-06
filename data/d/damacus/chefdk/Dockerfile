FROM ubuntu:18.04  
RUN apt-get update && apt-get install curl tar rsync -y &&\  
curl -L https://www.opscode.com/chef/install.sh | bash -s -- -P chefdk &&\  
echo 'eval "$(chef shell-init bash)"' >> ~/.bashrc &&\  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV DOCKER_CHANNEL=edge \  
DOCKER_VERSION=18.02.0-ce  
  
RUN set -ex; \  
curl -fL -o docker.tgz
"https://download.docker.com/linux/static/${DOCKER_CHANNEL}/x86_64/docker-${DOCKER_VERSION}.tgz"
&&\  
tar --extract --file docker.tgz --strip-components 1 --directory
/usr/local/bin/ &&\  
rm docker.tgz &&\  
dockerd -v &&\  
docker -v &&\  
alias dokken="KITCHEN_LOCAL_YAML=.kitchen.dokken.yml kitchen"  
  
COPY modprobe.sh /usr/local/bin/modprobe  
  
ARG PROJECT=unknown  
ARG DATE=unknown  
ARG DESCRIPTION=unknown  
ARG URL=unknown  
ARG COMMIT=unknown  
  
LABEL "io.damacus.title"=$PROJECT \  
"io.damacus.created"=$DATE \  
"io.damacus.description"=$DESCRIPTION \  
"io.damacus.url"=$URL \  
"io.damacus.revision"=$COMMIT  
  

