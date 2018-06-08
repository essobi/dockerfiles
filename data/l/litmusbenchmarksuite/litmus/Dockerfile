FROM ubuntu:16.04  
LABEL maintainer1 "yashwant.keswani@gmail.com"  
LABEL maintainer2 "harsh9t@gmail.com"  
  
# Install packages.  
RUN apt-get update && apt-get install -y \  
apt-transport-https \  
git \  
pkg-config \  
make \  
gcc-4.7 \  
build-essential g++ \  
python3 \  
software-properties-common \  
# default-jre \  
# default-jdk \  
unzip \  
wget \  
&& apt-get clean  
  
RUN apt-get -y update;  
RUN apt-get -y upgrade;  
RUN apt-get install -y linux-tools-common linux-tools-generic linux-
tools-`uname -r`  
  
RUN add-apt-repository ppa:openjdk-r/ppa  
RUN apt-get update  
RUN apt-get install -y openjdk-8-jdk  
  
#ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64  
# Install gh-rdf3x and clean up  
RUN git clone https://github.com/gh-rdf3x/gh-rdf3x.git \  
&& cd gh-rdf3x \  
&& make  
  
# Install Openlink Virtuoso  
# RUN apt-get update && apt-get install -y openssl  
# RUN git clone https://github.com/openlink/virtuoso-opensource \  
# && cd virtuoso-opensource \  
# && ./autogen.sh \  
# && ./configure \  
# && make \  
# && make install  
# Install Gremlin Groovy for sparksee  
ADD ./gremlin-groovy-2.6.0.zip ./  
RUN unzip gremlin-groovy-2.6.0.zip  
RUN mv gremlin-groovy-2.6.0 gremlin-groovy  
  
# Install Orient  
RUN wget https://orientdb.com/download.php?file=orientdb-
community-2.1.3.tar.gz  
RUN ls  
RUN tar -xf download.php?file=orientdb-community-2.1.3.tar.gz -C /  
RUN mv /orientdb-community-2.1.3 /orientdb  
  
# Install Apache Jena  
ADD ./apache-jena-3.2.0.zip /  
RUN unzip apache-jena-3.2.0.zip  
  
#Installing open link virtuoso  
RUN apt-get install -y build-essential debhelper autotools-dev autoconf
automake unzip wget net-tools git libtool flex bison gperf gawk m4 libssl-dev
libreadline-dev libreadline-dev openssl  
RUN git clone https://github.com/openlink/virtuoso-opensource.git \  
&& cd virtuoso-opensource \  
&& ./autogen.sh \  
&& ./configure \  
&& make && make install  
  
RUN apt-get install -y time  
  
RUN apt-get install -y software-properties-common  
  
RUN apt-get -y update  
  
RUN apt-get install -y libglib2.0-dev libraptor2-dev librasqal3-dev uuid-dev
libreadline-dev lib32ncurses5-dev  
RUN wget https://4store.danielknoell.de/download/4store-v1.1.5.tar.gz  
RUN tar -xf 4store-v1.1.5.tar.gz  
RUN cd 4store-v1.1.5 \  
&& ./configure \  
&& make \  
&& make install  
  
#RUN add-apt-repository -y ppa:webupd8team/java  
#RUN apt-get update  
#RUN apt-get i-y nstall oracle-java8-installer  
#RUN apt-get install oracle-java8-set-default  
RUN apt-get -y update  
RUN apt-get -y upgrade  
RUN apt-get install -y openjdk-7-jdk  
  
ADD ./apache-tinkerpop-gremlin-console-3.2.4-bin.zip ./  
RUN unzip apache-tinkerpop-gremlin-console-3.2.4-bin.zip  
RUN mv apache-tinkerpop-gremlin-console-3.2.4 gremlin-groovy-3  
  
RUN apt-get install -y python3-pandas  
RUN apt-get install -y python3-matplotlib  
  
# create directory for gh-rdf3x logs  
RUN mkdir /var/log/rdf3x  
  
# create directory for sparkee logs  
RUN mkdir /var/log/sparksee  
  
# create directory for orient logs  
RUN mkdir /var/log/orient  
  
# create directory for neo4j logs  
RUN mkdir /var/log/neo4j  
  
# create directory for monet logs  
RUN mkdir /var/log/monet  
  
# create directory for jena logs  
RUN mkdir /var/log/jena  
  
# create directory for arq logs  
RUN mkdir /var/log/arq  
  
# create directory for tinker logs  
RUN mkdir /var/log/tinker  
  
# create directory for virtuoso logs  
RUN mkdir /var/log/virtuoso  
  
# create directory for 4store logs  
RUN mkdir /var/log/4store  
  
# create directory and add data  
RUN mkdir graph_data  
ADD ./data/* /graph_data/  
  
# create a general directory for all scripts  
RUN mkdir scripts  
  
#create directory for Tinker  
RUN mkdir scripts/tinker/  
ADD ./tinker/* /scripts/tinker/  
  
#create directory for sparksee  
RUN mkdir scripts/sparksee/  
ADD ./sparksee/* /scripts/sparksee/  
  
#Create directory for rdf3x  
RUN mkdir scripts/rdf3x/  
ADD ./rdf3x/* /scripts/rdf3x/  
  
#Create directory for orient  
RUN mkdir scripts/orient/  
ADD ./orient/* /scripts/orient/  
  
#Create directory for neo4j  
RUN mkdir scripts/neo4j/  
ADD ./ne04j/* /scripts/neo4j/  
  
#Create directory for jena  
RUN mkdir scripts/jena/  
ADD ./jena/* /scripts/jena/  
  
#Create directory for 4store  
RUN mkdir scripts/4store/  
ADD ./4store/* /scripts/4store/  
  
#Create directory for tinker3  
RUN mkdir scripts/tinker3/  
ADD ./tinker3/* /scripts/tinker3/  
  
ADD ./tinker.properties ./tinker.properties  
  
#Create directory for virtuoso  
RUN mkdir scripts/virtuoso/  
ADD ./openlink/* /scripts/virtuoso/  
  
#Copy all the graph_files  
#RUN mkdir /graph_data  
ADD ./graph_data/* /graph_data/  
  
#Copy all the rdf_files  
RUN mkdir /rdf_data  
ADD ./rdf_data/* /rdf_data/  
  
#Copy all the sparql queries  
RUN pwd  
RUN mkdir /sparql_query  
ADD ./sparql_query/* /sparql_query/  
  
#Copy all the gremlin queries  
RUN mkdir /gremlin_query  
ADD ./gremlin_query/* /gremlin_query/  
  
# create folder for gremlin query for perf  
RUN mkdir /gremlin_query_perf  
  
# copying all the scripts  
#ADD ./hello_world.py ./  
RUN mkdir /virtuoso_queries  
RUN mkdir /jena_queries  
RUN mkdir /4store_queries  
RUN mkdir /rdf3x_queries  
  
#Adding plotting script here  
ADD ./plot_script.py ./  
ADD ./run_script.py ./  
  
#ADD ./orient_gremlin.sh /orientdb/bin/gremlin.sh  
#ADD ./gremlin_gremlin.sh /gremlin_groovy/bin/gremlin.sh  
#RUN chmod 777 /orientdb/bin/gremlin.sh  
#CMD python3 run_script.py  
#CMD python3 run_script.py -r -n 3 -gd /graph_data -rd /rdf_data -gq
/gremlin_query -rq /sparql_query && java -version  
#CMD ls /usr/lib/jvm/*  
#CMD java -version  
#CMD update-java-alternatives --list  

