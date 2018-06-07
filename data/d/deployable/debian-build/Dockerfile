FROM debian:7  
# docker build -t deployable/debian-build --build-arg
DOCKER_BUILD_PROXY=http://10.8.8.8:3142 --build-arg DOCKER_BUILD_LOCALE=au .  
# Source build packages locally  
ARG DOCKER_BUILD_PROXY=  
  
# Fix ipv6 wierdness with new debian mirror resolver  
RUN echo 'precedence ::ffff:0:0/96 100' > /etc/gai.conf  
  
# Turn off documentation  
COPY dpkg.01_nodoc /etc/dpkg/dpkg.conf.d/01_nodoc  
# Install common build tools  
RUN set -uex; \  
export http_proxy=${HTTP_PROXY-$DOCKER_BUILD_PROXY}; \  
apt-get update; \  
apt-get install --no-install-suggests --no-install-recommends -y \  
make \  
curl \  
wget \  
ca-certificates \  
gcc \  
g++ \  
git \  
libc6-dev \  
libtool \  
autoconf \  
automake \  
libssl-dev; \  
apt-get clean all  
  
  
label org.label-schema.name = "deployable/debian-build" \  
org.label-schema.version = "20171010" \  
org.label-schema.vendor="Deployable" \  
org.label-schema.docker.cmd="docker run -ti deployable/debian-build" \  
org.label-schema.url="https://github.com/deployable/docker-debian-build" \  
org.label-schema.vcs-url="https://github.com/deployable/docker-debian-
build.git" \  
org.label-schema.vcs-ref = "cd645644de4c0a13b2129415fc5969c7d280661c" \  
org.label-schema.schema-version="1.0"  

