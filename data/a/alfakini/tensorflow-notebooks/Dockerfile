FROM gcr.io/tensorflow/tensorflow  
MAINTAINER Alan Fachini <alfakini@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -y update && \  
apt-get -y install \  
gfortran \  
libblas-dev \  
liblapack-dev \  
libjpeg-dev \  
libpng-dev \  
libtiff-dev \  
zlib1g-dev \  
libfreetype6-dev \  
liblcms2-dev \  
libwebp-dev  
  
ENV TENSORFLOW_VERSION 0.8.0  
RUN pip --no-cache-dir install --upgrade \  
jupyter numpy scipy matplotlib scikit-learn scikit-image \  
http://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-${TENSORFLOW_VERSION}-cp27-none-
linux_x86_64.whl  
  
VOLUME /notebooks  
WORKDIR /notebooks  
  
ENV TINI_VERSION v0.9.0  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/tini  
RUN chmod +x /tini  
ENTRYPOINT ["/tini", "--"]  
  
CMD ["jupyter", "notebook", "--no-browser"]  
  

