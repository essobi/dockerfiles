#Pull base image from Docker hub  
FROM ubuntu:14.04  
MAINTAINER Eric Irwin <eirwin@integrate.com>  
  
RUN sudo apt-get update  
RUN sudo apt-get install -y npm  
  
# Set in what directory commands will run  
WORKDIR /home/app  
  
# Put all our code inside that directory that lives in the container  
ADD . /home/app  
  
RUN sudo npm install && \  
sudo npm install -g grunt-cli  
  
#Need to do this for npm and bower  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
  
# Install dependencies  
RUN sudo npm install -g bower && \  
sudo npm install -g grunt-cli && \  
sudo npm install && \  
bower install --config.interactive=false \--allow-root  
  
EXPOSE 9000  
# The command to run our app when the container is run  
ENTRYPOINT ["npm","start"]  

