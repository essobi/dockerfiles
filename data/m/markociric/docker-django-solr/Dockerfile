FROM django:1.8-python2  
MAINTAINER Marko Ciric (ciric.marko@gmail.com)  
  
RUN apt-get update  
  
WORKDIR /usr/src/app/  
EXPOSE 8000 8983  
  
RUN pip install virtualenv && \  
mkdir venv && \  
virtualenv env && \  
apt-get install -qq -y wget libmysqlclient-dev python-dev \  
libffi-dev libxml2-dev libxslt1-dev zlib1g-dev \  
libtiff5-dev libjpeg-dev zlib1g-dev libfreetype6-dev \  
liblcms2-dev libwebp-dev tcl8.5-dev tk8.5-dev python-tk \  
libxslt1-dev libcairo-dev libpango-1.0.0 libpango1.0-dev  
  
RUN apt-get install -qq -y openjdk-7-jdk && mkdir /usr/java && \  
ln -s /usr/lib/jvm/java-7-openjdk-amd64 /usr/java/default && \  
cd /opt && \  
wget http://archive.apache.org/dist/lucene/solr/5.2.1/solr-5.2.1.tgz && \  
tar -xvf solr-5.2.1.tgz && cp -R solr-5.2.1/example /opt/solr  

