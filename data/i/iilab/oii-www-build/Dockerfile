FROM fridus/docker-rvm-nvm  
MAINTAINER iilab <iilab.org>  
  
RUN apt-get update  
RUN apt-get install -y software-properties-common  
RUN add-apt-repository -y ppa:ubuntu-toolchain-r/test  
RUN apt-get update  
RUN apt-get install -y libstdc++-4.9-dev  
ENV CXX g++-4.8  
  
ENV NVM_DIR /root/.nvm  
RUN echo ". /root/.nvm/nvm.sh" >> /etc/profile  
RUN bash -lc "nvm install 4"  
RUN echo "nvm use 4" >> /etc/profile  
RUN bash -lc "npm config set user 0"  
RUN bash -lc "npm config set unsafe-perm true"  
RUN bash -lc "npm install -g pm2 http-server contentascode/broken-link-checker
docsmith sigh-cli hercule jade"  
RUN wget
"https://github.com/jgm/pandoc/releases/download/1.17.0.2/pandoc-1.17.0.2-1-amd64.deb"  
RUN dpkg -i "pandoc-1.17.0.2-1-amd64.deb"  

