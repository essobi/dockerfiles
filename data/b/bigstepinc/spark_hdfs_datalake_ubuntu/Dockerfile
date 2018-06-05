FROM ubuntu:16.04  
ADD entrypoint.sh /  
ADD password.py /opt/  
ADD version.json /opt/  
ADD env.sh /opt/  
ADD handlers.py /opt/  
  
ADD core-site.xml.datalake /opt/spark-2.3.0-bin-hadoop2.7/conf/  
ADD core-site.xml.datalake.integration /opt/spark-2.3.0-bin-hadoop2.7/conf/  
ADD spark-defaults.conf /opt/spark-2.3.0-bin-hadoop2.7/conf/spark-
defaults.conf  
ADD hive-site.xml /opt/spark-2.3.0-bin-hadoop2.7/conf/  
  
ADD krb5.conf.integration /etc/  
ADD krb5.conf /etc/  
  
# Install Java 8  
ENV JAVA_HOME /opt/jdk1.8.0_171  
ENV PATH
$PATH:/opt/jdk1.8.0_171/bin:/opt/jdk1.8.0_171/jre/bin:/etc/alternatives:/var/lib/dpkg/alternatives  
  
RUN apt-get -qq update -y  
RUN apt-get install -y unzip wget curl tar bzip2 software-properties-common
git  
  
RUN cd /opt && wget --no-cookies --no-check-certificate --header "Cookie:
gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-
cookie" "http://download.oracle.com/otn-
pub/java/jdk/8u171-b11/512cd62ec5174c3487ac17c61aaa89e8/jdk-8u171-linux-x64.tar.gz"
&&\  
tar xzf jdk-8u171-linux-x64.tar.gz && rm -rf jdk-8u171-linux-x64.tar.gz  
  
RUN echo 'export JAVA_HOME="/opt/jdk1.8.0_171"' >> ~/.bashrc && \  
echo 'export PATH="$PATH:/opt/jdk1.8.0_171/bin:/opt/jdk1.8.0_171/jre/bin"' >>
~/.bashrc && \  
bash ~/.bashrc && cd /opt/jdk1.8.0_171/ && update-alternatives --install
/usr/bin/java java /opt/jdk1.8.0_171/bin/java 1  
  
#Add Java Security Policies  
RUN curl -L -C - -b "oraclelicense=accept-securebackup-cookie" -O
http://download.oracle.com/otn-pub/java/jce/8/jce_policy-8.zip && \  
unzip jce_policy-8.zip  
RUN cp UnlimitedJCEPolicyJDK8/US_export_policy.jar
/opt/jdk1.8.0_171/jre/lib/security/ && cp
UnlimitedJCEPolicyJDK8/local_policy.jar /opt/jdk1.8.0_171/jre/lib/security/  
RUN rm -rf UnlimitedJCEPolicyJDK8  
  
# Install Spark 2.3.0  
RUN cd /opt && wget
http://apache.javapipe.com/spark/spark-2.3.0/spark-2.3.0-bin-hadoop2.7.tgz &&
\  
tar xzvf /opt/spark-2.3.0-bin-hadoop2.7.tgz && \  
rm /opt/spark-2.3.0-bin-hadoop2.7.tgz  
  
# Spark pointers for Jupyter Notebook  
ENV SPARK_HOME /opt/spark-2.3.0-bin-hadoop2.7  
ENV R_LIBS_USER
$SPARK_HOME/R/lib:/opt/conda/envs/ir/lib/R/library:/opt/conda/lib/R/library  
ENV PYTHONPATH $SPARK_HOME/python:$SPARK_HOME/python/lib/py4j-0.8.2.1-src.zip  
  
# Create additional files in the DataLake  
RUN mkdir -p /user && mkdir -p /user/notebooks && mkdir -p /user/datasets &&
chmod 777 /entrypoint.sh  
  
# Setup Miniconda  
ENV CONDA_DIR /opt/conda  
ENV PATH $CONDA_DIR/bin:$PATH  
ENV PATH $PATH:/$SPARK_HOME/bin/  
  
RUN cd /opt && \  
wget https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh &&
\  
/bin/bash Miniconda2-latest-Linux-x86_64.sh -b -p $CONDA_DIR && \  
rm -rf Miniconda2-latest-Linux-x86_64.sh  
  
RUN export PATH=$PATH:$CONDA_DIR/bin  
  
# Install Jupyter notebook  
RUN $CONDA_DIR/bin/conda install --yes \  
'notebook' && \  
$CONDA_DIR/bin/conda clean -yt  
  
RUN $CONDA_DIR/bin/jupyter notebook --generate-config --allow-root  
  
RUN $CONDA_DIR/bin/conda install -c conda-forge nb_conda  
RUN $CONDA_DIR/bin/python -m nb_conda_kernels.install --disable
\--prefix=$CONDA_DIR && \  
$CONDA_DIR/bin/conda clean -yt  
  
#Add Spark progress bar extension and presentation extensions  
RUN pip install nbpresent jupyter-spark lxml && \  
jupyter nbextension install nbpresent --py --overwrite && \  
jupyter-nbextension enable nb_conda --py --sys-prefix && \  
jupyter-serverextension enable nb_conda --py --sys-prefix && \  
jupyter-nbextension enable nbpresent --py --sys-prefix && \  
jupyter-serverextension enable nbpresent --py --sys-prefix && \  
jupyter serverextension enable \--py jupyter_spark && \  
jupyter nbextension install --py jupyter_spark && \  
jupyter nbextension enable \--py jupyter_spark && \  
jupyter nbextension enable \--py widgetsnbextension  
  
#Add Spark progress bar extension  
RUN pip install jupyter-spark  
  
#RUN pip install lxml  
#Install Scala Spark kernel  
ENV SBT_VERSION 0.13.11  
ENV SBT_HOME /usr/local/sbt  
ENV PATH ${PATH}:${SBT_HOME}/bin  
  
#Install Python3 packages  
RUN cd /root && $CONDA_DIR/bin/conda install --yes \  
'ipywidgets' \  
'pandas' \  
'matplotlib' \  
'scipy' \  
'seaborn' \  
'scikit-learn' && \  
$CONDA_DIR/bin/conda clean -yt  
  
RUN $CONDA_DIR/bin/conda config --set auto_update_conda False  
  
RUN CONDA_VERBOSE=3 $CONDA_DIR/bin/conda create --yes -p
$CONDA_DIR/envs/python3 python=3.5 ipython ipywidgets pandas matplotlib scipy
seaborn scikit-learn  
RUN bash -c '. activate $CONDA_DIR/envs/python3 && \  
python -m ipykernel.kernelspec --prefix=/opt/conda && \  
. deactivate'  
  
RUN wget https://github.com/stedolan/jq/releases/download/jq-1.5/jq-linux64 -O
/root/jq-linux64  
  
RUN chmod +x /root/jq-linux64  
RUN /root/jq-linux64 --arg v "$CONDA_DIR/envs/python3/bin/python"
'.["env"]["PYSPARK_PYTHON"]=$v'
/opt/conda/share/jupyter/kernels/python3/kernel.json > /tmp/kernel.json && \  
mv /tmp/kernel.json /opt/conda/share/jupyter/kernels/python3/kernel.json  
  
#Install R kernel and set up environment  
RUN $CONDA_DIR/bin/conda config --add channels r  
RUN $CONDA_DIR/bin/conda install --yes -c r r-essentials r-base r-irkernel
r-irdisplay r-ggplot2 r-repr r-rcurl  
RUN $CONDA_DIR/bin/conda create --yes -n ir -c r r-essentials r-base
r-irkernel r-irdisplay r-ggplot2 r-repr r-rcurl  
  
#Configure Scala kernel  
RUN mkdir -p /opt/conda/share/jupyter/kernels/scala  
COPY kernel.json /opt/conda/share/jupyter/kernels/scala/  
  
RUN cd /root && wget
http://central.maven.org/maven2/com/google/collections/google-
collections/1.0/google-collections-1.0.jar  
  
#Add Getting Started Notebooks and change Jupyter logo and download additional
libraries  
RUN wget
http://repo.uk.bigstepcloud.com/bigstep/datalab/datalab_getting_started_in_scala__4.ipynb
-O /user/notebooks/DataLab\ Getting\ Started\ in\ Scala.ipynb && \  
wget
http://repo.bigstepcloud.com/bigstep/datalab/DataLab%2BGetting%2BStarted%2Bin%2BR%20%281%29.ipynb
-O /user/notebooks/DataLab\ Getting\ Started\ in\ R.ipynb && \  
wget
http://repo.bigstepcloud.com/bigstep/datalab/DataLab%2BGetting%2BStarted%2Bin%2BPython%20%283%29.ipynb
-O /user/notebooks/DataLab\ Getting\ Started\ in\ Python.ipynb && \  
wget http://repo.bigstepcloud.com/bigstep/datalab/logo.png -O logo.png && \  
cp logo.png $CONDA_DIR/envs/python3/doc/global/template/images/logo.png && \  
cp logo.png $CONDA_DIR/envs/python3/lib/python3.5/site-
packages/notebook/static/base/images/logo.png && \  
cp logo.png $CONDA_DIR/lib/python2.7/site-
packages/notebook/static/base/images/logo.png && \  
cp logo.png $CONDA_DIR/doc/global/template/images/logo.png && \  
rm -rf logo.png && \  
cd $SPARK_HOME/jars/ && wget
http://repo.bigstepcloud.com/bigstep/datalab/hive-schema-1.2.0.postgres.sql &&
\  
wget http://repo.bigstepcloud.com/bigstep/datalab/hive-txn-
schema-0.13.0.postgres.sql && \  
wget http://repo.bigstepcloud.com/bigstep/datalab/hive-txn-
schema-0.14.0.postgres.sql && \  
wget https://jdbc.postgresql.org/download/postgresql-9.4.1212.jar -P
$SPARK_HOME/jars/ && \  
wget http://central.maven.org/maven2/org/apache/spark/spark-streaming-
kafka-0-10_2.11/2.3.0/spark-streaming-kafka-0-10_2.11-2.3.0.jar -P
$SPARK_HOME/jars/ && \  
wget http://central.maven.org/maven2/org/apache/spark/spark-sql-
kafka-0-10_2.11/2.3.0/spark-sql-kafka-0-10_2.11-2.3.0.jar -P $SPARK_HOME/jars/
&& \  
cp $SPARK_HOME/examples/jars/spark-examples_2.11-2.3.0.jar
$SPARK_HOME/jars/spark-examples_2.11-2.3.0.jar  
  
# Setup PostgreSQL connection prerequisites and add libraries for the R
environment  
RUN apt-get update -y  
RUN add-apt-repository "deb http://apt.postgresql.org/pub/repos/apt/ trusty-
pgdg main" && \  
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key
add -  
RUN apt-get install -y postgresql-client libcairo2-dev python-cairo-dev
python3-cairo-dev  
  
# Get Spark Thrift Postgresql connector  
#RUN wget https://jdbc.postgresql.org/download/postgresql-9.4.1212.jar -P
$SPARK_HOME/jars/  
#Get Kafka Streaming connector  
#RUN wget http://central.maven.org/maven2/org/apache/spark/spark-streaming-
kafka-0-10_2.11/2.3.0/spark-streaming-kafka-0-10_2.11-2.3.0.jar -P
$SPARK_HOME/jars/  
#Get Kafka Structured Streaming connector  
#RUN wget http://central.maven.org/maven2/org/apache/spark/spark-sql-
kafka-0-10_2.11/2.3.0/spark-sql-kafka-0-10_2.11-2.3.0.jar -P $SPARK_HOME/jars/  
# Get the examples jar in default location  
#RUN cp $SPARK_HOME/examples/jars/spark-examples_2.11-2.3.0.jar
$SPARK_HOME/jars/spark-examples_2.11-2.3.0.jar  
#Overwrite the Spark daemon file  
#ADD spark-daemon.sh $SPARK_HOME/sbin/spark-daemon.sh  
#Overwrite log4j properties file  
#ADD log4j.properties $SPARK_HOME/conf/log4j.properties  
RUN cd /tmp && \  
wget "http://repo.bigstepcloud.com/bigstep/datalab/sbt-0.13.11.tgz" -O
/tmp/sbt-0.13.11.tgz && \  
tar -xvf /tmp/sbt-0.13.11.tgz -C /usr/local && \  
echo -ne "- with sbt $SBT_VERSION\n" >> /root/.built && \  
git clone https://github.com/apache/incubator-toree.git && \  
cd incubator-toree && \  
git checkout c064a0d97cb52645cab6f43f874659b0dc1020e9 && \  
make dist SHELL=/bin/bash APACHE_SPARK_VERSION=2.3.0 SCALA_VERSION=2.11 && \  
mv /tmp/incubator-toree/dist/toree /opt/toree-kernel && \  
chmod +x /opt/toree-kernel && \  
rm -rf /tmp/incubator-toree && \  
wget http://repo.bigstepcloud.com/bigstep/datalab/toree-
assembly-0.3.0.dev1-incubating-SNAPSHOT.jar -O /opt/toree-kernel/lib/toree-
assembly-0.3.0.dev1-incubating-SNAPSHOT.jar && \  
cd /opt/ && \  
wget http://repo.uk.bigstepcloud.com/bigstep/datalab/datalake-1.5-SNAPSHOT-
bin.tar.gz && \  
tar xzvf datalake-1.5-SNAPSHOT-bin.tar.gz && \  
rm -rf datalake-1.5-SNAPSHOT-bin.tar.gz && \  
export PATH=$PATH:/opt/datalake-1.5-SNAPSHOT/bin  
  
# SparkMaster SparkMasterWebUI SparkWorkerWebUI REST Jupyter Spark Thrift  
EXPOSE 7077 8080 8081 6066 8888 4040 88 10000  
ENTRYPOINT ["/entrypoint.sh"]  

