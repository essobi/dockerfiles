FROM rocker/tidyverse:3.4.2  
USER root  
  
# Spark dependencies versions  
ENV APACHE_SPARK_VERSION 2.1.0  
ENV HADOOP_VERSION 2.7  
# Install system libraries required by R packages  
RUN apt-get -y update && apt-get install -y libcups2 libcups2-dev
openjdk-8-jdk systemd \  
unixodbc-dev libbz2-dev libgsl-dev odbcinst && \  
apt-get clean  
  
# Install Impala ODBC dependency  
RUN cd /tmp && \  
wget --no-verbose
https://downloads.cloudera.com/connectors/impala_odbc_2.5.41.1029/Debian/clouderaimpalaodbc_2.5.41.1029-2_amd64.deb
&& \  
dpkg -i clouderaimpalaodbc_2.5.41.1029-2_amd64.deb && \  
odbcinst -i -d -f /opt/cloudera/impalaodbc/Setup/odbcinst.ini  
  
# Install Spark  
RUN cd /tmp && \  
wget -q
https://archive.apache.org/dist/spark/spark-${APACHE_SPARK_VERSION}/spark-${APACHE_SPARK_VERSION}-bin-
hadoop${HADOOP_VERSION}.tgz && \  
tar xzf spark-${APACHE_SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz -C
/usr/local && \  
rm spark-${APACHE_SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz  
  
RUN cd /usr/local && ln -s spark-${APACHE_SPARK_VERSION}-bin-
hadoop${HADOOP_VERSION} spark  
  
# Mesos dependencies  
RUN DISTRO=debian && \  
CODENAME=stretch && \  
echo "deb http://repos.mesosphere.io/${DISTRO} ${CODENAME} main" >
/etc/apt/sources.list.d/mesosphere.list && \  
apt-get -y update && \  
apt-get --no-install-recommends -y --force-yes install mesos=1.3.1-2.0.1 && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Spark and Mesos config  
ENV SPARK_HOME /usr/local/spark  
ENV MESOS_NATIVE_LIBRARY /usr/local/lib/libmesos.so  
ENV SPARK_OPTS --driver-java-options=-Xms1024M --driver-java-options=-Xmx4096M
--driver-java-options=-Dlog4j.logLevel=info  
  
RUN R -e "install.packages('sparklyr', repos='http://cran.rstudio.com/',
dependencies=T)"  
  
# Install Saagie's RStudio Addin  
RUN R -e "install.packages('devtools')" && \  
R -e "devtools::install_github('saagie/rstudio-saagie-addin')"  
  
# Install R packages  
RUN R CMD javareconf && R -e "install.packages('rJava')"  
RUN R -e "install.packages('odbc')"  
RUN R -e "install.packages('RJDBC')"  
RUN R -e "install.packages('implyr')"  
RUN R -e "install.packages('futile.logger')"  
RUN R -e "install.packages('h2o')"  
RUN R -e "install.packages('caret')"  
RUN R -e "install.packages('ROSE')"  
RUN R -e "install.packages('caretEnsemble')"  
RUN R -e "install.packages('randomForest')"  
RUN R -e "install.packages('pROC')"  
RUN R -e "install.packages('rsparkling')"  
RUN R -e "install.packages('xts')"  
RUN R -e "install.packages('dygraphs')"  
RUN R -e "install.packages('forecast')"  
RUN R -e "install.packages('mclust')"  
RUN R -e "install.packages('factoextra')"  
RUN R -e "install.packages('dbscan')"  
RUN R -e "install.packages('dtw')"  
RUN R -e "install.packages('ROCR')"  
RUN R -e "install.packages('rtsne')"  
RUN R -e "install.packages('corrplot')"  
RUN R -e "install.packages('dummies')"  
RUN R -e "install.packages('xgboost')"  
RUN R -e "install.packages('e1071')"  
RUN R -e "install.packages('DescTools')"  
RUN R -e "install.packages('packrat')"  
RUN R -e "install.packages('tm')"  
RUN R -e "install.packages('RTextTools')"  
RUN R -e "install.packages('networkD3')"  
RUN R -e "install.packages('sqldf')"  
RUN R -e "install.packages('syuzhet')"  
RUN R -e "install.packages('TSclust')"  
RUN R -e "install.packages('arules')"  
RUN R -e "install.packages('arulesSequences')"  
RUN R -e "install.packages('recommenderlab')"  
RUN R -e "install.packages('AUC')"  
RUN R -e "install.packages('kohonen')"  
RUN R -e "install.packages('topicmodels')"  
RUN R -e "install.packages('argparse')"  
RUN R -e "install.packages('lsa')"  
RUN R -e "install.packages('d3heatmap')"  
RUN R -e "install.packages('pvclust')"  
RUN R -e "install.packages('trend')"  
RUN R -e "install.packages('breakpoint')"  
RUN R -e "install.packages('changepoint')"  
RUN R -e "install.packages('mvoutlier')"  
RUN R -e "install.packages('shinydashboard')"  
RUN R -e "install.packages('FNN')"  
RUN R -e "install.packages('plotly')"  
  
# Be sure rstudio user has full access to his home directory  
RUN mkdir -p /home/rstudio && \  
chown -R rstudio:rstudio /home/rstudio && \  
chmod -R 755 /home/rstudio  
  
ADD ./init_rstudio.sh /  
RUN chmod 500 /init_rstudio.sh  
  
CMD ["/bin/sh", "-c", "/init_rstudio.sh"]  

