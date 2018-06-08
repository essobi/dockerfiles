FROM ubuntu:16.04  
RUN sed 's@/archive.ubuntu.com/@/archive.ubuntu.com.section.io/@' -i
/etc/apt/sources.list  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \  
apt-get install --assume-yes --no-install-recommends \  
redis-tools=2:3.0.6-1 \  
jq \  
wget \  
ca-certificates \  
gettext-base  
  
RUN wget https://storage.googleapis.com/kubernetes-
release/release/v1.6.0/bin/linux/amd64/kubectl -O /usr/bin/kubectl && \  
chmod +x /usr/bin/kubectl  
  
COPY sitedeployment.yml.template /sitedeployment.yml.template  
COPY entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]

