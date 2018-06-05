FROM openjdk:8u141  
  
MAINTAINER Sondre T. Johannessen <sondre@vimond.com>  
  
# Get dependencies  
RUN apt-get update  
RUN apt-get -y install apt-transport-https ca-certificates curl gnupg2
software-properties-common  
  
# Add docker to apt-get  
RUN curl -fsSL https://download.docker.com/linux/$(. /etc/os-release; echo
"$ID")/gpg | apt-key add -  
RUN apt-key fingerprint 0EBFCD88  
RUN add-apt-repository \  
"deb [arch=amd64] https://download.docker.com/linux/$(. /etc/os-release; echo
"$ID") \  
$(lsb_release -cs) \  
stable"  
  
# Install node  
#RUN curl -sL https://deb.nodesource.com/setup_8.x -o nodesource_setup.sh  
#RUN bash nodesource_setup.sh  
#RUN apt-get install nodejs  
# Install CQL  
#RUN echo "deb http://debian.datastax.com/community stable 21x main" | tee -a
/etc/apt/sources.list.d/cassandra.sources.list  
#RUN curl -L http://debian.datastax.com/debian/repo_key | apt-key add -  
#RUN apt-get update  
#RUN apt-get -y install cassandra=2.1.15  
#RUN cqlsh --version  
#RUN service cassandra stop  
#RUN rm -rf /var/lib/cassandra/data/system/*  
# Install mvn  
RUN apt-get -y install maven  
RUN mvn --version  
  
# Install docker and docker-compose  
RUN apt-get update  
RUN apt-get -y install docker-ce  
RUN curl -L https://github.com/docker/compose/releases/download/1.16.1/docker-
compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose  
RUN chmod +x /usr/local/bin/docker-compose  
RUN docker-compose --version  
RUN docker --version  
  
# Env variables  
ENV SCALA_VERSION 2.10.2  
ENV SBT_VERSION 0.13.6  
# Scala expects this file  
RUN touch /usr/lib/jvm/java-8-openjdk-amd64/release  
  
# Install Scala  
## Piping curl directly in tar  
RUN \  
curl -fsL
https://downloads.typesafe.com/scala/$SCALA_VERSION/scala-$SCALA_VERSION.tgz |
tar xfz - -C ./ && \  
touch /root/.bashrc && \  
echo >> /root/.bashrc && \  
echo "export PATH=~/scala-$SCALA_VERSION/bin:$PATH" >> /root/.bashrc  
  
# Install sbt  
RUN \  
curl -L -o sbt-$SBT_VERSION.deb
https://dl.bintray.com/sbt/debian/sbt-$SBT_VERSION.deb && \  
dpkg -i sbt-$SBT_VERSION.deb && \  
rm sbt-$SBT_VERSION.deb && \  
apt-get update && \  
apt-get install sbt && \  
sbt sbtVersion  
  
EXPOSE 8888 9000  
WORKDIR /root  
  

