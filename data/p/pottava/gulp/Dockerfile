# Gulp v3.9 with docker client v1.13.0  
  
FROM pottava/gulp:3.9  
  
ENV DOCKER_VERSION=1.13.0  
  
RUN apk \--no-cache add \--virtual build-deps curl \  
  
# Install Docker  
&& cd / \  
&& curl \--location \--silent \--show-error -O \  
https://get.docker.com/builds/Linux/x86_64/docker-${DOCKER_VERSION}.tgz \  
&& tar xzf docker-${DOCKER_VERSION}.tgz \  
&& cp docker/docker /usr/bin/docker \  
  
# Clean up  
&& rm -rf /docker* \  
&& apk del \--purge -r build-deps  

