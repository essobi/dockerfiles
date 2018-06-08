FROM thehunt33r/ansible-on-debian:latest  
  
RUN apt-get update && apt-get install -y \  
build-essential \  
ruby \  
ruby-dev \  
rake \  
gem  
  
RUN gem install serverspec  
  
CMD ["/sbin/init"]  
  

