#  
# Ubuntu Dockerfile  
#  
# https://github.com/tamboraorg/docker/creUbuntu  
# (adapted from https://github.com/dockerfile/ubuntu )  
# Pull base image.  
FROM ubuntu:16.04  
# version: yyyy.n for stable versions / 0.yyyy for development  
ENV CRE_VERSION 0.2010  
ENV UBUNTU_VERSION 16.04  
ENV DOCKER_GEN_VERSION 0.7.4  
RUN mkdir -p /cre && touch /cre/versions.txt && \  
echo "$(date +'%F %R') \t creUbuntu \t $(cat /usr/lib/os-release | grep PRETTY
| sed -e "s/^PRETTY_NAME=\"Ubuntu //" -e "s/\"$//")" >> /cre/versions.txt  
  
# Install.  
RUN \  
sed -i 's/# \\(.*multiverse$\\)/\1/g' /etc/apt/sources.list && \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y build-essential && \  
apt-get install -y software-properties-common && \  
apt-get install -y byobu curl git htop man unzip vim wget && \  
rm -rf /var/lib/apt/lists/*  
  
# Add files.  
#ADD root/.bashrc /root/.bashrc  
#ADD root/.gitconfig /root/.gitconfig  
#ADD root/.scripts /root/.scripts  
RUN apt-get update && apt-get -y install apt-transport-https curl libzip4
libssh2-1  
  
# Install docker-gen (generates files from templates with docker data filled
in)  
RUN wget https://github.com/jwilder/docker-
gen/releases/download/$DOCKER_GEN_VERSION/docker-gen-linux-
amd64-$DOCKER_GEN_VERSION.tar.gz \  
&& tar -C /usr/local/bin -xvzf docker-gen-linux-
amd64-$DOCKER_GEN_VERSION.tar.gz \  
&& rm /docker-gen-linux-amd64-$DOCKER_GEN_VERSION.tar.gz  
  
RUN echo "$(date +'%F %R') \t docker-gen \t $(docker-gen -version)" >>
/cre/versions.txt  
  
# Copy shoremen to handle Procfile (Process Managment)  
COPY shoreman.sh /usr/local/bin/shoreman  
RUN chmod 755 /usr/local/bin/shoreman  
  
# Set environment variables.  
ENV HOME /root  
  
# Define working directory.  
WORKDIR /root  
  
# Define default command.  
CMD ["bash"]  
  

