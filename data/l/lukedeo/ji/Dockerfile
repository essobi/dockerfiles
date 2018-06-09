FROM phusion/baseimage:0.9.19  
MAINTAINER Luke de Oliveira <lukedeo@vaitech.io>  
  
# USER root  
RUN apt-get update && apt-get -y --force-yes install \  
bc \  
curl \  
git \  
wget \  
python-dev \  
python-pip \  
python-numpy \  
python-scipy \  
libx11-dev \  
libxpm-dev \  
libxft-dev \  
libxext-dev \  
libpng3 \  
libjpeg8 \  
gfortran \  
libssl-dev \  
libpcre3-dev \  
libgl1-mesa-dev \  
libglew1.5-dev \  
libftgl-dev \  
libmysqlclient-dev \  
libfftw3-dev \  
libcfitsio3-dev \  
graphviz-dev \  
libavahi-compat-libdnssd-dev \  
libldap2-dev \  
libxml2-dev && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN pip install --upgrade pip  
RUN pip install --no-cache-dir six  
RUN pip install --no-cache-dir cython scikit-image==0.10.0  
  
# all SW is installed under /opt  
WORKDIR /opt  
  
# unpack ROOT to /opt/troot  
RUN wget -O root.tgz \  
https://root.cern.ch/download/root_v6.08.00.Linux-
ubuntu16-x86_64-gcc5.4.tar.gz && \  
tar -xzf root.tgz  
  
# set up all ROOT related env vars  
ENV ROOTSYS=/opt/root  
ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$ROOTSYS/lib  
ENV DYLD_LIBRARY_PATH=$DYLD_LIBRARY_PATH:$ROOTSYS/lib  
ENV PYTHONPATH=$PYTHONPATH:$ROOTSYS/lib  
ENV PATH=$PATH:$ROOTSYS/bin  
ENV DISPLAY=""  
# install all pip-able requirements  
COPY requirements.txt /tmp/  
RUN pip install --no-cache-dir -r /tmp/requirements.txt  
  
# copy our custom rolled scripts  
COPY scripts/install-pythia.sh /tmp/  
COPY scripts/install-fastjet.sh /tmp/  
RUN chmod +x /tmp/install*  
  
ENV NUMCORES=2  
RUN /tmp/install-pythia.sh $NUMCORES  
  
ENV PYTHIA_ROOT=/opt/pythia8219  
ENV C_INCLUDE_PATH=$C_INCLUDE_PATH:$PYTHIA_ROOT/include  
ENV CPLUS_INCLUDE_PATH=$C_INCLUDE_PATH:$PYTHIA_ROOT/include  
ENV PATH=$PATH:$PYTHIA_ROOT/bin  
  
RUN /tmp/install-fastjet.sh $NUMCORES  
  
RUN mkdir /jet-generation  
COPY . /jet-generation/  
  
WORKDIR /jet-generation  
  
RUN make purge && make  
  
RUN mkdir /sim  
  
# # Install Pythia8  
# RUN wget http://home.thep.lu.se/~torbjorn/pythia8/pythia8219.tgz && \  
# tar -xzf pythia8219.tgz  
# RUN cd pythia8219 && \  
# ./configure && \  
# make && \  
# make install && \  
# cd /opt  
# # Install FastJet  
# RUN wget http://fastjet.fr/repo/fastjet-3.2.1.tar.gz && \  
# tar -xzf fastjet-3.2.1.tar.gz  
# RUN cd fastjet-3.2.1 && \  
# ./configure && \  
# make && \  
# make install && \  
# cd /opt  
# # Setup all system level  
# RUN pip install joblib  
# ADD generation /root/generation  
# WORKDIR /root/generation  
# RUN make  
# # VOLUME /data  
ENTRYPOINT ["python", "generate-events.py"]  
# ENTRYPOINT ["jet-image-maker"]  

