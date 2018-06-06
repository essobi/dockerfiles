FROM factual/docker-base-openjdk  
MAINTAINER Maxime DEVALLAND <maxime@factual.com>  
  
RUN apt-get update && apt-get install -y git zip ipmitool unzip wget && rm -r
/var/lib/apt/lists/*  
  
RUN useradd -Ur -d /opt/collins collins  
RUN for dir in /build /build/collins /var/log/collins /var/run/collins; do
mkdir $dir; done  
ENV APP_HOME /opt/collins  
ENV LOG_HOME /var/log/collins  
  
RUN git clone https://github.com/tumblr/collins /build/collins  
  
WORKDIR /build  
# get Play, Collins, build, and deploy it to /opt/collins  
#COPY collins/ /build/collins/  
RUN echo "Fetching Play 2.3.9" && \  
wget -q http://downloads.typesafe.com/typesafe-activator/1.3.4/typesafe-
activator-1.3.4-minimal.zip -O /build/typesafe-activator-1.3.4-minimal.zip &&
\  
unzip -q ./typesafe-activator-1.3.4-minimal.zip && \  
cd collins && \  
java -version 2>&1 && \  
PLAY_CMD=/build/activator-1.3.4-minimal/activator ./scripts/package.sh && \  
unzip -q /build/collins/target/collins.zip -d /opt/ && \  
cd / && rm -rf /build  
  
# Add in all the default configs we want in this build so collins can run.  
# Override /opt/collins/conf with your own configs with -v  
COPY database.conf.mo /opt/collins/conf/database.conf.mo  
  
RUN mkdir -p /etc/service/collins/  
COPY collins.sh /etc/service/collins/run  
  
WORKDIR /opt/collins  
EXPOSE 9000  

