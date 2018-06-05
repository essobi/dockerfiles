FROM ruby:2.3.3  
MAINTAINER Justin Campbell <justin@justincampbell.me>  
  
# Bundler  
RUN gem install bundler --no-document  
  
# bundle-cache  
RUN gem install bundle_cache --no-document  
  
# Node.js  
RUN curl --silent --location https://deb.nodesource.com/setup_6.x | bash -  
RUN apt-get install -y nodejs  
  
# Bower  
RUN npm install -g bower  
RUN echo '{ "allow_root": true }' > /root/.bowerrc  
  
# Yarn  
RUN npm install -g yarn  
  
# Ember CLI  
RUN npm install -g ember-cli  
  
# aws-cli  
RUN \  
curl --location https://s3.amazonaws.com/aws-cli/awscli-bundle.zip -o awscli-
bundle.zip && \  
apt-get install -y python-dev unzip && \  
unzip awscli-bundle.zip && \  
./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws && \  
apt-get remove -y python-dev unzip && \  
rm -rf awscli-bundle*  

