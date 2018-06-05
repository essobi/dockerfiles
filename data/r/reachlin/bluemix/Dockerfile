FROM ubuntu:16.04  
MAINTAINER reachlin@gmail.com  
  
RUN apt-get update  
RUN apt-get install -y curl wget apt-transport-https  
  
# install docker tools, so we can use DIND to manipulate the docker on the
host  
# https://github.com/docker-library/docker  
ENV DOCKER_BUCKET get.docker.com  
ENV DOCKER_VERSION 17.04.0-ce  
ENV DOCKER_SHA256
c52cff62c4368a978b52e3d03819054d87bcd00d15514934ce2e0e09b99dd100  
RUN set -x \  
&& curl -fSL
"https://${DOCKER_BUCKET}/builds/Linux/x86_64/docker-${DOCKER_VERSION}.tgz" -o
docker.tgz \  
&& echo "${DOCKER_SHA256} *docker.tgz" | sha256sum -c - \  
&& tar -xzvf docker.tgz \  
&& mv docker/* /usr/local/bin/ \  
&& rmdir docker \  
&& rm docker.tgz \  
&& docker -v  
  
# install kubectl  
RUN curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl
-s https://storage.googleapis.com/kubernetes-
release/release/stable.txt)/bin/linux/amd64/kubectl  
RUN mv kubectl /usr/local/bin/kubectl  
RUN chmod +x /usr/local/bin/kubectl  
  
# install Bluemix CLI  
ADD http://public.dhe.ibm.com/cloud/bluemix/cli/bluemix-
cli/latest/Bluemix_CLI_amd64.tar.gz ./bx.tar.gz  
RUN tar -xvf bx.tar.gz  
RUN Bluemix_CLI/install_bluemix_cli  
RUN bx plugin install container-service -r Bluemix  
RUN bx plugin install container-registry -r Bluemix  
  
ENTRYPOINT tail -f /dev/null  

