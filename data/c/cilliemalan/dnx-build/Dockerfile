FROM ubuntu  
  
MAINTAINER Cillie Malan <cilliemalan@gmail.com>  
  
# deps  
RUN sudo apt-get update -qq && sudo apt-get install -y curl && \  
curl -sL https://deb.nodesource.com/setup_4.x | sudo -E bash - && \  
sudo apt-get update -qq && \  
sudo apt-get install -y -qq unzip curl libunwind8 gettext libssl-dev
libcurl4-openssl-dev zlib1g libicu-dev uuid-dev git build-essential && \  
sudo apt-get install -y -qq nodejs && \  
sudo npm install -g npm  
  
# dnx  
RUN ["/bin/bash", "-c", "curl -sSL
https://raw.githubusercontent.com/aspnet/Home/dev/dnvminstall.sh |
DNX_BRANCH=dev sh && source ~/.dnx/dnvm/dnvm.sh && dnvm upgrade -r coreclr"]  
  
# some general npm deps  
RUN ["/bin/bash", "-c", "sudo npm install -g -y typings bower grunt-cli gulp-
cli mocha typescript node-gyp"]  
  

