FROM ubuntu:14.04  
MAINTAINER Rogier Slag  
  
# RVM and NVM  
RUN echo "# Generate locales" && \  
locale-gen en_US.UTF-8 && \  
locale-gen fr_BE.UTF-8 && \  
export LANG=en_US.UTF-8 && \  
export LC_CTYPE=fr_BE.UTF-8 && \  
  
echo "# Upgrade apt" && \  
apt-get update && apt-get upgrade -y && \  
  
echo "# Install common dev dependencies via apt" && \  
apt-get install -y git \  
curl \  
wget \  
rsync \  
patch \  
build-essential \  
python \  
time \  
&& \  
  
echo "# Install nvm" && \  
curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.25.4/install.sh |
bash && \  
  
echo "# Install rvm" && \  
gpg --keyserver hkp://keys.gnupg.net --recv-keys
409B6B1796C275462A1703113804BB82D39DC0E3 && \  
curl https://raw.githubusercontent.com/rvm/rvm/stable/binscripts/rvm-installer
| bash -s stable --ruby && \  
  
echo "# Clean" && \  
apt-get clean && rm -rf /tmp/*  
  
# Elasticsearch  
RUN wget -qO - https://packages.elastic.co/GPG-KEY-elasticsearch | sudo apt-
key add -  
RUN echo "deb http://packages.elastic.co/elasticsearch/1.7/debian stable main"
| sudo tee -a /etc/apt/sources.list.d/elk.list  
  
RUN apt-get update && apt-get install bcrypt libmagic-dev libmariadbclient-dev
libgmp-dev libpq-dev elasticsearch openjdk-7-jdk redis-server -y && apt-get
clean  
  
RUN mkdir /opt/mergemaster  
RUN mkdir /root/.ssh  
RUN mkdir /tmp/lock  
ADD merge.sh /opt/mergemaster/  
  
VOLUME ["/root/.ssh", "/tmp/lock"]  
  
CMD ["/bin/bash", "/opt/mergemaster/merge.sh"]  
  

