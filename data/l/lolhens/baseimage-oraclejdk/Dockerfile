FROM lolhens/baseimage:latest  
MAINTAINER LolHens <pierrekisters@gmail.com>  
  
  
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu bionic main" |
tee /etc/apt/sources.list.d/webupd8team-java.list \  
&& echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu bionic main"
| tee -a /etc/apt/sources.list.d/webupd8team-java.list \  
&& apt-get update \  
&& apt-get -y install gnupg \  
&& apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C2518248EEA14886 \  
&& apt-get remove -y gnupg \  
&& cleanimage  
  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | debconf-set-selections  
  
COPY ["bin/cleanjava", "/tmp/"]  
RUN chmod +x /tmp/cleanjava  
  
RUN apt-get update \  
&& apt-get -y install \  
oracle-java8-installer \  
&& /tmp/cleanjava \  
&& cleanimage  

