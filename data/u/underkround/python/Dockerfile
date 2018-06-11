FROM debian:wheezy  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
build-essential \  
libxml2-dev \  
libxslt1-dev \  
locales \  
python \  
python-dev \  
python-pip \  
zlib1g-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN locale-gen C.UTF-8 && \  
/usr/sbin/update-locale LANG=C.UTF-8  
  
ENV LC_ALL C.UTF-8  
CMD ["python2"]  

