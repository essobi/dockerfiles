FROM ubuntu:14.04  
# Install necessary packages  
RUN apt-get update && apt-get -y install software-properties-common ruby1.9.3
haproxy patch make zlib1g-dev  
  
# Install Smartstack (Synapse + Nerve)  
RUN gem install amq-protocol -v 1.9.2 # Latest compatible with Ruby 1.9.3  
RUN gem install synapse -v 0.12.1 --conservative  
RUN gem install nerve -v 0.6.0 --conservative  
  
# Enable HAProxy  
RUN echo "ENABLED=1" > /etc/default/haproxy  
  
# Add startup scripts  
ADD *.sh /opt/

