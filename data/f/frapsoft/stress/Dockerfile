FROM debian:jessie-slim  
  
MAINTAINER Maik Ellerbrock (https://github.com/ellerbrock)  
  
USER root  
  
RUN apt-get update && \  
apt-get install --no-install-recommends stress -y && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENTRYPOINT ["stress"]  
  
CMD ["--version"]  

