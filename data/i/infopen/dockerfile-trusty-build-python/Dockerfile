FROM infopen/jenkins-slave-ubuntu-trusty-build-deb:0.2.0  
MAINTAINER Alexandre Chaussier <a.chaussier@infopen.pro>  
  
# Install packages to manage python jobs  
RUN apt-get update && \  
apt-get install -y python3 \  
python-pip \  
python-virtualenv \  
libffi-dev \  
libpython2.7-dev \  
libpython3.4-dev \  
libssl-dev \  
libxml2-dev \  
libxslt1-dev \  
lzop  
  
# Locale management  
RUN locale-gen en_US.UTF-8  
RUN echo 'LC_ALL=en_US.UTF-8' > /etc/default/locale  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
# MongoDB management  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10 && \  
(echo "deb http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.0
multiverse" > /etc/apt/sources.list.d/mongodb-org-3.0.list) && \  
apt-get update && \  
sudo apt-get install -y mongodb-org  

