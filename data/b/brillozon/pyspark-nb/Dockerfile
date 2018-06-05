# Establish a working envirionment for Spark with more than just the basics.  
#  
# a249876881d3 - From 5/31/16, jupyter/docker-stacks  
#  
FROM jupyter/pyspark-notebook:a249876881d3  
  
MAINTAINER Docker Support <docker-support@brillozon.com>  
  
USER root  
  
RUN \  
echo "deb http://ftp.us.debian.org/debian/ jessie main contrib non-free" >>
/etc/apt/sources.list \  
&& echo "deb-src http://ftp.us.debian.org/debian/ jessie main contrib non-
free" >> /etc/apt/sources.list \  
&& export DEBIAN_FRONTEND=noninteractive \  
&& apt-get update -q \  
&& apt-get build-dep -q -y python-imaging \  
&& apt-get install -q -y -o Dpkg::Options::="--force-confnew" \  
curl  
  
USER jovyan  
  
RUN \  
pip install --upgrade pip \  
&& pip install \  
boto3 \  
pillow \  
stop-words \  
thunder-python  
  
ADD https://archive.ics.uci.edu/ml/machine-learning-
databases/covtype/covtype.data.gz /home/jovyan/work/data/  
COPY notebooks/* /home/jovyan/work/  
COPY data/* /home/jovyan/work/data/  
COPY images/* /home/jovyan/work/images/  
  
USER root  
  
RUN \  
chown -R jovyan.users /home/jovyan \  
&& chmod -R 0775 /home/jovyan  
  
USER jovyan  
  

