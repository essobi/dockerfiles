# taos  
FROM python:3.6.2  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install Go prerequisite, ansible, openstack, and s3 packages  
RUN apt-get update \  
&& apt-get install -y \--no-install-recommends \  
bash \  
git \  
graphviz \  
openssh-client \  
s3cmd \  
libssl-dev \  
libffi-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install ansible  
COPY scripts/get-ansible.sh /tmp/get-ansible.sh  
RUN /tmp/get-ansible.sh && rm /tmp/get-ansible.sh  
# Install go  
COPY scripts/get-go.sh /tmp/get-go.sh  
RUN /tmp/get-go.sh && rm /tmp/get-go.sh  
# Setup go environment  
ENV PATH /usr/local/go/bin:$PATH  
  
# Install terraform  
COPY scripts/get-terraform.sh /tmp/get-terraform.sh  
RUN /tmp/get-terraform.sh && rm /tmp/get-terraform.sh  
# Set workdir and entrypoint  
WORKDIR /tmp  
ENTRYPOINT []  

