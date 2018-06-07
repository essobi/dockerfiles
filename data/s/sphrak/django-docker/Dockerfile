FROM ubuntu:16.04  
ENV LANG en_US.utf8  
ENV LC_ALL en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
RUN apt-get update && \  
apt-get install -y tzdata locales && \  
rm -rf /var/lib/apt/lists/* && \  
localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8  
#RUN /usr/sbin/update-locale LANG="en_US.UTF-8" LC_ALL="en_US.UTF-8"
LANGUAGE="en_US.UTF-8"  
RUN apt-get update  
RUN apt-get upgrade -y  
RUN apt-get install -y \  
curl \  
enchant \  
git \  
libbz2-dev \  
libffi-dev \  
libjpeg-dev \  
libmemcached-dev \  
python-setuptools \  
python3 \  
python3-gdal \  
python3-pip \  
python3-psycopg2 \  
tox \  
zlib1g-dev  
RUN rm -rf /var/lib/apt/lists/*  
ENV PYTHONDONTWRITEBYTECODE 1  
RUN useradd django -m -d /django  
USER django  

