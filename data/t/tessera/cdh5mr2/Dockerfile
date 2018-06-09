FROM ubuntu:12.04  
MAINTAINER "Ryan Hafen" rhafen@gmail.com  
  
# fix bash bug  
RUN apt-get update -q -q && apt-get dist-upgrade --yes --force-yes  
  
# install sudo  
RUN apt-get update -q -q \  
&& apt-get install -y sudo vim wget curl git ant maven  
  
RUN su -c "useradd tessera -s /bin/bash -m" \  
&& echo "tessera:tessera" | chpasswd  
  
## Add Cloudera repositories  
RUN wget -c http://archive.cloudera.com/cdh5/one-click-
install/precise/amd64/cdh5-repository_1.0_all.deb \  
&& dpkg -i cdh5-repository_1.0_all.deb \  
&& curl -s
http://archive.cloudera.com/cdh5/ubuntu/precise/amd64/cdh/archive.key | apt-
key add -  
  
## Install Java  
RUN apt-get update -q -q \  
&& apt-get install -y openjdk-7-jdk  
  
## Install Hadoop with YARN  
RUN apt-get install -y hadoop-conf-pseudo \  
&& dpkg -L hadoop-conf-pseudo \  
&& sudo -u hdfs hdfs namenode -format \  
&& for x in `cd /etc/init.d ; ls hadoop-hdfs-*` ; do service $x start ; done \  
&& sudo -u hdfs hadoop fs -mkdir -p /tmp/hadoop-
yarn/staging/history/done_intermediate \  
&& sudo -u hdfs hadoop fs -chown -R mapred:mapred /tmp/hadoop-yarn/staging \  
&& sudo -u hdfs hadoop fs -chmod -R 1777 /tmp \  
&& sudo -u hdfs hadoop fs -mkdir -p /var/log/hadoop-yarn \  
&& sudo -u hdfs hadoop fs -chown yarn:mapred /var/log/hadoop-yarn \  
&& service hadoop-yarn-resourcemanager start \  
&& service hadoop-yarn-nodemanager start \  
&& service hadoop-mapreduce-historyserver start \  
&& sudo -u hdfs hadoop fs -mkdir /user \  
&& sudo -u hdfs hadoop fs -chown tessera /user \  
&& sudo -u hdfs hadoop fs -mkdir /user/tessera \  
&& sudo -u hdfs hadoop fs -chown tessera /user/tessera \  
&& rm cdh5-repository*  
# && sudo apt-get install -y hive-server2  
###########  
RUN touch /home/tessera/.Renviron \  
&& echo 'HADOOP=/usr/lib/hadoop' | tee -a /home/tessera/.Renviron \  
&& echo 'HADOOP_HOME=/usr/lib/hadoop' | tee -a /home/tessera/.Renviron \  
&& echo 'HADOOP_CONF_DIR=/etc/hadoop/conf' | tee -a /home/tessera/.Renviron \  
&& echo 'HADOOP_BIN=$HADOOP_HOME/bin' | tee -a /home/tessera/.Renviron \  
&& echo 'HADOOP_OPTS=-Djava.awt.headless=true' | tee -a
/home/tessera/.Renviron \  
&& echo
'HADOOP_LIBS=/etc/hadoop/conf:/usr/lib/hadoop/lib/:/usr/lib/hadoop/.//:/usr/lib/hadoop-
hdfs/./:/usr/lib/hadoop-hdfs/lib/:/usr/lib/hadoop-hdfs/.//:/usr/lib/hadoop-
yarn/lib/:/usr/lib/hadoop-yarn/.//:/usr/lib/hadoop-
mapreduce/lib/:/usr/lib/hadoop-mapreduce/.//' | tee -a /home/tessera/.Renviron
\  
&& echo 'LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH' | tee -a
/home/tessera/.Renviron \  
&& echo 'RHIPE_RUNNER=/home/tessera/rhRunner.sh' | tee -a
/home/tessera/.Renviron \  
&& echo 'JAVA_HOME=/usr/lib/jvm/java-7-openjdk-amd64' | tee -a
/home/tessera/.Renviron \  
&& echo export 'HADOOP=/usr/lib/hadoop' | tee -a /etc/profile \  
&& echo export 'HADOOP_HOME=/usr/lib/hadoop' | tee -a \  
&& echo export 'HADOOP_CONF_DIR=/etc/hadoop/conf' | tee -a /etc/profile \  
&& echo export 'HADOOP_BIN=$HADOOP_HOME/bin' | tee -a /etc/profile \  
&& echo export 'HADOOP_OPTS=-Djava.awt.headless=true' | tee -a /etc/profile \  
&& echo export
'HADOOP_LIBS=/etc/hadoop/conf:/usr/lib/hadoop/lib/:/usr/lib/hadoop/.//:/usr/lib/hadoop-
hdfs/./:/usr/lib/hadoop-hdfs/lib/:/usr/lib/hadoop-hdfs/.//:/usr/lib/hadoop-
yarn/lib/:/usr/lib/hadoop-yarn/.//:/usr/lib/hadoop-
mapreduce/lib/:/usr/lib/hadoop-mapreduce/.//' | tee -a /etc/profile \  
&& echo export 'LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH' | tee -a
/etc/profile \  
&& echo export 'RHIPE_RUNNER=/home/tessera/rhRunner.sh' | tee -a /etc/profile
\  
&& echo export 'JAVA_HOME=/usr/lib/jvm/java-7-openjdk-amd64' | tee -a
/etc/profile  
  
RUN chown -R tessera:tessera /home/tessera  
  
ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64  
  
RUN echo '/usr/lib/jvm/java-7-openjdk-amd64/jre/lib/amd64/server/' | tee -a
/etc/ld.so.conf.d/jre.conf \  
&& echo '/usr/lib/jvm/java-7-openjdk-amd64/jre/lib/amd64/' | tee -a
/etc/ld.so.conf.d/jre.conf \  
&& echo '/usr/lib/hadoop/lib' | tee -a /etc/ld.so.conf.d/hadoop.conf  
  
## build/install R  
RUN apt-get -y update \  
&& apt-get -y install pkg-config unzip libcairo2-dev libcurl4-openssl-dev
screen libssl0.9.8 gdebi-core firefox libapparmor1 psmisc supervisor  
  
RUN echo "deb http://cran.rstudio.com/bin/linux/ubuntu precise/" | tee -a
/etc/apt/sources.list \  
&& apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys E084DAB9
\  
&& apt-get -y update \  
&& apt-get install -y r-base-dev \  
&& chmod -R aou=rwx /usr/local/lib/R/site-library  
  
RUN R CMD javareconf  
  
USER tessera  
  
## rJava package  
RUN R -e "install.packages('rJava', repos='http://www.rforge.net/')"  
  
## shiny package  
RUN R -e "install.packages('shiny', repos='http://cran.rstudio.com/')"  
  
USER root  
  
## rstudio  
RUN update-locale  
  
RUN wget -q https://s3.amazonaws.com/rstudio-server/current.ver -O
currentVersion.txt \  
&& ver=$(cat currentVersion.txt) \  
&& wget http://download2.rstudio.org/rstudio-server-${ver}-amd64.deb \  
&& dpkg -i rstudio-server-${ver}-amd64.deb \  
&& rm rstudio-server-*-amd64.deb currentVersion.txt \  
&& echo "www-port=80" | tee -a /etc/rstudio/rserver.conf \  
&& echo "rsession-ld-library-path=/usr/local/lib" | tee -a
/etc/rstudio/rserver.conf \  
&& rstudio-server restart  
  
## shiny server  
RUN ver=$(wget -qO- https://s3.amazonaws.com/rstudio-shiny-server-os-
build/ubuntu-12.04/x86_64/VERSION) \  
&& wget https://s3.amazonaws.com/rstudio-shiny-server-os-
build/ubuntu-12.04/x86_64/shiny-server-${ver}-amd64.deb -O shiny-server.deb \  
&& dpkg -i shiny-server.deb \  
&& rm shiny-server.deb \  
&& mkdir /srv/shiny-server/examples \  
&& cp -R /usr/local/lib/R/site-library/shiny/examples/* /srv/shiny-
server/examples \  
&& chown -R shiny:shiny /srv/shiny-server/examples \  
&& echo "tessera ALL=(ALL) NOPASSWD: /bin/chown -R shiny /srv/shiny-server" |
tee -a /etc/sudoers  
  
## protobuf  
RUN export PROTO_BUF_VERSION=2.5.0 \  
&& wget
https://protobuf.googlecode.com/files/protobuf-$PROTO_BUF_VERSION.tar.bz2 \  
&& tar jxvf protobuf-$PROTO_BUF_VERSION.tar.bz2 \  
&& cd protobuf-$PROTO_BUF_VERSION \  
&& ./configure && make -j4 \  
&& make install \  
&& cd .. \  
&& rm -rf protobuf-*  
  
## RHIPE  
USER tessera  
  
RUN cd /home/tessera \  
&& export RHIPE_VERSION=Rhipe_0.75.0_cdh5mr2 \  
&& export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH \  
&& export PKG_CONFIG_PATH=/usr/local/lib \  
&& wget http://ml.stat.purdue.edu/rhipebin/$RHIPE_VERSION.tar.gz \  
&& R CMD INSTALL $RHIPE_VERSION.tar.gz \  
&& rm $RHIPE_VERSION.tar.gz \  
&& echo "export LD_LIBRARY_PATH=/usr/local/lib" | tee -a
/home/tessera/rhRunner.sh \  
&& echo "exec /usr/bin/R CMD /usr/local/lib/R/site-
library/Rhipe/bin/RhipeMapReduce --slave --silent --vanilla" | tee -a
/home/tessera/rhRunner.sh \  
&& chown -R tessera:tessera /home/tessera \  
&& chmod 755 /home/tessera \  
&& chmod 755 /home/tessera/rhRunner.sh  
  
## do initial downloading of maven artifacts  
RUN cd /home/tessera  
&& git clone --depth=50 \--recursive --branch=dev
git://github.com/hafen/RHIPE.git  
&& cd RHIPE  
&& rm -rf /home/tessera/.m2  
&& mvn package --fail-never  
&& cd ..  
&& rm -rf RHIPE  
  
## more packages  
RUN R -e "install.packages('devtools', repos='http://cran.rstudio.com/')" \  
&& R -e "options(unzip = 'unzip', repos = 'http://cran.rstudio.com/');
library(devtools); install_github('tesseradata/datadr')" \  
&& R -e "options(unzip = 'unzip', repos = 'http://cran.rstudio.com/');
library(devtools); install_github('tesseradata/trelliscope')" \  
&& R -e "install.packages('testthat', repos='http://cran.rstudio.com/')" \  
&& R -e "install.packages('roxygen2', repos='http://cran.rstudio.com/')"  
  
USER root  
  
## Configure persistent daemons  
RUN mkdir -p /var/log/supervisor  
RUN chmod 777 /var/log/supervisor  
  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
EXPOSE 22 80 8787 8030 8031 8032 8033 8040 8042 8088 9000 50010 50020 50070
50075 50090  
## Run persistent tasks (see supervisord.conf)  
CMD ["/usr/bin/supervisord"]  
  
# docker run -d -p 80:80 test  
# boot2docker ip  

