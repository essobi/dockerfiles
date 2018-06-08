## BUILDING  
## (from project root directory)  
## $ docker build -t node-js-for-ervin210-buba .  
##  
## RUNNING  
## $ docker run -p 3000:3000 node-js-for-ervin210-buba  
##  
## CONNECTING  
## Lookup the IP of your active docker host using:  
## $ docker-machine ip $(docker-machine active)  
## Connect to the container at DOCKER_IP:3000  
## replacing DOCKER_IP for the IP of your active docker host  
  
FROM gcr.io/bitnami-containers/minideb-extras:jessie-r14-buildpack  
  
MAINTAINER Bitnami <containers@bitnami.com>  
  
ENV STACKSMITH_STACK_ID="ac7ca9x" \  
STACKSMITH_STACK_NAME="Node.js for ervin210/buba" \  
STACKSMITH_STACK_PRIVATE="1"  
  
# Install required system packages  
RUN install_packages libc6 libssl1.0.0 libncurses5 libtinfo5 libsqlite3-0
zlib1g libbz2-1.0 libreadline6 libstdc++6 libgcc1 ghostscript imagemagick
libmysqlclient18  
  
RUN bitnami-pkg install node-7.10.0-0 --checksum
7209e62e60335308287cba38bc18fb34245d41b86bc7ffd3ad26413f186c529b  
  
ENV PATH=/opt/bitnami/node/bin:/opt/bitnami/python/bin:$PATH \  
NODE_PATH=/opt/bitnami/node/lib/node_modules  
  
## STACKSMITH-END: Modifications below this line will be unchanged when
regenerating  
  
# Node base template  
COPY . /app  
WORKDIR /app  
  
RUN npm install  
  
CMD ["node"]  

