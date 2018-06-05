# uwsgi for python 2  
# a base image for further deployment of python2 wsgi apps with uwsgi  
# Version 0.1  
FROM python:2.7  
MAINTAINER Hong Xu <hong@topbug.net>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
ENV UWSGIVERSION 2.0.13.1  
RUN apt-get update && apt-get install -y --no-install-recommends \  
build-essential \  
libjansson-dev \  
libpcre3-dev \  
libssl-dev \  
libxml2-dev \  
wget \  
zlib1g-dev  
  
RUN pip install gevent greenlet  
  
RUN cd /usr/src && \  
wget --quiet -O -
http://projects.unbit.it/downloads/uwsgi-${UWSGIVERSION}.tar.gz | \  
tar zxvf -  
  
RUN cd /usr/src/uwsgi-${UWSGIVERSION} && \  
python uwsgiconfig.py --build default && \  
python setup.py install  
  
EXPOSE 9000 9002  
ENV NUM_PROCESSES=1 NUM_THREADS=1 WSGI_MODULE="" WSGI_FILE="" \  
ADDITIONAL_ARGUMENTS="" ADDITIONAL_USER_ARGUMENTS=""  
# Run uwsgi unpriviledged  
RUN groupadd uwsgi && useradd -g uwsgi uwsgi  
  
# Make a directory to serve uwsgi files  
RUN mkdir -vp /var/uwsgi && chown -v uwsgi.uwsgi /var/uwsgi  
  
COPY run.sh /usr/local/bin/run.sh  
  
# Add a script to easily install uWSGI plugin  
COPY docker-install-uwsgi-plugin.sh /usr/local/bin/docker-install-uwsgi-plugin  
  
CMD ["/usr/local/bin/run.sh"]  

