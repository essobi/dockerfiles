FROM ubuntu:wily  
MAINTAINER Xi Shen <davidshen84@gmail.com>  
LABEL os=ubuntu:wily java=openjdk-8-jre python=python34  
  
ADD http://www-us.apache.org/dist/zeppelin/zeppelin-0.6.2/zeppelin-0.6.2-bin-
all.tgz /opt/  
RUN mkdir /opt/zeppelin && \  
tar xzf /opt/zeppelin-0.6.2-bin-all.tgz --strip-components=1 -C /opt/zeppelin
&& \  
rm /opt/zeppelin-0.6.2-bin-all.tgz  
  
ADD http://www-us.apache.org/dist/spark/spark-2.0.1/spark-2.0.1-bin-
hadoop2.7.tgz /opt  
RUN mkdir /opt/spark && \  
tar xzf /opt/spark-2.0.1-bin-hadoop2.7.tgz --strip-components=1 -C /opt/spark
&& \  
rm /opt/spark-2.0.1-bin-hadoop2.7.tgz  
  
RUN apt-get update && apt-get install -y \  
build-essential \  
gfortran \  
libblas-dev \  
liblapack-dev \  
libpng12-dev \  
libxft-dev \  
openjdk-8-jdk \  
python3-dev \  
python3-pip \  
&& rm -rf /var/lib/apt/lists/*  
  
# order matters  
RUN pip3 install --upgrade \  
numpy \  
scipy \  
scikit-learn \  
matplotlib \  
cython \  
pandas  
  
RUN locale-gen en_US.UTF-8 && \  
ln -s /usr/bin/python3 /usr/bin/python && \  
sed -e 's/backend : tkagg/backend : agg/' \  
-i '/usr/local/lib/python3.4/dist-packages/matplotlib/mpl-data/matplotlibrc'  
  
COPY opt/ /opt  
COPY root/ /root  
  
EXPOSE \  
# zeppelin.server.port  
8080 \  
# spark.ui.port  
4040\  
# spark.driver.port  
7229 \  
# spark.blockManager.port  
7717  
VOLUME ["/notebook"]  
WORKDIR /opt/zeppelin  
ENTRYPOINT ["/root/startup.sh"]  

