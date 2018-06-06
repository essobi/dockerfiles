  
###########################################  
# Spark & python for Data analytics course  
# Last update: 9th February, 2017  
FROM jupyter/all-spark-notebook:228ae7a44e0c  
MAINTAINER "Paolo D'Onorio De Meo <p.donoriodemeo@cineca.it>"  
###########################################  
# MAPREDUCE RELATED  
USER root  
  
# install dev tools  
RUN apt-get update && apt-get upgrade -y && apt-get update && \  
apt-get install -y \  
wget axel curl \  
tar sudo openssh-server openssh-client rsync \  
openjdk-7-jdk libyaml-dev \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# hadoop  
ENV APACHE http://www.eu.apache.org  
ENV HADOOP_VERSION hadoop-2.6.5  
ENV HD "$APACHE/dist/hadoop/common/$HADOOP_VERSION/$HADOOP_VERSION.tar.gz"  
WORKDIR /tmp  
RUN axel -a -n 8 $HD \  
&& tar xzvf $HADOOP_VERSION.tar.gz -C /usr/local/ \  
&& rm -rf /tmp/* \  
&& cd /usr/local && ln -s ./$HADOOP_VERSION hadoop  
ENV HADOOP_PREFIX /usr/local/hadoop  
  
RUN mkdir -p /usr/java \  
&& ln -s /usr/lib/jvm/java-7-openjdk-amd64 /usr/java/default  
ENV JAVA_HOME /usr/java/default/  
ENV PATH $PATH:$JAVA_HOME/bin  
  
RUN sed -i '/^export JAVA_HOME/ s:.*:export
JAVA_HOME=/usr/java/default\nexport HADOOP_PREFIX=/usr/local/hadoop\nexport
HADOOP_HOME=/usr/local/hadoop\n:' $HADOOP_PREFIX/etc/hadoop/hadoop-env.sh \  
&& sed -i '/^export HADOOP_CONF_DIR/ s:.*:export
HADOOP_CONF_DIR=/usr/local/hadoop/etc/hadoop/:'
$HADOOP_PREFIX/etc/hadoop/hadoop-env.sh \  
&& . $HADOOP_PREFIX/etc/hadoop/hadoop-env.sh  
  
RUN mkdir $HADOOP_PREFIX/input \  
&& cp $HADOOP_PREFIX/etc/hadoop/*.xml $HADOOP_PREFIX/input  
  
# passwordless ssh  
RUN rm -f /etc/ssh/ssh_host_dsa_key /etc/ssh/ssh_host_rsa_key
/root/.ssh/id_rsa  
RUN ssh-keygen -q -N "" -t dsa -f /etc/ssh/ssh_host_dsa_key  
RUN ssh-keygen -q -N "" -t rsa -f /etc/ssh/ssh_host_rsa_key  
RUN ssh-keygen -q -N "" -t rsa -f /root/.ssh/id_rsa  
RUN cp /root/.ssh/id_rsa.pub /root/.ssh/authorized_keys  
ADD ssh_config /root/.ssh/config  
RUN chmod 600 /root/.ssh/config && chown root:root /root/.ssh/config  
  
# pseudo distributed  
ADD core-site.xml.template $HADOOP_PREFIX/etc/hadoop/core-site.xml.template  
RUN sed s/HOSTNAME/localhost/ \  
/usr/local/hadoop/etc/hadoop/core-site.xml.template \  
> /usr/local/hadoop/etc/hadoop/core-site.xml  
ADD hdfs-site.xml $HADOOP_PREFIX/etc/hadoop/hdfs-site.xml  
ADD mapred-site.xml $HADOOP_PREFIX/etc/hadoop/mapred-site.xml  
ADD yarn-site.xml $HADOOP_PREFIX/etc/hadoop/yarn-site.xml  
  
## workingaround docker.io build error  
RUN chmod +x /usr/local/hadoop/etc/hadoop/*-env.sh  
  
# Reformat namenode  
RUN $HADOOP_PREFIX/bin/hdfs namenode -format  
  
###########################################  
# # Spark  
# ENV SPARK_VERSION spark-1.5.2  
# ENV SPARK_HADOOP_VERSION hadoop2.6  
# ENV SPARK_BIN "$SPARK_VERSION-bin-$SPARK_HADOOP_VERSION"  
# ENV SPARK_URL "$APACHE/dist/spark/$SPARK_VERSION/$SPARK_BIN.tgz"  
# RUN axel -a -n 16 $SPARK_URL \  
# && tar xvzf $SPARK_BIN.tgz -C /usr/local/ \  
# && rm *.tgz && cd /usr/local && ln -s $SPARK_BIN spark  
# ENV SPARK_HOME /usr/local/spark  
# hadoop bootstrap  
ADD bootstrap.sh /etc/bootstrap.sh  
RUN chown root:root /etc/bootstrap.sh  
RUN chmod 700 /etc/bootstrap.sh  
ENV BOOTSTRAP /etc/bootstrap.sh  
# fixing the libhadoop.so like a boss  
RUN rm /usr/local/hadoop/lib/native/*  
RUN curl -Ls http://dl.bintray.com/sequenceiq/sequenceiq-bin/hadoop-
native-64-2.6.0.tar|tar -x -C /usr/local/hadoop/lib/native/  
# fix the 254 error code  
RUN sed -i "/^[^#]*UsePAM/ s/.*/#&/" /etc/ssh/sshd_config  
RUN echo "UsePAM no" >> /etc/ssh/sshd_config  
RUN echo "Port 2122" >> /etc/ssh/sshd_config  
  
# HDFS with spark libs  
ENV PATH $PATH:$HADOOP_PREFIX/bin  
RUN service ssh start \  
&& $HADOOP_PREFIX/etc/hadoop/hadoop-env.sh \  
&& $HADOOP_PREFIX/sbin/start-dfs.sh \  
&& hdfs dfs -mkdir -p /user/root \  
&& hdfs dfs -put $HADOOP_PREFIX/etc/hadoop/ input \  
# && hdfs dfs -put $SPARK_HOME/lib /spark \  
&& hadoop fs -mkdir -p /tmp \  
&& hadoop fs -chown -R $NB_USER:$NB_USER /tmp \  
&& hadoop fs -mkdir -p /user/$NB_USER \  
&& hadoop fs -chown -R $NB_USER:$NB_USER /user/$NB_USER  
  
###################################  
# JUPYTER RELATED  
# Dependencies  
RUN chown jovyan /opt  
# Main notebook user  
USER jovyan  
# install libs  
RUN pip install --upgrade pip \  
plumbum jinja2 tweepy version_information \  
# Add mrjob from Yelp  
git+https://github.com/Yelp/mrjob  
  
###################################  
# Update anaconda  
RUN echo "Update conda package" \  
# && conda remove -y nbpresent \  
&& conda install -y -c damianavila82 rise \  
&& conda install -y -c pydy version_information \  
&& conda clean -y --all  
  
# ###############################  
# WORKDIR /opt  
# # Install and not remove from installation!  
# RUN git clone https://github.com/Yelp/mrjob  
# && cd mrjob && pip install -e .  
# ###############################  
# Note:  
# IPython.external.mathjax is deprecated, Mathjax is now installed by default
with the notebook package  
# # Add offline use of mathjax  
# RUN wget -q https://github.com/mathjax/MathJax/archive/2.5.3.zip \  
# && python -m IPython.external.mathjax 2.5.3.zip \  
# && rm *.zip  
# # RUN python3 -m IPython.external.mathjax  
# ###############################  
# # Live slideshows  
# RUN wget -q https://github.com/pdonorio/RISE/archive/master.tar.gz \  
# && tar xvzf *.gz && cd *master && \  
# python setup.py install && rm -rf *.gz  
###############################  
# New bootstrap?  
ADD boot-all.sh /usr/bin/booter  
CMD ["booter"]  
  
###############################  
# Environment variables  
ADD env.sh /tmp/env.sh  
RUN echo ". /tmp/env.sh" >> /home/$NB_USER/.bashrc  
USER root  
  
###############################  
# mrjob fix  
ADD mrjob.conf /etc/mrjob.conf  
WORKDIR /data  
  
###############################  
# Extra spark libs  
COPY jars/*.jar /usr/local/spark/extensions/  
COPY jars/spark-defaults.conf /usr/local/spark/conf/  
  
###############################  
# The end  

