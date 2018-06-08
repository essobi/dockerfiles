#  
# Scala 2.12.4 Dockerfile  
# Pull base image  
FROM openjdk:9-slim  
  
ENV SCALA_VERSION=2.12.4  
ENV SCALA_HOME=/usr/share/scala  
  
# Install scala and cleanup  
RUN apt-get update; \  
apt-get install -y wget; \  
cd "/tmp"; \  
wget
"https://downloads.typesafe.com/scala/${SCALA_VERSION}/scala-${SCALA_VERSION}.tgz";
\  
tar xzf "scala-${SCALA_VERSION}.tgz"; \  
mkdir "${SCALA_HOME}"; \  
rm "/tmp/scala-${SCALA_VERSION}/bin/"*.bat; \  
mv "/tmp/scala-${SCALA_VERSION}/bin" "/tmp/scala-${SCALA_VERSION}/lib"
"${SCALA_HOME}"; \  
ln -s "${SCALA_HOME}/bin/"* "/usr/bin/"; \  
# Clean ups  
apt-get remove -y wget; \  
rm -rf /var/lib/apt/lists/*; \  
rm -rf "/tmp/"*  
  
# Define working directory  
WORKDIR /root  

