FROM jpetazzo/dind  
MAINTAINER jeroen@jeroennijhof.nl  
  
# Install ruby and kitchen  
RUN apt-get update && \  
apt-get install -y software-properties-common && \  
apt-add-repository ppa:brightbox/ruby-ng && \  
apt-get update && \  
apt-get -y install ruby2.2 ruby2.2-dev make && \  
gem install berkshelf chefspec test-kitchen kitchen-docker  
  
ENV LOG=file  
ENTRYPOINT ["wrapdocker"]  
CMD []  

