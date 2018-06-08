# pao  
FROM python:3.6.2  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install Go/Packer prerequisite and openstack packages  
RUN apt-get update \  
&& apt-get install -y \--no-install-recommends \  
apt-utils \  
software-properties-common \  
&& apt-get install -y \--no-install-recommends \  
bash \  
build-essential \  
curl \  
g++ \  
gcc \  
git \  
libc6-dev \  
libffi-dev \  
libssl-dev \  
make \  
openssh-client \  
pkg-config \  
python3-pip \  
qemu \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install go  
COPY scripts/get-go.sh /tmp/get-go.sh  
RUN /tmp/get-go.sh && rm /tmp/get-go.sh  
# Setup go environment  
ENV PATH /usr/local/go/bin:$PATH  
  
# Install packer  
COPY scripts/get-packer.sh /tmp/get-packer.sh  
RUN /tmp/get-packer.sh && rm /tmp/get-packer.sh  
# Install ansible  
COPY scripts/get-ansible.sh /tmp/get-ansible.sh  
RUN /tmp/get-ansible.sh && rm /tmp/get-ansible.sh  
# Install openstack client (PyPi version is much more up-to-date than that
install via apt!)  
RUN pip3 install python-openstackclient==3.9.0  
  
# Install glance-proxy  
COPY scripts/get-glance-proxy.sh /tmp/get-glance-proxy.sh  
RUN /tmp/get-glance-proxy.sh && rm /tmp/get-glance-proxy.sh  
# Set workdir and entrypoint  
WORKDIR /tmp  
ENTRYPOINT []  
  

