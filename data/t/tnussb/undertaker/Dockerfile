################################################################################  
#  
# Undertaker - Garbage Collection for Docker Containers and Images  
#  
# (*) based on Alpine Linux due to its incredible small size  
# (*) relies on the availability of the Docker binary at:  
# https://get.docker.com/builds/Linux/x86_64/docker-${DOCKER_VERSION}  
# (*) has to be started with docker socket bind-mounted:  
# docker run --rm \  
# -v /var/run/docker.sock:/var/run/docker.sock \  
# tnussb/undertaker:X.Y.Z  
#  
################################################################################  
FROM gliderlabs/alpine:3.2  
  
MAINTAINER Tom Nussbaumer <thomas.nussbaumer@gmx.net>  
  
RUN export DOCKER_VERSION="1.8.1" && apk -U add bash curl grep \  
&& curl --output /bin/docker
https://get.docker.com/builds/Linux/x86_64/docker-${DOCKER_VERSION} \  
&& chmod +x /bin/docker \  
&& apk del curl \  
&& rm /var/cache/apk/*  
  
COPY ./undertaker ./REPO_AND_VERSION /  
COPY ./image-excludes ./container-excludes /etc/undertaker/  
  
ENTRYPOINT ["/undertaker"]  

