FROM ubuntu:14.04  
MAINTAINER Maximilian Strehse <max@strehse.eu>  
  
ENV TINI_VERSION v0.6.0  
RUN apt-get update && apt-get -yq install \  
pandoc \  
python \  
supervisor \  
wget \  
python-pip \  
python-dev \  
gfortran \  
libopenblas-dev \  
liblapack-dev \  
r-base \  
python-qt4 \  
libfreetype6-dev \  
libxft-dev \  
libjpeg-dev \  
libpng-dev  
  
RUN pip install pip --upgrade && \  
pip install numpy && \  
pip install scipy && \  
pip install nose && \  
pip install mock && \  
pip install sphinx && \  
pip install astropy && \  
pip install biopython && \  
pip install matplotlib && \  
pip install pandas && \  
pip install pylab && \  
pip install cython && \  
pip install bottleneck && \  
pip install mrjob && \  
pip install scikit-image && \  
pip install scikit-learn || true  
  
RUN pip install pip --upgrade jupyter[all]  
RUN mkdir /notebooks  
WORKDIR /notebooks  
Expose 443  
VOLUME ["/notebooks"]  
  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/usr/bin/tini  
RUN chmod +x /usr/bin/tini  
ENTRYPOINT ["/usr/bin/tini", "--"]  
  
CMD ["jupyter", "notebook", "--port=443", "--no-browser", "--ip=0.0.0.0"]  
  

