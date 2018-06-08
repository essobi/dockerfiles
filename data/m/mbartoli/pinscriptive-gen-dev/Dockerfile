#version 0.0.5  
FROM ubuntu:14.04  
MAINTAINER Mike Bartoli "michael.bartoli@pomona.edu"  
RUN apt-get update  
RUN apt-get -y install \  
python \  
build-essential \  
python-dev \  
python-pip \  
wget \  
unzip \  
git \  
perl \  
gcc \  
gfortran \  
g++ \  
curl \  
gfortran \  
libopenblas-dev \  
liblapack-dev \  
libzmq-dev \  
\--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN pip install -u \  
numpy \  
scipy \  
matplotlib \  
pandas \  
patsy \  
statsmodels \  
scikit-learn \  
ggplot \  
pyzmq \  
jinja2 \  
tornado \  
ipython  
  
EXPOSE 8888  
  
RUN mkdir /root/dev  
  
WORKDIR /root/notebooks  
  
#CMD ["/notebook.sh"]  
CMD [ "bash" ]  

