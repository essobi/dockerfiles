# Data science tools for Python 2.7  
# - Anaconda (a practical data science plateform)  
# - numpy, pandas, scrapy, scipy, scikit-learn, and nltk  
# - R, Rstudio, R packages  
# - OpenCV (and its dependencies for python 2.7, installed through apt-get)  
# - Scala and sbt  
# - Julia  
FROM patrickmerlot/ubuntu_14.04  
MAINTAINER Patrick Merlot <patrick.merlot@gmail.com>  
  
USER root  
RUN apt-get -y update  
ENV DEBIAN_FRONTEND noninteractive  
  
# versions  
ENV ANACONDA_VERSION 2-4.0.0  
ENV OPENCV_VERSION 3.0.0  
# Install Anaconda.  
RUN echo 'export PATH=/opt/conda/bin:$PATH' > conda.sh && mv conda.sh
/etc/profile.d/  
RUN wget https://repo.continuum.io/archive/Anaconda$ANACONDA_VERSION-
Linux-x86_64.sh  
RUN /bin/bash /Anaconda$ANACONDA_VERSION-Linux-x86_64.sh -b -p /opt/conda && \  
rm /Anaconda$ANACONDA_VERSION-Linux-x86_64.sh  
# Add the anaconda binary directory to your PATH environment variable  
ENV PATH /opt/conda/bin:$PATH

