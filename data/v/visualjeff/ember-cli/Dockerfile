# Docker version 1.8.2  
#  
# To build: sudo docker build --force-rm=true -t visualjeff/ember-cli:1.13.12
.  
# To tag: sudo docker tag CONTAINERID visualjeff/ember-cli:latest  
# To run: sudo docker run -t -i -p 4200:4200 -p 35729:35729 visualjeff/ember-
cli:latest /bin/bash  
FROM debian:latest  
  
# Update and install basics  
RUN apt-get update && apt-get install -y git curl nano vim tmux tar bzip2  
  
# Install Node.js  
RUN curl -sL https://deb.nodesource.com/setup | bash -  
RUN apt-get install -y nodejs  
  
# Install NVM  
RUN git clone https://github.com/creationix/nvm.git /.nvm  
RUN echo ". /.nvm/nvm.sh" >> /etc/bash.bashrc  
RUN /bin/bash -c '. /.nvm/nvm.sh && \  
nvm install v4.2.2 && \  
nvm use v4.2.2 && \  
nvm alias default v4.2.2'  
  
#Install ember-cli  
RUN npm install -g ember-cli@1.13.12 bower phantomjs  
  
ADD setupVim.sh /root/setupVim.sh  
RUN chmod +x /root/setupVim.sh  
  
#Clean-up  
RUN apt-get clean && rm -rf /var/lib/apt/lists/*  
  
#Expose ports  
EXPOSE 4200 35729  
# Define default command.  
WORKDIR /root  
CMD ["bash"]  

