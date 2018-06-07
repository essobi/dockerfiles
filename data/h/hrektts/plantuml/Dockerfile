FROM hrektts/ubuntu:latest  
LABEL maintainer="mps299792458@gmail.com" \  
version="1.2018.2"  
  
ENV PLANTUML_VERSION="1.2018.2"  
WORKDIR /usr/share/java  
  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886
\  
&& echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" \  
> /etc/apt/sources.list.d/webupd8team-java.list \  
&& apt-get update \  
&& echo "oracle-java9-installer shared/accepted-oracle-license-v1-1 select
true" \  
| debconf-set-selections \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y \  
curl oracle-java9-installer maven graphviz fonts-takao-pgothic \  
&& curl -o plantuml.jar -JLsS \  
http://sourceforge.net/projects/plantuml/files/plantuml.${PLANTUML_VERSION}.jar/download
\  
&& rm -rf /var/lib/apt/lists/*  
  
COPY plantuml.sh /usr/local/bin/plantuml  
RUN chmod 755 /usr/local/bin/plantuml  
  
ENV JAVA_HOME=/usr/lib/jvm/java-9-oracle  
  
WORKDIR /data  
VOLUME ["/data"]  

