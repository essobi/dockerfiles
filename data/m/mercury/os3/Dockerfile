FROM ubuntu:16.04  
  
RUN apt-get -q=2 update \  
&& apt-get -q=2 -y \--no-install-recommends install \  
s3cmd \  
git \  
ruby \  
ssh \  
curl \  
bzip2 \  
gzip \  
xorriso \  
xz-utils \  
file \  
&& apt-get autoremove \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install python-gitlab  
COPY scripts/get-python-gitlab.sh /tmp/get-python-gitlab.sh  
RUN /tmp/get-python-gitlab.sh && rm /tmp/get-python-gitlab.sh  
# Install openstack client  
COPY scripts/get-openstackclient.sh /tmp/get-openstackclient.sh  
RUN /tmp/get-openstackclient.sh && rm /tmp/get-openstackclient.sh  
# Set workdir and entrypoint  
WORKDIR /tmp  
ENTRYPOINT []  

