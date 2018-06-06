FROM centos:7.3.1611  
RUN yum -y install epel-release gcc openssl-devel bzip2-devel make; yum clean
all  
RUN yum -y install python-pip; yum clean all && pip install --upgrade pip
numpy scipy pandas scikit-learn tensorflow keras  
RUN yum -y install java-1.8.0-openjdk; yum clean all  
RUN curl -s http://apache.crihan.fr/dist/spark/spark-2.3.0/spark-2.3.0-bin-
hadoop2.7.tgz | tar xz -C /opt  
RUN ln -s /opt/spark-2.3.0-bin-hadoop2.7 /opt/spark  
RUN curl -s https://www.python.org/ftp/python/3.6.4/Python-3.6.4.tgz | tar xz
-C /usr/src  
RUN /usr/src/Python-3.6.4/configure --enable-optimizations  
RUN make altinstall /usr/src/Python-3.6.4  
WORKDIR /opt/spark  
RUN cp /opt/spark/conf/spark-defaults.conf.template /opt/spark/conf/spark-
defaults.conf  
RUN echo
'spark.driver.extraJavaOptions=-Dhttp.proxyHost=http://proxy.lbs.alcatel-
lucent.com -Dhttp.proxyPort=8000 -Dhttps.proxyHost=http://proxy.lbs.alcatel-
lucent.com -Dhttps.proxyPort=8000' >> /opt/spark/conf/spark-defaults.conf  
RUN echo 'spark.ui.reverseProxy true' >> /opt/spark/conf/spark-defaults.conf  

