FROM nanobox/runit  
  
# Create directories  
RUN mkdir -p \  
/var/log/gonano \  
/var/nanobox \  
/opt/nanobox/hooks  
  
# Install nfs client  
RUN apt-get update -qq && \  
apt-get install -y nfs-common cron && \  
apt-get clean all && \  
rm -rf /var/lib/apt/lists/*  
  
# remove pkgsrc base bootstrap to save space  
# since it's replaced by the build and not used  
RUN rm -rf /data && \  
mkdir -p /data  
  
# Install hooks  
RUN curl \  
-f \  
-k \  
https://d1ormdui8qdvue.cloudfront.net/hooks/code-stable.tgz \  
| tar -xz -C /opt/nanobox/hooks  
  
# Download hooks md5 (used to perform updates)  
RUN curl \  
-f \  
-k \  
-o /var/nanobox/hooks.md5 \  
https://d1ormdui8qdvue.cloudfront.net/hooks/code-stable.md5  
  
# Run runit automatically  
CMD [ "/opt/gonano/bin/nanoinit" ]  

