FROM docker.io/java:openjdk-7-jdk  
MAINTAINER Jess Malvin Chin, jess@teamcodeflux.com  
RUN apt-get update && apt-get install -y curl \  
openssh-server \  
make \  
build-essential \  
libssl-dev \  
zlib1g-dev \  
libbz2-dev \  
libreadline-dev \  
libsqlite3-dev \  
wget \  
curl \  
thrift-compiler \  
libpq-dev \  
llvm && \  
rm -rf /var/lib/apt/lists/*  
  
ENV HOME /home/jenkins  
ENV PYENV_ROOT $HOME/.pyenv  
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH  
ENV DOCKER_COMPOSE_VERSION 1.6.2  
COPY id_rsa.pub /home/jenkins/.ssh/authorized_keys  
  
RUN useradd jenkins && \  
mkdir /var/run/sshd && \  
mkdir -p /home/jenkins/.ssh && \  
chown -R jenkins /home/jenkins && chmod 0700 /home/jenkins/.ssh  
  
RUN curl -sSL https://get.docker.com/ | sh && \  
usermod -aG docker jenkins && \  
curl -L
https://github.com/docker/compose/releases/download/$DOCKER_COMPOSE_VERSION/docker-
compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose && \  
chmod +x /usr/local/bin/docker-compose  
  
USER jenkins  
WORKDIR /home/jenkins  
RUN git clone https://github.com/yyuu/pyenv.git ~/.pyenv && \  
pyenv install 3.4.3 && \  
pyenv global 3.4.3 && \  
pyenv rehash  
  
USER root  
EXPOSE 22  
CMD /usr/sbin/sshd -D  

