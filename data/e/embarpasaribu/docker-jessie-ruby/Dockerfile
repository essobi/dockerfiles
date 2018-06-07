FROM embarpasaribu/docker-jessie:8.6  
MAINTAINER Embar Pasaribu <embar@pasaribu.web.id>  
  
ARG RUBY_VERSION=2.3.1  
RUN gpg --keyserver pgp.mit.edu --recv-keys
409B6B1796C275462A1703113804BB82D39DC0E3 && \  
\curl -sSL https://get.rvm.io | bash -s stable && \  
/bin/bash -l -c "rvm requirements" && \  
/bin/bash -l -c "rvm install $RUBY_VERSION" && \  
/bin/bash -l -c "rvm use $RUBY_VERSION"  

