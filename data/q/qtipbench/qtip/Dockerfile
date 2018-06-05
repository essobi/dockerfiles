##########################################  
#####Docker container for QTIP############  
##########################################  
  
FROM ubuntu:16.04  
MAINTAINER Yujun Zhang <zhang.yujunz@zte.com.cn>  
LABEL version="0.1" description="OPNFV QTIP Docker container"  
  
ARG BRANCH=master  
  
ENV REPOS_DIR=/home/opnfv/repos \  
PYTHONPATH=/home/opnfv/repos/qtip \  
USER=root  
  
WORKDIR /home/opnfv  
  
RUN mkdir -p ${REPOS_DIR} \  
&& mkdir -p /root/qtip/logs \  
&& mkdir -p /root/.ssh \  
&& chmod 700 /root/.ssh  
  
# Packaged Dependencies  
RUN apt-get update && apt-get install -y \  
software-properties-common \  
git \  
gcc \  
build-essential\  
libssl-dev\  
libffi-dev\  
locales \  
supervisor \  
python-dev \  
python-pip \  
python-setuptools \  
rsync \  
iputils-ping \  
wget \  
curl \  
openssh-client \  
\--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN locale-gen en_US en_US.UTF-8 \  
&& pip install -U pip \  
&& pip install -U setuptools  
  
#Cloning Repos  
RUN git config --global http.sslVerify false \  
&& git clone -b $BRANCH https://gerrit.opnfv.org/gerrit/qtip $REPOS_DIR/qtip \  
&& cd $REPOS_DIR/qtip \  
&& pip install pipenv \  
&& pipenv install --system  
  
RUN echo 'eval $(ssh-agent)' >> /root/.bashrc  
  
# Exposing ports  
EXPOSE 5000  
  
#Config supervisor  
RUN mkdir -p /var/log/supervisor  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
CMD ["/usr/bin/supervisord"]

