FROM ubuntu:latest  
  
MAINTAINER kramos <markosrendell@gmail.com>  
  
# Install cloud foundry cli  
RUN apt-get update -y && \  
apt-get install -y curl && \  
curl -L
"https://cli.run.pivotal.io/stable?release=linux64-binary&source=github" | tar
xzv -C /usr/local/bin cf && \  
cf install-plugin autopilot -f -r CF-Community  
  
COPY cf_deploy.sh /usr/local/bin  
  
CMD cf -v  

