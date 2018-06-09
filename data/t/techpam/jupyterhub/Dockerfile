FROM jupyterhub/jupyterhub:latest  
  
MAINTAINER Florent Garcin  
  
# assign root password  
RUN echo "root:docker" | chpasswd  
  
ADD req_pip.txt /srv/jupyterhub/req_pip.txt  
ADD req_conda.txt /srv/jupyterhub/req_conda.txt  
  
# Basic dependencies  
RUN apt-get -y update && \  
apt-get install -y --no-install-recommends \  
openjdk-7-jre-headless \  
sudo \  
libxrender1 \  
libfreetype6-dev \  
libxft-dev \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# Spark  
ENV APACHE_SPARK_VERSION 1.6.2  
RUN cd /tmp && \  
wget -q
http://d3kbcqa49mib13.cloudfront.net/spark-${APACHE_SPARK_VERSION}-bin-
hadoop2.6.tgz && \  
tar xzf spark-${APACHE_SPARK_VERSION}-bin-hadoop2.6.tgz -C /usr/local && \  
rm spark-${APACHE_SPARK_VERSION}-bin-hadoop2.6.tgz  
RUN cd /usr/local && ln -s spark-${APACHE_SPARK_VERSION}-bin-hadoop2.6 spark  
  
# Spark config  
ENV SPARK_HOME /usr/local/spark  
ENV PYTHONPATH $SPARK_HOME/python:$SPARK_HOME/python/lib/py4j-0.9-src.zip  
ENV SPARK_OPTS --driver-java-options=-Xms1024M --driver-java-options=-Xmx4096M
--driver-java-options=-Dlog4j.logLevel=info  
  
# Hadoop config  
ADD cd-yarn /etc/yarn-conf  
ENV YARN_CONF_DIR /etc/yarn-conf  
ENV HADOOP_CONF_DIR /etc/yarn-conf  
ENV HADOOP_USER_NAME hdfs  
  
# spark streaming kafka  
RUN wget -q http://jcenter.bintray.com/org/apache/spark/spark-streaming-kafka-
assembly_2.10/1.6.2/spark-streaming-kafka-assembly_2.10-1.6.2.jar  
RUN mv spark-streaming-kafka-assembly_2.10-1.6.2.jar
/usr/local/spark/lib/spark-streaming-kafka-assembly_2.10-1.6.2.jar  
  
# python 2.7  
RUN conda create -n python27 python=2.7  
RUN /opt/conda/bin/conda install -n python27 --yes matplotlib  
RUN /opt/conda/bin/conda install -n python27 --yes --file
/srv/jupyterhub/req_conda.txt  
RUN /opt/conda/envs/python27/bin/pip install -r /srv/jupyterhub/req_pip.txt  
RUN /opt/conda/envs/python27/bin/python -m pip install --upgrade -I setuptools  
RUN /opt/conda/envs/python27/bin/python -m pip install --upgrade ipykernel  
RUN /opt/conda/envs/python27/bin/python -m ipykernel install  
  
# python 3.5 default  
RUN /opt/conda/bin/conda install --yes matplotlib  
RUN pip install -r /srv/jupyterhub/req_pip.txt  
RUN /opt/conda/bin/conda install --yes --file /srv/jupyterhub/req_conda.txt  
  
# install jupyter notebook  
RUN /opt/conda/bin/conda install --yes jupyter  
  
# install oauthenticator for Github OAuth  
RUN python3 -m pip install oauthenticator  
  
# Create oauthenticator directory and put necessary files in it  
ENV OAUTHENTICATOR_DIR /srv/jupyterhub  
ADD logo.png /srv/jupyterhub/logo.png  
ADD jupyterhub_config.py /srv/jupyterhub/jupyterhub_config.py  
ADD addusers.sh /srv/jupyterhub/addusers.sh  
ADD adduser-jupyter.sh /srv/jupyterhub/adduser-jupyter.sh  
ADD userlist /srv/jupyterhub/userlist  
ADD ssl /srv/jupyterhub/ssl  
  
# copy pyspark local kernel  
RUN mkdir -p /opt/conda/share/jupyter/kernels/pyspark_local  
ADD pyspark_local_kernel.json
/opt/conda/share/jupyter/kernels/pyspark_local/kernel.json  
ADD pyspark_cluster_kernel_py35.json
/opt/conda/share/jupyter/kernels/pyspark_cluster_py35/kernel.json  
ADD pyspark_cluster_kernel_py27.json
/opt/conda/share/jupyter/kernels/pyspark_cluster_py27/kernel.json  
  
# allow install new packages as standard user  
RUN chmod -R 777 /opt/conda  
  
# create user group  
RUN addgroup jupusers  
  
# create common data folder  
RUN mkdir /data  
RUN chmod -R 777 /data  
  
# add users  
RUN ["sh", "/srv/jupyterhub/addusers.sh"]  
  
# map volume  
VOLUME /data  
  
# allow install new packages as standard user  
RUN chmod -R 777 /opt/conda  
  
# set read write on data  
RUN setfacl -m d:g:jupusers:rw /data  
  
#RUN python3 -m pip install git+https://github.com/jupyter/sudospawner  

