FROM ubuntu:16.04  
# Ubuntu Setup  
RUN apt-get update -y  
# RUN apt-get upgrade -y  
WORKDIR /app  
  
# HTTPS  
RUN apt-get install apt-transport-https -y  
RUN echo 'deb http://private-
repo-1.hortonworks.com/HDP/ubuntu14/2.x/updates/2.4.2.0 HDP main' >>
/etc/apt/sources.list.d/HDP.list  
RUN echo 'deb http://private-repo-1.hortonworks.com/HDP-
UTILS-1.1.0.20/repos/ubuntu14 HDP-UTILS main' >>
/etc/apt/sources.list.d/HDP.list  
RUN echo 'deb [arch=amd64] https://apt-mo.trafficmanager.net/repos/azurecore/
trusty main' >> /etc/apt/sources.list.d/azure-public-trusty.list  
  
# Install all required libraries  
RUN apt-get install build-essential libssl-dev curl imagemagick -y  
  
# Install nvm and use correct node version  
ENV NVM_DIR /usr/local/nvm  
RUN /bin/bash -c "curl -sL
https://raw.githubusercontent.com/creationix/nvm/v0.33.8/install.sh | bash \  
&& source $NVM_DIR/nvm.sh \  
&& nvm install 7.8.0 \  
&& nvm use 7.8.0"  
  
# Install sphinx  
RUN apt-get install libmysqlclient20 libodbc1 libpq5 wget -y  
RUN apt-get install sphinxsearch -y  
  
# Install Ruby  
RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys
409B6B1796C275462A1703113804BB82D39DC0E3  
RUN curl -sSL https://get.rvm.io | bash -s stable  
RUN /bin/bash -c "source /etc/profile.d/rvm.sh \  
&& rvm install 2.3.4 \  
&& rvm rubygems current \  
&& rvm use 2.3.4"  
  
# Get ShareTribe  
RUN apt-get install git-core -y  
RUN git clone git://github.com/sharetribe/sharetribe.git ~/sharetribe  
  
# Install gem  
RUN apt-get install libxslt-dev libxml2-dev libmysqlclient-dev -y  
  
RUN /bin/bash -c "source /etc/profile.d/rvm.sh \  
&& gem install bundler mailcatcher \  
&& cd ~/sharetribe \  
&& bundle install"  
  
RUN /bin/bash -c "source $NVM_DIR/nvm.sh \  
&& cd ~/sharetribe \  
&& npm install"  
  
# Get ShareTribe  
RUN apt-get install git-core -y  
RUN git clone git://github.com/sharetribe/sharetribe.git /app/sharetribe  
  
RUN /bin/bash -c "source /etc/profile.d/rvm.sh \  
&& gem install bundler mailcatcher \  
&& cd /app/sharetribe \  
&& bundle install"  

