# Pull base image.  
FROM ubuntu:14.04  
MAINTAINER Patrice Rey  
  
RUN apt-get update -y  
RUN apt-get upgrade -y  
  
RUN apt-get install -y git python-pip python-dev libzmq3 libzmq3-dev pkg-
config libfreetype6-dev libpng3  
  
RUN apt-get install -y gcc-multilib lib32gcc-4.8-dev zip unzip  
RUN apt-get install imagemagick -y  
RUN pip install -U setuptools  
RUN pip install -U pip # fixes AssertionError in Ubuntu pip  
RUN pip install enum34  
RUN pip install Pillow  
RUN pip install six==1.10.0  
RUN pip install jupyter markupsafe zmq singledispatch backports_abc certifi
jsonschema path.py matplotlib  
RUN pip install Cython==0.20  
RUN pip install scipy  
RUN pip install numpy  
RUN python -m pip install -U matplotlib  
  
RUN mkdir /workspace && \  
mkdir /workspace/volume  
  
# launch notebook  
WORKDIR /build  
RUN git clone https://github.com/tristan-salles/GEOS3104Geodynamics.git  
  
RUN cd /build/GEOS3104Geodynamics/ellipsis && \  
./configure CFLAGS='-g -O2 -m32' && \  
make clean && \  
make && \  
cp ellipsis3d /usr/local/bin  
  
RUN cp -av /build/GEOS3104Geodynamics/Exercises/* /workspace/  
  
# setup space for working in  
VOLUME /workspace/volume  
  
ENV TINI_VERSION v0.8.4  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/usr/local/bin/tini  
RUN chmod +x /usr/local/bin/tini  
  
WORKDIR /workspace  
  
EXPOSE 8888  
ENTRYPOINT ["/usr/local/bin/tini", "--"]  
  
CMD jupyter notebook --ip=0.0.0.0 --no-browser \  
\--NotebookApp.token='' \--allow-root
--NotebookApp.iopub_data_rate_limit=1.0e10  

