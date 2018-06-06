FROM rerng007/pipeline:spark_base  
  
WORKDIR /root  
  
# Install Anaconda with Python3  
RUN wget -q
https://repo.continuum.io/miniconda/Miniconda3-4.3.21-Linux-x86_64.sh -O
/tmp/miniconda.sh && \  
echo 'c1c15d3baba15bf50293ae963abef853 */tmp/miniconda.sh' | md5sum -c - && \  
bash /tmp/miniconda.sh -f -b -p /opt/conda && \  
/opt/conda/bin/conda install --yes python=3.6 sqlalchemy tornado jinja2
traitlets requests pip && \  
/opt/conda/bin/pip install --upgrade pip && \  
rm /tmp/miniconda.sh  
  
ENV \  
PATH=/opt/conda/bin:$PATH  
  
RUN \  
pip install --upgrade pip  
  
# Downgrade Python 3.6 to Python 3.5 since Spark doesn't like Python 3.6  
RUN \  
conda update conda \  
&& conda install python=3.5  
  
RUN \  
conda config --add channels conda-forge  
  
RUN \  
conda install --yes nltk  
  
RUN python -m nltk.downloader -d /usr/local/share/nltk_data all  
  
RUN \  
conda install --yes luigi gensim  
  
RUN \  
conda install --yes \  
nbconvert==5.2.1 \  
graphviz==2.38.0 \  
seaborn==0.8.0 \  
bqplot==0.9.0 \  
bokeh==0.12.6 \  
&& conda clean -tipsy  
  
RUN \  
mkdir -p /root/tensorboard  
  
RUN \  
mkdir -p /root/models  
  
RUN \  
mkdir -p /root/logs  
  
# Screen  
RUN \  
apt-get update && apt-get install -y screen  
  
# Apache2  
RUN \  
apt-get update \  
&& apt-get install -y apache2  
  
RUN \  
a2enmod proxy \  
&& a2enmod proxy_http \  
&& a2dissite 000-default  
  
RUN \  
mv /var/www/html /var/www/html.orig  
  
RUN \  
mv /etc/apache2/apache2.conf /etc/apache2/apache2.conf.orig  
  
RUN \  
pip install sklearn_pandas==1.4.0 \  
&& pip install git+https://github.com/jpmml/sklearn2pmml.git@0.22.0  
  
ENV \  
SPARK_VERSION=2.1.0 \  
PYSPARK_VERSION=0.10.4  
RUN \  
# This is not a custom version of Spark. It's merely a version with all the
desired -P profiles enabled.  
wget
https://s3.amazonaws.com/fluxcapacitor.com/packages/spark-${SPARK_VERSION}-bin-
fluxcapacitor.tgz \  
&& tar xvzf spark-${SPARK_VERSION}-bin-fluxcapacitor.tgz \  
&& rm spark-${SPARK_VERSION}-bin-fluxcapacitor.tgz  
  
ENV \  
SPARK_HOME=/root/spark-${SPARK_VERSION}-bin-fluxcapacitor  
  
# This must be separate from the ${SPARK_HOME} ENV definition or else Docker
doesn't recognize it  
ENV \  
PATH=${SPARK_HOME}/bin:$PATH  
  
ENV \  
HADOOP_VERSION=2.7.4  
RUN \  
wget
http://www.apache.org/dist/hadoop/common/hadoop-${HADOOP_VERSION}/hadoop-${HADOOP_VERSION}.tar.gz
\  
&& tar xvzf hadoop-${HADOOP_VERSION}.tar.gz \  
&& rm hadoop-${HADOOP_VERSION}.tar.gz  
  
ENV \  
HADOOP_HOME=/root/hadoop-${HADOOP_VERSION} \  
HADOOP_OPTS=-Djava.net.preferIPv4Stack=true  
  
# This must be separate from the ${HADOOP_HOME} ENV definition or else Docker
doesn't recognize it  
ENV \  
HADOOP_CONF=${HADOOP_HOME}/etc/hadoop/ \  
PATH=${HADOOP_HOME}/bin:${HADOOP_HOME}/sbin:${PATH}  
  
# Required by Spark  
ENV \  
HADOOP_CONF_DIR=${HADOOP_CONF}  
  
# Required by Tensorflow  
ENV \  
HADOOP_HDFS_HOME=${HADOOP_HOME}  
  
# Required by Tensorflow for HDFS  
RUN \  
echo 'export CLASSPATH=$(${HADOOP_HDFS_HOME}/bin/hadoop classpath --glob)' >>
/root/.bashrc  
  
ENV \  
LD_LIBRARY_PATH=$LD_LIBRARY_PATH:${JAVA_HOME}/jre/lib/amd64/server  
  
ENV \  
PATH=/root/scripts:$PATH  
  
RUN \  
apt-get install -y ssh  
  
RUN \  
sed -i s/#PermitRootLogin.*/PermitRootLogin\ yes/ /etc/ssh/sshd_config \  
&& sed -i s/#.*StrictHostKeyChecking.*/StrictHostKeyChecking\ no/
/etc/ssh/ssh_config \  
&& ssh-keygen -A \  
&& ssh-keygen -t rsa -f /root/.ssh/id_rsa -q -N "" \  
&& cat /root/.ssh/id_rsa.pub > /root/.ssh/authorized_keys  
  
RUN \  
sed -i "s%<HADOOP_HOME>%${HADOOP_HOME}%" ${HADOOP_CONF}/*.xml \  
&& sed -i "s%\${JAVA_HOME}%${JAVA_HOME}%" ${HADOOP_CONF}/hadoop-env.sh  
  
RUN \  
hadoop namenode -format  
  
# Required by sshd  
RUN \  
mkdir /var/run/sshd  
  
RUN \  
pip install pio-cli==0.87  
  
ENV \  
TF_CPP_MIN_LOG_LEVEL=0 \  
TF_XLA_FLAGS=--xla_generate_hlo_graph=.*  
  
# This will install tensorflow for Python 3.5 since we overrode the Python way
up top.  
RUN \  
pip install tensorflow==1.3.0 \  
&& pip install tensorflow-tensorboard==0.1.4 \  
&& pip install keras==2.0.7  
  
RUN \  
pip install pipeline-ai-cli==0.52  
  
EXPOSE 80 50070 39000 9000 9001 9002 9003 9004 6006 8754 7077 6066 6060 6061
4040 4041 4042 4043 4044 2222 10254  
CMD ["supervise", "."]  

