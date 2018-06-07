FROM ubuntu:16.04  
MAINTAINER Gremlin Inc. <support@gremlin.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
ENV SERVICE_URL https://api.staging.gremlin.com/v1  
ENV CLIENT_VERSION latest  
ENV DAEMON_VERSION latest  
ENV GREMLIN_DOCKER_IMAGE gremlin/gremlin:staging  
  
RUN apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -y apt-transport-https \  
&& echo "deb https://apt.dockerproject.org/repo ubuntu-xenial main" >
/etc/apt/sources.list.d/docker.list \  
&& apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E15DED2F B302C012
2C52609D 61A50EF6 \  
&& apt-get update \  
&& apt-get install -y curl ca-certificates dnsutils iproute docker-engine \  
&& curl -fsSL $SERVICE_URL/install/client/$CLIENT_VERSION/x86_64-unknown-
linux-musl -o /usr/bin/gremlin \  
&& curl -fsSL $SERVICE_URL/install/daemon/$DAEMON_VERSION/x86_64-unknown-
linux-musl -o /usr/sbin/gremlind \  
&& chmod +x /usr/bin/gremlin /usr/sbin/gremlind \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY entrypoint.sh /  
ENTRYPOINT ["/entrypoint.sh"]  

