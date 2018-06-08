# -*- mode: Dockerfile; tab-width: 4;indent-tabs-mode: nil;-*-  
# vim: ts=4 sw=4 ft=Dockerfile et: 1  
FROM nanobox/runit  
  
# Create directories  
RUN mkdir -p /var/log/gonano  
  
# Install arping  
RUN apt-get update -qq && \  
apt-get install -y iputils-arping && \  
apt-get clean all && \  
rm -rf /var/lib/apt/lists/*  
  
# Install binaries  
RUN rm -rf /data/var/db/pkgin && \  
/data/bin/pkgin -y up && \  
/data/bin/pkgin -y in \  
luvit-0.10.0 \  
flip \  
flip-scripts \  
mongodb-server-3.0 \  
mongodb30-tools-3.0 && \  
rm -rf /data/var/db/pkgin/cache  
  
RUN rm -rf /var/gonano/db/pkgin && \  
/opt/gonano/bin/pkgin -y up && \  
/opt/gonano/bin/pkgin -y in \  
rsync && \  
rm -rf /var/gonano/db/pkgin/cache  
  
# Install hooks  
RUN mkdir -p /opt/nanobox/hooks && \  
mkdir -p /var/nanobox && \  
curl \  
-f \  
-k \  
https://d1ormdui8qdvue.cloudfront.net/hooks/mongodb-stable.tgz \  
| tar -xz -C /opt/nanobox/hooks && \  
curl \  
-f \  
-k \  
-o /var/nanobox/hooks.md5 \  
https://d1ormdui8qdvue.cloudfront.net/hooks/mongodb-stable.md5  
  
# Cleanup disk  
RUN rm -rf \  
/var/lib/apt/lists/* \  
/tmp/* \  
/var/tmp/*  
  
# Run runit automatically  
CMD [ "/opt/gonano/bin/nanoinit" ]  

