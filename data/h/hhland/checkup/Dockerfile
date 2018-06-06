FROM java:8  
ENV P_HOME /d/program  
ENV APACHE_HOME /d/program/apache  
RUN mkdir -p $APACHE_HOME && mkdir $P_HOME/R && mkdir /d/download && mkdir
/d/git && mkdir /d/notebook  
  
RUN apt-get update && apt-get install -y g++ cmake gfortran xpdf libbz2-dev
libgdbm-dev liblzma-dev libreadline-dev libsqlite3-dev libssl-dev tcl-dev tk-
dev dpkg-dev wget git subversion vim ssh  
  
WORKDIR /d/download  
  
#clojure  
RUN wget
http://repo1.maven.org/maven2/org/clojure/clojure/1.6.0/clojure-1.6.0.zip &&
unzip clojure-1.6.0 && mv clojure-1.6.0 $P_HOME  
ENV CLOJURE_HOME $APACHE_HOME/clojure-1.6.0  
#scala  
RUN wget http://downloads.typesafe.com/scala/2.11.4/scala-2.11.4.tgz && tar
-xvf scala-2.11.4.tgz && mv scala-2.11.4 $P_HOME  
ENV SCALA_HOME $APACHE_HOME/scala-2.11.4  
#maven  
RUN wget http://mirror.bit.edu.cn/apache/maven/maven-3/3.2.3/binaries/apache-
maven-3.2.3-bin.tar.gz && tar -xvf apache-maven-3.2.3-bin.tar.gz && mv apache-
maven-3.2.3 $APACHE_HOME  
ENV MVN_HOME $APACHE_HOME/apache-maven-3.2.3  
#ant  
RUN wget http://mirrors.cnnic.cn/apache/ant/binaries/apache-
ant-1.9.4-bin.tar.gz && tar -xvf apache-ant-1.9.4-bin.tar.gz && mv apache-
ant-1.9.4 $APACHE_HOME  
ENV ANT_HOME $APACHE/apache-ant-1.9.4  
#python  
RUN wget https://www.python.org/ftp/python/2.7.8/Python-2.7.8.tgz && tar -xvf
Python-2.7.8.tgz && mv Python-2.7.8 $P_HOME && cd $P_HOME/Python-2.7.8 &&
./configure && make && make install && cd -  
RUN wget https://bootstrap.pypa.io/ez_setup.py -O - | python && easy_install
pip && pip install ipython[all]  
  
ENV PATH $PATH:$ANT_MOME/bin:$MVN_HOME/bin:$SCALA_HOME/bin:$CLOJURE_HOME/bin  
  
WORKDIR /d  
  
EXPOSE 8888  
CMD ipython notebook --ip 0.0.0.0 --notebook-dir /d/notebook  

