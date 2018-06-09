FROM gettyimages/spark:1.6.1-hadoop-2.6  
MAINTAINER OpenGov, Inc. <mseal@opengov.com>  
  
########################################################  
# add python environment to existing CDH5  
########################################################  
  
# Need to do all apt-get installs in one call with apt-get update or it can
get  
# our of sync. We need to do two apt-get install calls because it has an issue  
# resolving all of the dependencies.  
# ZeroMQ library 4.0.5 is installed  
ENV DEBIAN_FRONTEND='noninteractive'  
RUN apt-get update -yy -q && apt-get upgrade -yy -q  
RUN apt-get install -yy -q vim less net-tools inetutils-ping \  
curl git telnet nmap socat dnsutils netcat tree htop unzip sudo \  
software-properties-common pkg-config wget \  
build-essential python-dev liblapack-dev libatlas-dev \  
gfortran libfreetype6 libfreetype6-dev libpng12-dev python-lxml \  
libyaml-dev g++ libffi-dev libhunspell-1.3-0 libpgm-dev \  
libsodium-dev libzmq3 libzmq3-dev  
  
# Default to python 2  
ENV PYSPARK_PYTHON=python  
  
# Upgrade pip  
RUN cd /tmp && wget -q https://bootstrap.pypa.io/get-pip.py && \  
python get-pip.py 'pip==8.1.2' && rm /tmp/get-pip.py  
  
# Common python repositories. We need to install nupmy and scipy seperately
first.  
RUN pip install --upgrade numpy==1.10.4 && \  
pip install --upgrade scipy==0.17.0 && \  
pip install --upgrade \  
pandas==0.18.1 \  
scikit-learn==0.17 \  
bottleneck==1.0.0 \  
requests==2.8.1 \  
beautifulsoup4==4.4.1 \  
nltk==3.0.3 \  
pyyaml==3.11 \  
networkx==1.10 \  
boto==2.38.0 \  
pattern==2.6 \  
cyhunspell==1.1.3 \  
py4j==0.10.1  
  
# IPython / Notebook dependencies  
# Install graphing capabilities  
RUN pip install ipython==4.1.2 jsonschema==2.5.1 jupyter==1.0.0 pygments==2.1
&& \  
pip install matplotlib==1.5.1 && \  
pip install bokeh==0.11.1 seaborn==0.7.0 vincent==0.4.4  
  
# Add spark history directory  
RUN mkdir -p /var/log/spark/history  

