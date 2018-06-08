# -*- mode: Dockerfile; tab-width: 4;indent-tabs-mode: nil;-*-  
# vim: ts=4 sw=4 ft=Dockerfile et: 1  
FROM nanobox/runit  
  
# Create directories  
RUN mkdir -p /var/log/gonano  
  
# Install ipvsadm  
RUN apt-get update -qq && \  
apt-get install -y ipvsadm && \  
apt-get clean all  
  
# Download portal  
RUN curl \  
-f \  
-k \  
-o /usr/local/bin/portal \  
https://s3.amazonaws.com/tools.nanopack.io/portal/linux/amd64/portal && \  
chmod 755 /usr/local/bin/portal  
  
# Download md5 (used to perform updates in hooks)  
RUN mkdir -p /var/nanobox && \  
curl \  
-f \  
-k \  
-o /var/nanobox/portal.md5 \  
https://s3.amazonaws.com/tools.nanopack.io/portal/linux/amd64/portal.md5  
  
# Install hooks  
RUN mkdir -p /opt/nanobox/hooks && \  
curl \  
-f \  
-k \  
https://s3.amazonaws.com/tools.nanobox.io/hooks/portal-stable.tgz \  
| tar -xz -C /opt/nanobox/hooks  
  
# Cleanup disk  
RUN rm -rf \  
/var/lib/apt/lists/* \  
/tmp/* \  
/var/tmp/*  
  
# Run runit automatically  
CMD /opt/gonano/bin/nanoinit  

