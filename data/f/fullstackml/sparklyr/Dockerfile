FROM kaggle/rstats:latest  
MAINTAINER Dmitry Petrov <dmitry@fullstackml.com>  
  
LABEL com.fullstackml = "true" \  
com.fullstackml.function = "sparklyr" \  
com.fullstackml.version = "0.01"  
  
RUN wget http://d3kbcqa49mib13.cloudfront.net/spark-2.0.0-bin-hadoop2.7.tgz
2>/dev/null && \  
tar zxf spark-2.0.0-bin-hadoop2.7.tgz -C /usr/local/ && \  
rm spark-2.0.0-bin-hadoop2.7.tgz && \  
(cd /usr/local && ln -s spark-2.0.0-bin-hadoop2.7 spark) && \  
R -e 'install.packages("devtools")' && \  
R -e 'devtools::install_github("rstudio/sparklyr")'  
#ENV SPARK_HOME /usr/local/spark  

