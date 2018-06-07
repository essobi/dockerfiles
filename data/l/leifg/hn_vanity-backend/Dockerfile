FROM leifg/elixir:1.6  
LABEL maintainer="Leif Gensert <leif@leif.io>"  
  
RUN apk add --no-cache libc6-compat build-base curl postgresql-client bash git
openssh  
  
# Install Docker in Docker  
ENV DOCKER_VERSION="17.05.0-ce"  
RUN curl -L -o /tmp/docker-$DOCKER_VERSION.tgz
https://get.docker.com/builds/Linux/x86_64/docker-$DOCKER_VERSION.tgz \  
&& tar -xz -C /tmp -f /tmp/docker-$DOCKER_VERSION.tgz \  
&& mv /tmp/docker/* /usr/local/bin \  
&& rm -rf /tmp/*  
  
# Docker Cloud  
RUN apk -Uuv --no-cache add python py-pip  
  
ENV DOCKER_CLOUD_VERSION="1.0.9"  
RUN pip install docker-cloud==${DOCKER_CLOUD_VERSION}  
  
# Install Semantic Release  
ENV SEMANTIC_RELEASE_VERSION=1.9.1  
ADD https://github.com/semantic-release/go-semantic-
release/releases/download/v${SEMANTIC_RELEASE_VERSION}/semantic-
release_v${SEMANTIC_RELEASE_VERSION}_linux_amd64 /usr/local/bin/semantic-
release  
RUN chmod a+x /usr/local/bin/semantic-release  
  
ADD https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-
it.sh /usr/local/bin/wait-for-it  
RUN chmod a+x /usr/local/bin/wait-for-it  

