FROM ubuntu:trusty  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN adduser --disabled-password --gecos "" nuser && echo "nuser ALL=(ALL)
NOPASSWD:ALL" >> /etc/sudoers  
# set HOME so 'npm install' and 'bower install' don't write to /  
ENV HOME /home/nuser  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.en  
ENV LC_ALL en_US.UTF-8  
USER nuser  
# RUN sudo locale-gen  
# Add all base dependencies  
RUN sudo apt-get update  
RUN sudo apt-get install -y language-pack-en-base  
RUN sudo apt-get install -y vim curl  
RUN sudo apt-get install -y build-essential  
RUN sudo apt-get install -y git-core  
RUN sudo apt-get install -y man  
RUN sudo apt-get install -y dnsutils  
  
# Install the latest AWS cli - needed for S3 command line actions in scripts  
RUN sudo apt-get install -y python-pip  
RUN sudo pip install awscli  
  
# Install NVM and Node  
RUN /bin/bash -l -c "curl
https://raw.githubusercontent.com/creationix/nvm/v0.17.3/install.sh | bash"  
RUN /bin/bash -l -c "echo 'source ~/.nvm/nvm.sh' >> ~/.profile"  
ENV PATH $HOME/.nvm/bin:$PATH  
RUN /bin/bash -l -c "nvm install v6.10"  
RUN /bin/bash -l -c "nvm alias default 6.10"  
# Setup the working directory  
WORKDIR /project  
  
RUN sudo chown -R nuser:nuser /project/  
  
RUN sudo apt-get autoremove -y  
  
# Expose port 2345 and set env variable  
EXPOSE 2345  
ENV PORT 2345  
  
# Add current working directory in child builds  
ONBUILD ADD ./ /project  
ONBUILD RUN sudo chown -R nuser:nuser .  
  
# Bundle child working directory  
ONBUILD RUN /bin/bash -l -c "npm install"  
# Setup the entrypoint  
ENTRYPOINT ["/bin/bash", "-l", "-c"]  

