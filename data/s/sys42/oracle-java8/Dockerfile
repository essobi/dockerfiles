FROM sys42/docker-base  
  
MAINTAINER Tom Nussbaumer <thomas.nussbaumer@gmx.net>  
  
RUN export DEBIAN_FRONTEND=noninteractive \  
&& apt-get update && apt-get install -y \  
software-properties-common \  
python-software-properties \  
&& echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true
| debconf-set-selections \  
&& add-apt-repository -y ppa:webupd8team/java \  
&& apt-get update && apt-get install -y \  
oracle-java8-installer \  
oracle-java8-set-default \  
&& rm -rf /var/cache/oracle-jdk8-installer \  
&& rm -rf /var/lib/apt/lists/*  

