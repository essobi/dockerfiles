FROM ubuntu:14.04  
ENV REFRESHED_AT 2014-11-06  
# Base install  
RUN apt-get update -y  
RUN apt-get install -y vim git-core build-essential g++ libssl-dev curl wget
apache2-utils libxml2-dev  
  
# Install NVM  
RUN git clone https://github.com/creationix/nvm.git /.nvm  
RUN echo ". /.nvm/nvm.sh" >> /etc/bash.bashrc  
  
ENV NODEVERSION 0.10  
RUN /bin/bash -c '. /.nvm/nvm.sh && nvm install $NODEVERSION'  
  
VOLUME /project  
  
CMD /bin/bash -c '. /.nvm/nvm.sh && cd /project && nvm use $NODEVERSION && npm
install && `npm bin`/bower --allow-root -F install && env PREFIX=./dist `npm
bin`/grunt build && tar -czvf app.tar.gz -C dist .'  

