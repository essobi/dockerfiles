#  
# Conjur-Cli Dockerfile  
#  
# https://github.com/deny4ll/deny4ll-docker-conjur-cli  
#  
#  
# Pull base image.  
FROM ubuntu:latest  
  
  
# Install Ruby.  
RUN \  
apt-get update  
  
RUN \  
apt-get install -y ruby ruby-dev ruby-bundler zsh vim wget curl  
  
RUN \  
apt-get clean all  
  
RUN \  
wget https://github.com/cyberark/conjur-
cli/releases/download/v5.4.0/conjur_5.4.0-1_amd64.deb && \  
dpkg -i conjur_5.4.0-1_amd64.deb  
  
RUN rm conjur_5.4.0-1_amd64.deb  
  
RUN apt-get update && apt-get install openssh-client -y  
  
# Define default command.  
CMD ["/bin/bash"]  

