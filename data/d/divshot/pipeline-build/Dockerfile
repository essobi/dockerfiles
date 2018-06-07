FROM node:0.10  
RUN apt-get -y update && \  
apt-get -y install sudo build-essential ruby ruby-dev  
  
RUN adduser --disabled-password --gecos '' build && \  
adduser build sudo && \  
echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers && \  
mkdir -p /home/build  
  
USER build  
ENV HOME /home/build  
  
RUN npm config set prefix ~/npm &&\  
npm install -g bower jspm component browserify grunt-cli gulp broccoli-cli
ember-cli harp divshot-cli &&\  
gem install --user-install bundler middleman jekyll  
ENV PATH /home/build/npm/bin:$PATH  
  
ADD ./scripts /home/build/scripts  
  
USER root  
WORKDIR /home/build/src  
CMD ["/home/build/scripts/run"]

