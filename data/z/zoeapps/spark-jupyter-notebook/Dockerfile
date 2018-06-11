FROM ubuntu:14.04  
MAINTAINER Daniele Venzano <venza@brownhat.org>  
  
RUN apt-get update && apt-get install -y --force-yes software-properties-
common python-software-properties  
RUN apt-add-repository -y ppa:webupd8team/java  
RUN /bin/echo debconf shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections  
  
RUN apt-get update && apt-get -y install oracle-java7-installer oracle-
java7-set-default curl  
  
ARG SPARK_VERSION  
ENV SPARK_VERSION ${SPARK_VERSION:-1.6.2}  
  
ARG HADOOP_VERSION  
ENV HADOOP_VERSION ${HADOOP_VERSION:-hadoop2.6}  
  
ENV JAVA_HOME /usr/lib/jvm/java-7-oracle/  
  
RUN curl -s
http://mirrors.ircam.fr/pub/apache/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-${HADOOP_VERSION}.tgz
| tar -xz -C /opt/  
  
WORKDIR /opt  
  
RUN ln -s spark-${SPARK_VERSION}-bin-${HADOOP_VERSION} spark  
ENV SPARK_HOME /opt/spark  
ENV PATH /opt/spark/bin:/opt/spark/sbin:${PATH}  
  
RUN apt-get update && apt-get install -y --force-yes --no-install-recommends \  
git \  
vim \  
wget \  
build-essential \  
python-dev \  
ca-certificates \  
bzip2 \  
unzip \  
libsm6 \  
pandoc \  
texlive-latex-base \  
texlive-latex-extra \  
texlive-fonts-extra \  
texlive-fonts-recommended \  
texlive-generic-recommended \  
sudo \  
locales \  
libxrender1 \  
libopenblas-dev \  
libjpeg-dev \  
&& apt-get clean  
  
RUN locale-gen en_US.UTF-8  
  
# Install Tini  
RUN wget --quiet https://github.com/krallin/tini/releases/download/v0.6.0/tini
&& \  
echo "d5ed732199c36a1189320e6c4859f0169e950692f451c03e7854243b95f4234b *tini"
| sha256sum -c - && \  
mv tini /usr/local/bin/tini && \  
chmod +x /usr/local/bin/tini  
  
# Configure environment  
ENV CONDA_DIR /opt/conda  
ENV HADOOP_HOME /opt/hadoop  
ENV HADOOP_CONF_DIR $HADOOP_HOME/etc/hadoop  
ENV PATH $HADOOP_HOME/bin:$CONDA_DIR/bin:$PATH  
ENV SHELL /bin/bash  
ENV LC_ALL en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
ENV PYTHONPATH $SPARK_HOME/python:$SPARK_HOME/python/lib/py4j-0.9-src.zip  
ENV HADOOP_VERSION 2.6.1  
# Setup nbuser home directory  
RUN ln -s /mnt/workspace /root/work && \  
mkdir /root/.jupyter && \  
mkdir /root/.local  
  
# Install conda as nbuser  
RUN cd /tmp && \  
mkdir -p $CONDA_DIR && \  
wget http://repo.continuum.io/miniconda/Miniconda3-3.9.1-Linux-x86_64.sh && \  
echo "6c6b44acdd0bc4229377ee10d52c8ac6160c336d9cdd669db7371aa9344e1ac3
*Miniconda3-3.9.1-Linux-x86_64.sh" | sha256sum -c - && \  
/bin/bash Miniconda3-3.9.1-Linux-x86_64.sh -f -b -p $CONDA_DIR && \  
rm Miniconda3-3.9.1-Linux-x86_64.sh && \  
$CONDA_DIR/bin/conda install --yes conda==3.14.1  
  
# Install Jupyter notebook as nbuser  
RUN conda install --yes \  
'notebook=4.1*' \  
terminado \  
&& conda clean -yt  
  
# Install Python 3 packages  
RUN conda install --yes \  
'ipywidgets=4.0*' \  
'pandas=0.17*' \  
'matplotlib=1.4*' \  
'scipy=0.16*' \  
'seaborn=0.6*' \  
'scikit-learn=0.16*' \  
'statsmodels=0.6.1' \  
'pillow' \  
'basemap' \  
&& conda clean -yt  
  
RUN curl
http://apache.mirrors.ovh.net/ftp.apache.org/dist/hadoop/common/hadoop-${HADOOP_VERSION}/hadoop-${HADOOP_VERSION}.tar.gz
| tar -xz -C /opt/  
  
RUN ln -s /opt/hadoop-${HADOOP_VERSION} /opt/hadoop  
  
RUN /opt/conda/bin/pip install thunder-python showit  
  
# Add Spark JARs  
RUN curl http://central.maven.org/maven2/com/databricks/spark-
csv_2.10/1.3.0/spark-csv_2.10-1.3.0.jar -o /opt/spark/com.databricks_spark-
csv_2.10-1.3.0.jar  
RUN curl http://central.maven.org/maven2/org/apache/commons/commons-
csv/1.2/commons-csv-1.2.jar -o /opt/spark/org.apache.commons_commons-
csv-1.2.jar  
RUN curl http://central.maven.org/maven2/com/univocity/univocity-
parsers/1.5.6/univocity-parsers-1.5.6.jar -o
/opt/spark/com.univocity_univocity-parsers-1.5.6.jar  
  
COPY files/spark-defaults.conf /opt/spark-defaults.conf  
  
# Configure container startup as root  
EXPOSE 4040 8888  
WORKDIR /root/work  
ENTRYPOINT ["tini", "--"]  
CMD ["start-notebook.sh"]  
  
# Add local files as late as possible to avoid cache busting  
COPY files/start-notebook.sh /usr/local/bin/  
RUN chmod 755 /usr/local/bin/start-notebook.sh  
COPY files/jupyter_notebook_config.py /root/.jupyter/  
RUN mkdir -p /root/.ipython/profile_default/startup/  
COPY files/00-pyspark-setup.py /root/.ipython/profile_default/startup/  
  
COPY files/core-site.xml /opt  
COPY files/hdfs-site.xml /opt  

