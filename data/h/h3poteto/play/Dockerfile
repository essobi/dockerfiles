FROM h3poteto/sbt:0.13.16  
  
USER root  
  
RUN set -x && \  
curl -sL https://deb.nodesource.com/setup_6.x | bash - && \  
apt-get install -y --no-install-recommends \  
build-essential \  
mysql-client \  
nodejs && \  
rm -rf /var/lib/apt/lists/*  
  
USER scala  

