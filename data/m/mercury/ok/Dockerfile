FROM ruby:2.4.0  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
python \  
python-dev \  
python-pip \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install OpenStack client (pip version is much more up-to-date than that
install via apt)  
RUN pip install python-openstackclient  
  
# Install test kitchen  
RUN gem install test-kitchen kitchen-openstack  
  
# Set workdir and entrypoint  
WORKDIR /tmp  
ENTRYPOINT []  

