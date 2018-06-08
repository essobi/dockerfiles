FROM nice/ld-docker-app  
MAINTAINER Charlotte Gore <conspiracygore@gmail.com>  
  
RUN \  
apt-get -q -y install npm &&\  
npm install -g grunt-cli &&\  
apt-get install -q -y git raptor-utils graphviz && \  
mozroots --import --sync && \  
cd /tools && \  
./install.sh && \  
cd -  
  
ENV PROJECT_DIR="/tmp"  
ENV MIMIR_PORT=80  
EXPOSE 80  
CMD ["/bin/bash","/src/owldin/install.sh"]  

