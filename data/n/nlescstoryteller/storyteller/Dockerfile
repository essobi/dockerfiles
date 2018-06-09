# Dockerfile to create a machine with  
# - basic linux functions (curl,wget,python, etc)  
# - Lastest JDK installed  
FROM ubuntu:latest  
MAINTAINER m.vanmeersbergen@esciencecenter.nl  
  
# Update the APT cache  
RUN apt-get update  
RUN apt-get upgrade -y  
  
# Install and setup project dependencies  
RUN apt-get install -y \  
git \  
ssh \  
rsync \  
curl \  
wget \  
python3 \  
python3-pip \  
cmake \  
build-essential \  
libsqlite3-dev \  
locales  
  
# Generic stuff  
RUN /usr/sbin/locale-gen en_US.UTF-8  
ENV LANG='en_US.UTF-8' LC_ALL='en_US.UTF-8'  
# install cwltool  
RUN apt-get install -y python-pip  
RUN pip install cwltool  
  
# prepare for Java download  
RUN apt-get install -y python-software-properties  
RUN apt-get install -y software-properties-common  
  
# grab oracle java (auto accept licence)  
RUN add-apt-repository -y ppa:webupd8team/java  
RUN apt-get update  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
RUN apt-get install -y oracle-java8-installer maven  
  
# node  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -  
RUN apt-get install -y nodejs  
RUN npm install -g yarn  
  
# environment  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
ENV PYTHON_HOME /usr/lib/python3  
  
# make barebones  
RUN mkdir /src  
  
# cltl/StoryTeller  
RUN mkdir /src/StoryTeller  
COPY pom.xml install.sh /src/StoryTeller/  
COPY scripts /src/StoryTeller/scripts  
COPY src /src/StoryTeller/src  
  
WORKDIR /src/StoryTeller  
RUN chmod +wrx install.sh  
RUN sync  
RUN ./install.sh  

