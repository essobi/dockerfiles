############################################################  
# Dockerfile to build Ubuntu 14.04 custom container images  
# Based on Ubuntu  
############################################################  
  
# Set the base image to Ubuntu  
FROM ubuntu:14.04  
  
# File Author / Maintainer  
MAINTAINER Roger Seagle  
  
# Update the repository sources list  
RUN apt-get update  
  
# Install Git  
RUN apt-get install -y git-core  
  
# Install ruby dependencies  
RUN apt-get install -y curl libgdbm-dev libncurses5-dev automake libtool bison
libffi-dev build-essential  
  
# Configure git to not verify https  
RUN git config --global http.sslVerify false  
  
# Install rvm & ruby 2.2.2  
RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys
409B6B1796C275462A1703113804BB82D39DC0E3  
RUN cd /tmp && curl -sSL https://get.rvm.io | bash -s stable  
RUN echo 'source /usr/local/rvm/scripts/rvm' >> /etc/bash.bashrc  
RUN /bin/bash -l -c "rvm requirements"  
RUN /bin/bash -l -c "rvm install 2.2.2 --disable-binary"  
RUN /bin/bash -l -c "rvm use 2.2.2 --default"  
RUN echo "gem: --no-ri --no-rdoc" > ~/.gemrc  
RUN /bin/bash -l -c "gem install bundler"  
  
# overwrite this with 'CMD []' in a dependent Dockerfile  
CMD ["/bin/bash"]  

