FROM debian:stable-slim  
  
# Install needed tools and kubectl  
RUN apt-get update && \  
apt-get -qq install curl jq && \  
cd /usr/local/bin && \  
curl -LO https://storage.googleapis.com/kubernetes-
release/release/v1.8.6/bin/linux/amd64/kubectl && \  
chmod +x /usr/local/bin/kubectl && \  
cd -  
  
COPY create-secret.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/create-secret.sh  
CMD ["/usr/local/bin/create-secret.sh"]  

