FROM ubuntu:17.10  
MAINTAINER Mike Petersen <mike@odania-it.de>  
  
ENV TERM xterm  
RUN apt-get update && apt-get -y install vim curl autoconf zlib1g-dev unzip
bzip2 ca-certificates libffi-dev libgdbm3 \  
bison libreadline-dev libxml2-dev git docker xfsprogs net-tools python-pip
python-dev ansible gcc python-dev python3 \  
linux-headers-generic iproute2 htop strace sshpass openssh-client build-
essential \  
bash sudo libssh-dev libyaml-dev procps duplicity ncftp make g++ locales \  
ruby ruby-json rake ruby-bundler ruby-dev golang mongo-tools openjdk-8-jdk \  
apt-transport-https software-properties-common wget python-software-properties
\  
&& rm -rf /var/lib/apt/lists/*  
  
# Prepare locale  
RUN locale-gen de_DE.utf8 en_US.utf8  
RUN update-locale LANG=de_DE.UTF-8  
  
# Install docker  
RUN curl -fsSL get.docker.com -o get-docker.sh  
RUN sh get-docker.sh  
  
COPY . /opt/job-framework  
COPY docker/data /srv  
COPY docker/startup.sh /startup.sh  
WORKDIR /opt/job-framework  
  
RUN mkdir -p /home/jobs  
RUN useradd -d /home/jobs -s /bin/bash -u 1000 jobs  
RUN chown -R jobs:jobs /srv  
RUN chown -R jobs:jobs /home/jobs  
RUN chown -R jobs:jobs /opt/job-framework  
  
COPY docker/build.sh /build.sh  
RUN /build.sh  
  
# AWS ECR Login Helper for docker  
RUN mkdir -p /usr/lib/go/src/github.com/awslabs && \  
git clone https://github.com/awslabs/amazon-ecr-credential-helper.git
/usr/lib/go/src/github.com/awslabs/amazon-ecr-credential-helper && \  
cd /usr/lib/go/src/github.com/awslabs/amazon-ecr-credential-helper && \  
make && mv bin/local/docker-credential-ecr-login /usr/local/bin/docker-
credential-ecr-login  
ADD docker/docker-config.json /srv/.docker/config.json  
  
# Allow installation of ansible  
RUN echo "jobs ALL=(root) NOPASSWD:/usr/bin/pip install ansible" >>
/etc/sudoers  
  
VOLUME ["/srv"]  
CMD ["/startup.sh"]  
USER jobs  

