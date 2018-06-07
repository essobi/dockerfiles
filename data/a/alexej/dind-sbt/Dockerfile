# Use Ubuntu instead of Alpine due to glibc issues in running certain binaries  
FROM ubuntu:16.04  
# Disable warnings from apt-get installs  
ENV DEBIAN_FRONTEND=noninterative  
COPY apt-clean.sh /  
WORKDIR /src  
  
RUN apt-get update && apt-get install -y \  
apt-transport-https \  
ca-certificates \  
curl \  
software-properties-common && \  
update-ca-certificates && \  
/apt-clean.sh  
  
# Add Docker apt repo  
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add - &&
\  
add-apt-repository \  
"deb [arch=amd64] https://download.docker.com/linux/ubuntu \  
$(lsb_release -cs) \  
stable"  
  
# Add SBT apt repo  
RUN echo "deb https://dl.bintray.com/sbt/debian /" | \  
tee -a /etc/apt/sources.list.d/sbt.list && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv
2EE0EA64E40A89B84B2DF73499E82A75642AC823  
  
# Add yarn repo  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \  
echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
  
# Add nodejs repo  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -  
  
# Install Docker, openjdk8, and SBT  
RUN apt-get update && apt-get install -y \  
docker-ce \  
openjdk-8-jdk \  
sbt \  
nodejs \  
yarn && \  
/apt-clean.sh  
  
# Install latest version of SBT and print version information  
ARG SBT_VERSION=1.1.1  
RUN mkdir project && \  
echo "sbt.version = $SBT_VERSION" > project/build.properties && \  
sbt sbtVersion && \  
rm -r project  

