FROM nanobox/runit  
  
# Create directories  
RUN mkdir -p \  
/var/log/gonano \  
/var/nanobox \  
/opt/nanobox/hooks  
  
# Install and rsync  
RUN apt-get update -qq && \  
apt-get install -y rsync && \  
apt-get clean all && \  
rm -rf /var/lib/apt/lists/*  
  
# Download logvac  
RUN curl \  
-f \  
-k \  
-o /usr/local/bin/logvac \  
https://d3ep67zochz54j.cloudfront.net/logvac/linux/amd64/logvac && \  
chmod 755 /usr/local/bin/logvac  
  
# Download md5 (used to perform updates in hooks)  
RUN curl \  
-f \  
-k \  
-o /var/nanobox/logvac.md5 \  
https://d3ep67zochz54j.cloudfront.net/logvac/linux/amd64/logvac.md5  
  
# Install hooks  
RUN curl \  
-f \  
-k \  
https://d1ormdui8qdvue.cloudfront.net/hooks/logvac-stable.tgz \  
| tar -xz -C /opt/nanobox/hooks  
  
# Download hooks md5 (used to perform updates)  
RUN curl \  
-f \  
-k \  
-o /var/nanobox/hooks.md5 \  
https://d1ormdui8qdvue.cloudfront.net/hooks/logvac-stable.md5  
  
# Run runit automatically  
CMD [ "/opt/gonano/bin/nanoinit" ]  

