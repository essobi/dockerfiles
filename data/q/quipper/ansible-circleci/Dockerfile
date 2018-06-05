FROM ruby:2.3.4  
ENV DOCKER_CLIENT_VERSION="17.03.0-ce"  
ENV ANSIBLE_VERSION="2.3.0"  
ENV TOWERCLI_VERSION="2.3.0"  
# install essentials  
RUN apt-get update \  
&& apt-get -y install --no-install-recommends \  
curl git-core dnsutils build-essential jq \  
python-all-dev python-pip \  
python-yaml python-jinja2 python-httplib2 python-paramiko python-pkg-resources
python-keyczar \  
&& apt-get clean \  
&& rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*  
  
RUN pip install "ansible==${ANSIBLE_VERSION}"  
RUN pip install "ansible-tower-cli==${TOWERCLI_VERSION}"  
RUN pip install awscli  
  
# Install Docker client  
RUN curl -L -o /tmp/docker-${DOCKER_CLIENT_VERSION}.tgz
https://get.docker.com/builds/Linux/x86_64/docker-${DOCKER_CLIENT_VERSION}.tgz
\  
&& tar -xz -C /tmp -f /tmp/docker-${DOCKER_CLIENT_VERSION}.tgz \  
&& mv /tmp/docker/* /usr/bin  

