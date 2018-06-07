FROM java:8  
MAINTAINER Aaron Glahe <aarongmldt@gmail.com>  
  
# Setup env  
USER root  
  
# Download ant, hadoop & joshua decoder:  
RUN wget -q -O - http://archive.apache.org/dist/ant/binaries/apache-
ant-1.9.6-bin.tar.gz | tar -xzf - -C /usr/local  
RUN ln -s /usr/local/apache-ant-1.9.6 /usr/local/ant  
ENV ANT_HOME /usr/local/ant  
  
RUN wget -q -O -
http://apache.mirrors.pair.com/hadoop/common/hadoop-2.7.1/hadoop-2.7.1.tar.gz
| tar -xzf - -C /usr/local  
RUN ln -s /usr/local/hadoop-2.7.1 /usr/local/hadoop  
ENV HADOOP /usr/local/hadoop  
  
RUN wget -q -O - http://cs.jhu.edu/~post/files/joshua-6.0.5.tgz | tar -xzf -
-C /usr/local  
RUN ln -s /usr/local/joshua-6.0.5 /usr/local/joshua  
ENV JOSHUA /usr/local/joshua  
  
# Install other build dependencies:  
RUN \  
apt-get update && \  
apt-get install -y \  
cmake=3.0.2-1 \  
gcc=4:4.9.2-2 \  
g++=4:4.9.2-2 \  
libboost-all-dev=1.55.0.2 \  
make=4.0-8.1 \  
zlib1g-dev=1:1.2.8.dfsg-2+b1  
  
WORKDIR /usr/local/joshua  
RUN ${ANT_HOME}/bin/ant  
  
#Ports:  
EXPOSE 5674  
RUN wget -q -O - http://cs.jhu.edu/~post/language-packs/language-pack-ar-en-
phrase-2015-03-18.tgz | tar -xzf - -C /usr/local  
WORKDIR /usr/local/language-pack-ar-en-phrase-2015-03-18  
CMD ["./run-joshua.sh"]  

