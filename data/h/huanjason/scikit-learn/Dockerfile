FROM ubuntu  
COPY sources.list /etc/apt/  
RUN \  
apt-get update \  
&& apt-get install -y \  
build-essential \  
libatlas-dev \  
libatlas3-base \  
python \  
python-dev \  
python-setuptools \  
python-pip \  
python-numpy \  
python-matplotlib \  
python-scipy \  
python-pandas \  
ipython \  
python3 \  
python3-dev \  
python3-setuptools \  
python3-pip \  
python3-numpy \  
python3-matplotlib \  
python3-scipy \  
python3-pandas \  
ipython3 \  
&& update-alternatives --set libblas.so.3 /usr/lib/atlas-
base/atlas/libblas.so.3 \  
&& update-alternatives --set liblapack.so.3 /usr/lib/atlas-
base/atlas/liblapack.so.3 \  
&& pip install -U scikit-learn \  
&& pip3 install -U scikit-learn \  
&& /usr/bin/python -c "import matplotlib.pyplot" \  
&& /usr/bin/python3 -c "import matplotlib.pyplot"  
  
ENTRYPOINT [ "/usr/bin/ipython"]  

