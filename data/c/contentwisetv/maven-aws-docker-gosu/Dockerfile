FROM contentwisetv/maven-gosu:jdk8  
ARG AWSCLI_VERSION="1.14.55"  
ARG DOCKER_VERSION="17.12.1-ce"  
RUN apt-get update && apt-get install -y \  
python-pip && \  
rm -rf /var/lib/apt/lists/*  
RUN pip install \  
awscli==${AWSCLI_VERSION}  
RUN curl -L
https://download.docker.com/linux/static/stable/x86_64/docker-${DOCKER_VERSION}.tgz
| tar -xz -C /usr/local/bin --strip 1

