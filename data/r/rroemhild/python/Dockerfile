FROM debian:jessie  
  
MAINTAINER Rafael Römhild <rafael@roemhild.de>  
  
# http://bugs.python.org/issue19846  
ENV LANG C.UTF-8  
  
RUN apt-get -q update \  
&& apt-get install --no-install-recommends -y -q \  
ca-certificates build-essential git mercurial locales \  
python2.7 python2.7-dev python-pip \  
libffi-dev libssl-dev libxml2-dev \  
libxslt1-dev libpq-dev libmysqlclient-dev libcurl4-openssl-dev \  
libjpeg-dev zlib1g-dev libpng12-dev \  
gfortran libblas-dev liblapack-dev libatlas-dev libquadmath0 \  
libfreetype6-dev pkg-config swig \  
&& locale-gen C.UTF-8 \  
&& /usr/sbin/update-locale LANG=C.UTF-8 \  
&& echo 'en_US.UTF-8 UTF-8' >> /etc/locale.gen \  
&& locale-gen \  
&& apt-get clean && rm -rf /var/lib/apt/lists/*  
  
# Upgrade pip and install virtualenv  
RUN pip install --upgrade pip virtualenv  
  
WORKDIR /app  
  
CMD ["python2.7"]  

