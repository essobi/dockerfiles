FROM ubuntu:14.04  
USER root  
RUN locale-gen en_US.UTF-8  
RUN dpkg-reconfigure locales  
ENV LC_ALL en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
RUN apt-get -y update && apt-get install -y swig libzmq3-dev libgmp-dev
libglpk-dev glpk-utils \  
pandoc python-dev python-pip libxml2 libxml2-dev zlib1g zlib1g-dev bzip2
libbz2-dev libxslt1-dev openbabel \  
build-essential wget curl  
  
COPY requirements.txt requirements.txt  
  
# Install conda  
ADD miniconda.sh miniconda.sh  
RUN bash miniconda.sh -b -p /opt/conda  
ENV PATH "/opt/conda/bin:$PATH"  
RUN hash -r  
RUN conda config \--set always_yes yes \--set changeps1 no  
RUN conda update -q conda  
RUN conda install -y scipy numpy pandas numexpr matplotlib SIP  
  
# For Python 3.5 (default)  
RUN pip install pip --upgrade  
RUN pip install -r requirements.txt  
  
# For Python 3.4  
RUN conda create -y -n python3.4 python=3.4 scipy numpy pandas numexpr
matplotlib SIP  
RUN /opt/conda/envs/python3.4/bin/pip install pip --upgrade  
RUN /opt/conda/envs/python3.4/bin/pip install -r requirements.txt  
  
# For Python 2.7  
RUN conda create -y -n python2 python=2.7 scipy numpy pandas numexpr
matplotlib SIP  
RUN /opt/conda/envs/python2/bin/pip install pip --upgrade  
RUN /opt/conda/envs/python2/bin/pip install -r requirements.txt  

