FROM alpine  
  
# Install main utils  
RUN apk add \--no-cache --virtual .deps-main bash bind-tools ca-certificates
curl git htop iftop iotop iproute2 jq openssh-client procps tar tcpdump tmux
whois  
  
# Install AWS CLI  
RUN apk add \--no-cache --virtual .deps-aws python py-pip &&\  
pip install awscli  
  
# Install Docker CLI & Docker Compose  
## Official compose binaries don't work in alpine, but the pip package does  
ENV DOCKER_VERSION=17.06.0-ce DOCKER_COMPOSE_VERSION=1.17.1
TERM=xterm-256color  
RUN curl -L
"https://download.docker.com/linux/static/stable/x86_64/docker-${DOCKER_VERSION}.tgz"
-o /tmp/docker.tgz &&\  
cd /tmp/ && tar zxf docker.tgz && cp docker/docker /usr/local/bin && cd / &&\  
pip install "docker-compose~=${DOCKER_COMPOSE_VERSION}" &&\  
rm -rf /tmp/*  

