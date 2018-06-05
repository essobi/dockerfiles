FROM ubuntu:16.04  
MAINTAINER Shengwei An (njuasw#gmail.com)  
  
# All operations are not interactive  
ENV DEBIAN_FRONTEND noninteractive  
  
ENV TZ "US/Eastern"  
  
# Change the timezone  
# Set up a clean UTF-8 environment  
RUN echo $TZ > /etc/timezone \  
&& apt-get update && apt-get install -y tzdata \  
&& rm /etc/localtime \  
&& ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \  
&& dpkg-reconfigure -f noninteractive tzdata \  
&& apt-get install -y locales \  
&& locale-gen en_US.UTF-8 \  
&& dpkg-reconfigure locales  
  
ENV LC_ALL en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
RUN locale  
  
RUN apt-get install -y software-properties-common curl \  
&& echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true
| debconf-set-selections \  
&& add-apt-repository -y ppa:webupd8team/java \  
&& apt-get update \  
&& apt-get install -y oracle-java8-installer \  
&& rm -rf /var/cache/oracle-jdk8-installer  
  
RUN cd / \  
&& curl -O https://people.csail.mit.edu/asolar/sketch-1.7.4.tar.gz \  
&& tar zxf sketch-1.7.4.tar.gz \  
&& apt-get update \  
&& apt-get install -y build-essential g++ flex bison \  
&& cd /sketch-1.7.4/sketch-backend \  
&& chmod +x ./configure && ./configure && make \  
&& rm -rf /sketch-1.7.4.tar.gz \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV PATH "$PATH:/sketch-1.7.4/sketch-frontend"  
ENV SKETCH_HOME "/sketch-1.7.4/sketch-frontend/runtime"  

