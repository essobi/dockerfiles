############################################################  
# Dockerfile to build tomni container images  
# Based on Ubuntu  
############################################################  
  
#https://www.digitalocean.com/community/tutorials/docker-explained-using-
dockerfiles-to-automate-building-of-images  
  
# Set the base image to Ubuntu  
FROM ubuntu  
  
# File Author / Maintainer  
MAINTAINER Seung Lab  
  
# Update the repository sources list  
RUN apt-get -qq update  
  
  
################## BEGIN INSTALLATION ######################  
#Install apt-get packages  
RUN apt-get -qq -y install wget \  
npm \  
nodejs \  
nodejs-legacy \  
ruby-dev \  
libopenctm-dev \  
javacc \  
libpython2.7 \  
libspatialindex-dev  
  
#Set JAVA_HOME  
ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64/  
  
#Download and extract spark  
ENV TEST_SPARK_VERSION=1.6.0  
RUN mkdir thirdparty  
RUN wget
http://apache.mirror.cdnetworks.com/spark/spark-$TEST_SPARK_VERSION/spark-$TEST_SPARK_VERSION-
bin-hadoop2.4.tgz  
RUN tar zxfC spark-$TEST_SPARK_VERSION-bin-hadoop2.4.tgz thirdparty  
  
#Add spark to the env variables  
ENV SPARK_HOME /thirdparty/spark-$TEST_SPARK_VERSION-bin-hadoop2.4  
ENV PYTHONPATH /tomni  
ENV PYTHONPATH $SPARK_HOME/python/:$PYTHONPATH  
ENV PYTHONPATH $SPARK_HOME/python/lib/py4j-0.9-src.zip:$PYTHONPATH  
  
  
#install conda  
RUN wget https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh
-O miniconda.sh;  
RUN hash -r  
RUN bash miniconda.sh -p /miniconda -b  
RUN rm miniconda.sh  
ENV PATH=/miniconda/bin:${PATH}  
RUN conda update -y conda  
  
#Install python packages required for the backend  
RUN conda install -y \  
numpy \  
scikit-image \  
pillow \  
shapely \  
h5py \  
virtualenv  
  
RUN conda install -c https://conda.anaconda.org/ioos rtree  
  
RUN pip install tornado \  
networkx \  
Trimesh \  
pypng \  
urllib3 \  
tox  
  
#Install packages for the frontend  
RUN npm install -g grunt bower  
RUN gem install compass  
  
  
##################### INSTALLATION END #####################  
  
  
# Expose the default ports  
EXPOSE 9000  
EXPOSE 8888

