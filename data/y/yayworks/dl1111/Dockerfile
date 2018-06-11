  
FROM nimbix/base-ubuntu-nvidia:8.0-cudnn5-devel  
MAINTAINER Nimbix, Inc. <support@nimbix.net>  
  
RUN apt-get update && apt-get install -y \  
build-essential \  
curl \  
wget \  
libibverbs-dev \  
libibverbs1 \  
librdmacm1 \  
librdmacm-dev \  
rdmacm-utils \  
libibmad-dev \  
libibmad5 \  
byacc \  
libibumad-dev \  
libibumad3 \  
flex && \  
apt-get install -y python3.4 && \  
apt-get install -y python3-pip && \  
apt-get install -y nodejs-legacy && \  
apt-get install -y npm && \  
## npm install -g configurable-http-proxy && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
##RUN pip3 install virtualenv && \  
## pip3 install jupyterhub && \  
## pip3 install --upgrade zmq && \  
## pip3 install --upgrade notebook  
ENV MPI_VERSION 2.0.1  
ADD ./install-ompi.sh /tmp/install-ompi.sh  
RUN /bin/bash -x /tmp/install-ompi.sh && \  
rm -rf /tmp/install-ompi.sh  
  
ENV OSU_VERSION 5.3.2  
ADD ./install-osu.sh /tmp/install-osu.sh  
RUN /bin/bash -x /tmp/install-osu.sh && rm -rf /tmp/install-osu.sh  
  
ADD ./yb-sw-config.NIMBIX.x8664.turbotensor.sh /tmp/yb-sw-
config.NIMBIX.x8664.turbotensor.sh  
RUN /bin/bash -x /tmp/yb-sw-config.NIMBIX.x8664.turbotensor.sh  
  
ADD ./jupyterhub_config.py /usr/local  
ADD ./wetty.tar.gz /usr/local  
ADD ./config.sh /usr/local/config.sh  
ADD ./start.sh /usr/local/start.sh  
ADD ./setup.x /usr/local/setup.x  
ADD ./jpy_lab_start.sh /usr/local/jpy_lab_start.sh  
RUN chmod +x /usr/local/config.sh && chown nimbix.nimbix /usr/local/config.sh
&& \  
chmod +x /usr/local/start.sh && chown nimbix.nimbix /usr/local/start.sh && \  
chmod +x /usr/local/setup.x && chown nimbix.nimbix /usr/local/setup.x && \  
chmod +x /usr/local/jpy_lab_start.sh && \  
  
wget -O- -q http://s3tools.org/repo/deb-all/stable/s3tools.key | sudo apt-key
add \- && \  
sudo wget -O/etc/apt/sources.list.d/s3tools.list http://s3tools.org/repo/deb-
all/stable/s3tools.list && \  
sudo apt-get update && \  
sudo apt-get install s3cmd && \  
sudo apt-get install -y gfortran && \  
sudo apt-get update && \  
sudo apt-get install -y python-qt4 && \  
  
/usr/local/anaconda3/envs/tensorflow/bin/pip install --upgrade pip && \  
/usr/local/anaconda3/envs/tensorflow/bin/pip install
git+git://github.com/Hvass-Labs/scikit-
optimize.git@dd7433da068b5a2509ef4ea4e5195458393e6555 && \  
  
echo "Y" | /usr/local/anaconda3/envs/tensorflow/bin/conda install tensorflow-
gpu && \  
echo "Y" | /usr/local/anaconda3/envs/tensorflow/bin/conda install pytorch  
  
  
RUN echo 'export
PATH=/usr/local/cuda/bin:/usr/local/anaconda3/envs/tensorflow/bin:$PATH' >>
/home/nimbix/.bashrc \  
&& echo 'export
PYTHONPATH=/usr/local/anaconda3/envs/tensorflow/lib/python3.6:/usr/local/anaconda3/envs/tensorflow/lib/python3.6/site-
packages/:/usr/local/anaconda3/envs/tensorflow/lib/python3.6/site-
packages/prettytensor-0.7.2-py3.6.egg:/usr/local/anaconda3/envs/tensorflow/lib/python3.6/site-
packages/enum34-1.1.6-py3.6.egg:/usr/local/anaconda3/envs/tensorflow/lib/python3.6/site-
packages/matplotlib:$PYTHONPATH' >> /home/nimbix/.bashrc \  
&& echo 'export
PATH=/usr/local/cuda/bin:/usr/local/anaconda3/envs/tensorflow/bin:$PATH' >>
/etc/skel/.bashrc \  
&& echo 'export
PYTHONPATH=/usr/local/anaconda3/envs/tensorflow/lib/python3.6:/usr/local/anaconda3/envs/tensorflow/lib/python3.6/site-
packages/:/usr/local/anaconda3/envs/tensorflow/lib/python3.6/site-
packages/prettytensor-0.7.2-py3.6.egg:/usr/local/anaconda3/envs/tensorflow/lib/python3.6/site-
packages/enum34-1.1.6-py3.6.egg:/usr/local/anaconda3/envs/tensorflow/lib/python3.6/site-
packages/matplotlib:$PYTHONPATH' >> /etc/skel/.bashrc  
  
WORKDIR /home/nimbix  
RUN /usr/bin/wget https://s3.amazonaws.com/yb-lab-cfg/admin/yb-
admin.NIMBIX.x86_64.tar \  
&& tar xvf yb-admin.NIMBIX.x86_64.tar -C /usr/bin \  
&& sudo apt-get install -y tcl \  
&& sudo apt-get install -y git \  
&& sudo apt-get install -y awscli  
  
EXPOSE 8888  
ADD ./NAE/help.html /etc/NAE/help.html  

