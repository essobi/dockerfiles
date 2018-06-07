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
  
# Download hoarder  
RUN curl \  
-f \  
-k \  
-o /usr/local/bin/hoarder \  
https://d3ep67zochz54j.cloudfront.net/hoarder/linux/amd64/hoarder && \  
chmod 755 /usr/local/bin/hoarder  
  
# Download md5 (used to perform updates in hooks)  
RUN curl \  
-f \  
-k \  
-o /var/nanobox/hoarder.md5 \  
https://d3ep67zochz54j.cloudfront.net/hoarder/linux/amd64/hoarder.md5  
  
# Download slurp  
RUN curl \  
-f \  
-k \  
-o /usr/local/bin/slurp \  
https://d3ep67zochz54j.cloudfront.net/slurp/linux/amd64/slurp && \  
chmod 755 /usr/local/bin/slurp  
  
# Download md5 (used to perform updates in hooks)  
RUN curl \  
-f \  
-k \  
-o /var/nanobox/slurp.md5 \  
https://d3ep67zochz54j.cloudfront.net/slurp/linux/amd64/slurp.md5  
  
# Install hooks  
RUN curl \  
-f \  
-k \  
https://d1ormdui8qdvue.cloudfront.net/hooks/hoarder-stable.tgz \  
| tar -xz -C /opt/nanobox/hooks  
  
# Download hooks md5 (used to perform updates)  
RUN curl \  
-f \  
-k \  
-o /var/nanobox/hooks.md5 \  
https://d1ormdui8qdvue.cloudfront.net/hooks/hoarder-stable.md5  
  
# Run runit automatically  
CMD [ "/opt/gonano/bin/nanoinit" ]  

