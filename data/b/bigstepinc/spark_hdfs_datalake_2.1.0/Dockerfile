FROM mcristinagrosu/bigstep_hdfs_datalake  
  
RUN apk add --update alpine-sdk  
RUN apk add libffi && apk add jq  
  
# Install Spark 2.1.0  
RUN cd /opt && wget http://d3kbcqa49mib13.cloudfront.net/spark-2.1.0-bin-
hadoop2.7.tgz  
RUN tar xzvf /opt/spark-2.1.0-bin-hadoop2.7.tgz  
RUN rm /opt/spark-2.1.0-bin-hadoop2.7.tgz  
  
# Spark pointers  
ENV SPARK_HOME /opt/spark-2.1.0-bin-hadoop2.7  
ENV R_LIBS_USER
$SPARK_HOME/R/lib:/opt/conda/envs/ir/lib/R/library:/opt/conda/lib/R/library  
ENV PYTHONPATH $SPARK_HOME/python:$SPARK_HOME/python/lib/py4j-0.8.2.1-src.zip  
  
RUN mv spark-2.1.0-bin-hadoop2.7 /opt/ && mkdir -p /user && mkdir -p
/user/notebooks && mkdir -p /user/datasets  
  
ADD entrypoint.sh /  
ADD core-site.xml.datalake /opt/spark-2.1.0-bin-hadoop2.7/conf/  
ADD core-site.xml.datalake.integration /opt/spark-2.1.0-bin-hadoop2.7/conf/  
  
ADD krb5.conf.integration /etc/  
ADD krb5.conf /etc/  
  
RUN chmod 777 /entrypoint.sh  
ADD spark-defaults.conf /opt/spark-2.1.0-bin-hadoop2.7/conf/spark-
defaults.conf.template  
  
ENV HADOOP_HOME /opt/hadoop  
ENV HADOOP_CONF_DIR /opt/hadoop/etc/hadoop  
  
ENV CONDA_DIR /opt/conda  
ENV PATH $CONDA_DIR/bin:$PATH  
ENV PATH $PATH:/$SPARK_HOME/bin/  
  
RUN cd /opt && \  
#wget https://repo.continuum.io/miniconda/Miniconda2-4.1.11-Linux-x86_64.sh &&
\  
# /bin/bash Miniconda2-4.1.11-Linux-x86_64.sh -b -p $CONDA_DIR && \  
# rm -rf Miniconda2-4.1.11-Linux-x86_64.sh  
  
wget https://repo.continuum.io/miniconda/Miniconda2-4.2.12-Linux-x86_64.sh &&
\  
/bin/bash Miniconda2-4.2.12-Linux-x86_64.sh -b -p $CONDA_DIR && \  
rm -rf Miniconda2-4.2.12-Linux-x86_64.sh  
  
RUN export PATH=$PATH:/$CONDA_DIR/bin  
  
# Install Jupyter notebook  
RUN $CONDA_DIR/bin/conda install --yes \  
'notebook' && \  
$CONDA_DIR/bin/conda clean -yt  
  
RUN $CONDA_DIR/bin/jupyter notebook --generate-config  
  
RUN $CONDA_DIR/bin/conda install --yes nb_conda  
RUN $CONDA_DIR/bin/python -m nb_conda_kernels.install --disable
\--prefix=$CONDA_DIR && \  
$CONDA_DIR/bin/conda clean -yt  
RUN jupyter-nbextension enable nb_conda --py --sys-prefix  
RUN jupyter-serverextension enable nb_conda --py --sys-prefix  
RUN jupyter-nbextension enable nbpresent --py --sys-prefix  
RUN jupyter-serverextension enable nbpresent --py --sys-prefix  
  
#Install Scala Spark kernel  
ENV SBT_VERSION 0.13.11  
ENV SBT_HOME /usr/local/sbt  
ENV PATH ${PATH}:${SBT_HOME}/bin  
  
# Install sbt  
RUN curl -sL "http://dl.bintray.com/sbt/native-
packages/sbt/$SBT_VERSION/sbt-$SBT_VERSION.tgz" | gunzip | tar -x -C
/usr/local && \  
echo -ne "- with sbt $SBT_VERSION\n" >> /root/.built  
  
RUN cd /tmp && \  
curl -sL "http://dl.bintray.com/sbt/native-
packages/sbt/$SBT_VERSION/sbt-$SBT_VERSION.tgz" | gunzip | tar -x -C
/usr/local && \  
echo -ne "- with sbt $SBT_VERSION\n" >> /root/.built &&\  
git clone https://github.com/apache/incubator-toree.git && \  
cd incubator-toree && \  
# git checkout 87a9eb8ad08406ce0747e92f7714d4eb54153293 && \  
# git checkout 7c1bfb6df7130477c558e69bbb518b0af364e06a && \  
make dist SHELL=/bin/bash APACHE_SPARK_VERSION=2.1.0 SCALA_VERSION=2.11 && \  
mv /tmp/incubator-toree/dist/toree /opt/toree-kernel && \  
chmod +x /opt/toree-kernel && \  
rm -rf /tmp/incubator-toree  
  
#Install Python3 packages  
RUN $CONDA_DIR/bin/conda install --yes \  
'ipywidgets' \  
'pandas' \  
'matplotlib' \  
'scipy' \  
'seaborn' \  
'scikit-learn' && \  
$CONDA_DIR/bin/conda clean -yt  
  
RUN $CONDA_DIR/bin/conda config --set auto_update_conda False  
  
RUN CONDA_VERBOSE=3 $CONDA_DIR/bin/conda create --yes -p
/opt/conda/envs/python3 python=3.5 ipython ipywidgets pandas matplotlib scipy
seaborn scikit-learn  
RUN bash -c '. activate python3 && \  
python -m ipykernel.kernelspec --prefix=/opt/conda && \  
. deactivate'  
RUN jq --arg v "$CONDA_DIR/envs/python3/bin/python"
'.["env"]["PYSPARK_PYTHON"]=$v'
/opt/conda/share/jupyter/kernels/python3/kernel.json > /tmp/kernel.json && \  
mv /tmp/kernel.json /opt/conda/share/jupyter/kernels/python3/kernel.json  
  
#Install R kernel and set up environment  
RUN $CONDA_DIR/bin/conda config --add channels r  
RUN $CONDA_DIR/bin/conda install --yes -c r r-essentials r-base r-irkernel
r-irdisplay r-ggplot2 r-repr r-rcurl  
RUN $CONDA_DIR/bin/conda create --yes -n ir -c r r-essentials r-base
r-irkernel r-irdisplay r-ggplot2 r-repr r-rcurl  
  
RUN mkdir -p /opt/conda/share/jupyter/kernels/scala  
COPY kernel.json /opt/conda/share/jupyter/kernels/scala/  
  
RUN cd /root && wget
http://central.maven.org/maven2/com/google/collections/google-
collections/1.0/google-collections-1.0.jar  
  
#Solution to readline library issues for SparkR context/session  
RUN mv $CONDA_DIR/envs/python3/lib/libreadline.so.6
/opt/conda/envs/python3/lib/libreadline.so.6.tmp && \  
ln -s /usr/lib/libreadline.so.6 $CONDA_DIR/envs/python3/lib/libreadline.so.6  
RUN mv $CONDA_DIR/envs/ir/lib/libreadline.so.6
$CONDA_DIR/envs/ir/lib/libreadline.so.6.tmp && \  
ln -s /usr/lib/libreadline.so.6 $CONDA_DIR/envs/ir/lib/libreadline.so.6  
RUN mv $CONDA_DIR/lib/libreadline.so.6 $CONDA_DIR/lib/libreadline.so.6.tmp &&
\  
ln -s /usr/lib/libreadline.so.6 $CONDA_DIR/lib/libreadline.so.6  
RUN mv $CONDA_DIR/pkgs/readline-6.2-2/lib/libreadline.so.6
$CONDA_DIR/pkgs/readline-6.2-2/lib/libreadline.so.6.tmp && \  
ln -s /usr/lib/libreadline.so.6
$CONDA_DIR/pkgs/readline-6.2-2/lib/libreadline.so.6  
  
#Add Getting Started Notebooks  
RUN wget
http://repo.bigstepcloud.com/bigstep/datalab/DataLab%20Getting%20Started%20in%20Scala.ipynb
-O /user/notebooks/DataLab\ Getting\ Started\ in\ Scala.ipynb  
RUN wget
http://repo.bigstepcloud.com/bigstep/datalab/DataLab%20Getting%20Started%20in%20R.ipynb
-O /user/notebooks/DataLab\ Getting\ Started\ in\ R.ipynb  
RUN wget
http://repo.bigstepcloud.com/bigstep/datalab/DataLab%20Getting%20Started%20in%20Python.ipynb
-O /user/notebooks/DataLab\ Getting\ Started\ in\ Python.ipynb  
  
#Add cairo-dev for R notebook  
RUN apk add cairo-dev  
  
# Add hive-site.xml conf for metastore configuration  
ADD hive-site.xml /opt/spark-2.1.0-bin-hadoop2.7/conf/  
  
# Change Jupyter Logo  
RUN wget http://repo.bigstepcloud.com/bigstep/datalab/logo.png -O logo.png  
  
RUN cp logo.png $CONDA_DIR/envs/python3/doc/global/template/images/logo.png &&
\  
cp logo.png $CONDA_DIR/envs/python3/lib/python3.5/site-
packages/notebook/static/base/images/logo.png && \  
cp logo.png $CONDA_DIR/lib/python2.7/site-
packages/notebook/static/base/images/logo.png && \  
#cp logo.png $CONDA_DIR/pkgs/notebook-4.2.3-py27_0/lib/python2.7/site-
packages/notebook/static/base/images/logo.png && \  
#cp logo.png $CONDA_DIR/pkgs/qt-5.6.0-0/doc/global/template/images/logo.png &&
\  
#cp logo.png $CONDA_DIR/pkgs/notebook-4.2.3-py35_0/lib/python3.5/site-
packages/notebook/static/base/images/logo.png && \  
cp logo.png $CONDA_DIR/doc/global/template/images/logo.png && \  
rm -rf logo.png  
  
RUN wget http://repo.bigstepcloud.com/bigstep/datalab/hive-
schema-1.2.0.postgres.sql -O /opt/spark-2.1.0-bin-hadoop2.7/jars/hive-
schema-1.2.0.postgres.sql && \  
wget http://repo.bigstepcloud.com/bigstep/datalab/hive-txn-
schema-0.13.0.postgres.sql -O /opt/spark-2.1.0-bin-hadoop2.7/jars/hive-txn-
schema-0.13.0.postgres.sql && \  
wget http://repo.bigstepcloud.com/bigstep/datalab/hive-txn-
schema-0.14.0.postgres.sql -O /opt/spark-2.1.0-bin-hadoop2.7/jars/hive-txn-
schema-0.14.0.postgres.sql  
  
RUN apk add postgresql-client  
  
# Add Script for hashing password  
ADD password.py /opt  
  
# Download Bigstep Data Lake Client Libraries  
RUN wget https://github.com/bigstepinc/datalake-client-
libraries/releases/download/untagged-f557695f573fa1823db2/datalake-client-
libraries-1.5-SNAPSHOT.jar -P /opt/spark-2.1.0-bin-hadoop2.7/jars/  
  
# Get Spark Thrift Postgresql connector  
RUN wget https://jdbc.postgresql.org/download/postgresql-9.4.1212.jar -P
/opt/spark-2.1.0-bin-hadoop2.7/jars/  
  
#Get Kafka Streaming connector  
RUN wget http://central.maven.org/maven2/org/apache/spark/spark-streaming-
kafka-0-10_2.10/2.1.0/spark-streaming-kafka-0-10_2.10-2.1.0.jar -P
/opt/spark-2.1.0-bin-hadoop2.7/jars/  
  
#Get Kafka Structured Streaming connector  
RUN wget http://central.maven.org/maven2/org/apache/spark/spark-sql-
kafka-0-10_2.10/2.1.0/spark-sql-kafka-0-10_2.10-2.1.0.jar -P
/opt/spark-2.1.0-bin-hadoop2.7/jars/  
  
# Get the right Toree Assembly Jar  
RUN wget http://repo.bigstepcloud.com/bigstep/datalab/toree-
assembly-0.2.0.dev1-incubating-SNAPSHOT.jar -O /opt/toree-kernel/lib/toree-
assembly-0.2.0.dev1-incubating-SNAPSHOT.jar  
  
# Get the examples jar in default location  
RUN cp /opt/spark-2.1.0-bin-hadoop2.7/examples/jars/spark-
examples_2.11-2.1.0.jar /opt/spark-2.1.0-bin-hadoop2.7/jars/spark-
examples_2.11-2.1.0.jar  
  
#Overwrite the Spark daemon file  
ADD spark-daemon.sh /opt/spark-2.1.0-bin-hadoop2.7/sbin/spark-daemon.sh  
  
#Overwrite log4j properties file  
ADD log4j.properties /opt/spark-2.1.0-bin-hadoop2.7/conf/log4j.properties  
  
# SparkMaster SparkMasterWebUI SparkWorkerWebUI REST Jupyter Spark Thrift  
EXPOSE 7077 8080 8081 6066 8888 4040 88 10000  
ENTRYPOINT ["/entrypoint.sh"]  

