FROM openjdk:9-slim  
  
ENV SBT_VERSION=1.1.0  
# Install scala and cleanup  
RUN apt-get update; \  
apt-get install -y wget; \  
cd "/tmp"; \  
wget
"https://github.com/sbt/sbt/releases/download/v$SBT_VERSION/sbt-$SBT_VERSION.tgz";
\  
tar xzf "sbt-$SBT_VERSION.tgz" && \  
rm -f "sbt-$SBT_VERSION.tgz" && \  
mv sbt /usr/local && \  
ln -s /usr/local/sbt/bin/sbt /usr/local/bin/sbt && \  
chmod 0755 /usr/local/bin/sbt && \  
# Run sbt once to trigger dependencies download  
sbt update && \  
# Clean ups  
rm -rf /var/lib/apt/lists/*; \  
rm -rf "/tmp/"*  
  

