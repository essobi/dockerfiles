FROM python:3-onbuild  
MAINTAINER Dmitry Ustalov <dmitry.ustalov@gmail.com>  
  
RUN \  
apt-get update && \  
apt-get install -y -o Dpkg::Options::="--force-confold" \--no-install-
recommends graphviz && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
EXPOSE 5000  
USER nobody  
  
CMD ["uwsgi", "--http", "0.0.0.0:5000", "--master", "--module", "app:app", "--
processes", "1", "--threads", "4"]  

