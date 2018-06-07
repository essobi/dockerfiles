FROM ubuntu:latest  
MAINTAINER Gum-Joe "kishansambhi@hotmail.co.uk"  
ENV JAKHU_WORKER_VERSION 1.0.0  
ENV JAKHU_WORKER_NAME jakhu-docker-ubuntu-base-image  
# Replace shell  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
# Base image  
# First step: Set up user  
RUN adduser --disabled-password --gecos '' jakhu  
# Add to groups  
RUN adduser jakhu sudo  
# Allow sudo  
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers  
USER jakhu  
# Using user jakhu  
# Install apt packages  
# curl  
RUN sudo apt-get install -y curl  
# git  
RUN sudo apt-get install -y git-core  
# gnupg  
RUN sudo apt-get install -y gnupg  
# Source & run  
# Versions  
ENV NODE_VERSION stable  
ENV RUBY_VERSION ruby-head  
ENV VENV /home/jakhu/.virtualenv  
# Install nvm with node and npm  
RUN curl https://raw.githubusercontent.com/creationix/nvm/v0.30.1/install.sh |
bash \  
&& source ~/.nvm/nvm.sh \  
&& nvm install $NODE_VERSION \  
&& nvm alias default $NODE_VERSION \  
&& nvm use default \  
&& echo "source ~/.nvm/nvm.sh && nvm use default" >> ~/.bashrc  
# packages  
RUN source /home/jakhu/.nvm/nvm.sh && nvm use default && npm install -g \  
less \  
coffee-script \  
node-gyp  
# When using nodejs CMD:  
# CMD source ~/.nvm/nvm.sh && nvm use default && node --version  
# Ruby with bundle + gem  
RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys D39DC0E3  
RUN /bin/bash -l -c "curl -sSL https://get.rvm.io | bash -s stable"  
RUN /bin/bash -l -c "rvm use $RUBY_VERSION \--install --binary --fuzzy"  
RUN /bin/bash -l -c "echo 'gem: --no-ri --no-rdoc' > ~/.gemrc"  
RUN /bin/bash -l -c "source ~/.rvm/scripts/rvm && rvm use $RUBY_VERSION && gem
install bundler sass --no-ri --no-rdoc"  
RUN /bin/bash -l -c "echo 'rvm use $RUBY_VERSION' >> /home/jakhu/.bashrc"  
# Python  
RUN sudo apt-get install -y python  
# Pip  
RUN curl --silent https://bootstrap.pypa.io/get-pip.py | sudo python -  
# virtual env  
RUN sudo pip install virtualenv  
RUN mkdir $VENV  
RUN virtualenv ~/.virtualenv  
RUN source ~/.virtualenv/bin/activate  
RUN echo "source ~/.virtualenv/bin/activate" >> ~/.bashrc  
  
# Image info  
ENV JAKHU_OS_IMAGE ubuntu  
ENV JAKHU_OS_IMAGE_TAG latest  
ENV JAKHU_DOCKER_IMAGE base  
# Pull images list  
RUN sudo git clone https://github.com/Gum-Joe/jakhu-images /jakhuImages  
RUN sudo chown -R jakhu /jakhuImages  
VOLUME /jakhuImages  
# Create version  
RUN sudo mkdir /metadata  
RUN sudo chown -R jakhu /metadata  
COPY . /jakhutools  
RUN /bin/bash -l -c "source ~/.rvm/scripts/rvm && rvm use $RUBY_VERSION &&
ruby /jakhutools/versions.rb"  
RUN chmod 700 /metadata/version.sh  
RUN chmod 777 /metadata/version.sh  
RUN sudo chmod 700 /jakhutools/info.sh  
RUN sudo chmod 777 /jakhutools/info.sh  
VOLUME /jakhutools  
# Get runner  
RUN sudo git clone https://github.com/Gum-Joe/jakhu-runner /runner  
RUN sudo chown -R jakhu /runner  
VOLUME /runner  
CMD /jakhutools/info.sh  

