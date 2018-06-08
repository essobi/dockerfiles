FROM ubuntu  
RUN apt-get update && apt-get -y upgrade \  
&& apt-get -y install software-properties-common \  
&& add-apt-repository ppa:webupd8team/java \  
&& apt-get -y update \  
&& echo "oracle-java7-installer shared/accepted-oracle-license-v1-1 boolean
true" | debconf-set-selections \  
&& apt-get -y install oracle-java7-installer \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /var/cache/oracle-jdk7-installer

