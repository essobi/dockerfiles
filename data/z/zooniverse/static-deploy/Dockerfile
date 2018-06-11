FROM ubuntu:14.04  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get install -y curl && \  
curl https://deb.nodesource.com/setup | bash - && \  
apt-get install -y nodejs git ruby libjpeg-progs optipng jekyll && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
ADD deploy.sh /  
  
ENTRYPOINT [ "/deploy.sh" ]  

