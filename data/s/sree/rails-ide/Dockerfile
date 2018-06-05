FROM sree/dev-ide:latest  
  
MAINTAINER Sree <sree@aletilabs.com>  
  
ENV RAILS_PACKAGES ruby-libs mysql-dev mysql-client sqlite-dev ruby-io-console
libffi-dev \  
tzdata ruby-json ruby-bigdecimal ruby-irb libxml2-dev  
  
  
RUN sudo apk add --update $RAILS_PACKAGES && \  
sudo rm -rf /var/cache/* /var/log/* /var/tmp/* && \  
sudo mkdir /var/cache/apk && \  
sudo gem install -N bundler rails && \  
sudo npm install -g create-react-app  
  
#start container with bash  
ENTRYPOINT ["bash"]  

