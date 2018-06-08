FROM ubuntu:16.04  
MAINTAINER Datica <admin@datica.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV LC_ALL C  
  
RUN apt-get update && \  
apt-get install -y \  
wget \  
curl \  
git \  
lsb-core \  
unzip \  
iptables-persistent \  
apt-transport-https \  
ca-certificates \  
software-properties-common && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN curl -fsSL
https://repo.saltstack.com/apt/ubuntu/16.04/amd64/2018.3/SALTSTACK-GPG-KEY.pub
| apt-key add -  
RUN echo "deb http://repo.saltstack.com/apt/ubuntu/16.04/amd64/2018.3 xenial
main" > /etc/apt/sources.list.d/salt.list  
  
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -  
RUN echo "deb [arch=amd64] https://download.docker.com/linux/ubuntu
$(lsb_release -cs) stable" > /etc/apt/sources.list.d/docker.list  
  
RUN apt-get update && \  
apt-get install -y \  
salt-minion \  
python-pip \  
python-dev \  
python-m2crypto \  
docker-ce=17.12.1~ce-0~ubuntu && \  
pip install boto boto3 docker awscli && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# COPY ./state.py /usr/lib/python2.7/dist-packages/salt/modules/  
RUN git clone \--recursive https://github.com/kubernetes-client/python.git  
RUN pip install pyasn1==0.4.1  
RUN cd python && python setup.py install  
RUN wget
https://releases.hashicorp.com/terraform/0.11.7/terraform_0.11.7_linux_amd64.zip
&& unzip terraform_0.11.7_linux_amd64.zip && \  
mv terraform /usr/local/sbin/  
  
ENV PATH="/opt:${PATH}"  
CMD ["/usr/bin/salt-minion", "-l", "info"]  

