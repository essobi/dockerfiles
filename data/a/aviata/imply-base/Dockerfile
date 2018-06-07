FROM ubuntu  
  
ENV IMPLY_VERSION 1.0.0  
  
RUN mkdir /imply \  
&& apt-get update \  
&& apt-get -y upgrade \  
&& apt-get install -y curl python software-properties-common vim wget \  
&& curl -sL https://deb.nodesource.com/setup_4.x | sudo -E bash - \  
&& apt-add-repository ppa:webupd8team/java \  
&& echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true
| /usr/bin/debconf-set-selections \  
&& apt-get update \  
&& apt-get install -y oracle-java8-installer nodejs \  
&& curl -O http://static.imply.io/release/imply-${IMPLY_VERSION}.tar.gz \  
&& tar -xzf imply-${IMPLY_VERSION}.tar.gz \  
&& mv imply-${IMPLY_VERSION} /imply/  
  
WORKDIR /imply/imply-${IMPLY_VERSION}  

