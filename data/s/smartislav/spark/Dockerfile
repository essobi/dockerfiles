FROM openjdk:8u121  
  
ARG MESOS_VERSION=1.5.0  
  
RUN touch /usr/local/bin/systemctl && chmod +x /usr/local/bin/systemctl  
  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 \--recv E56151BF \  
&& echo "deb http://repos.mesosphere.io/debian jessie main" >
/etc/apt/sources.list.d/mesosphere.list \  
&& apt-get -y update \  
&& apt-get -y install --no-install-recommends "mesos=${MESOS_VERSION}*" wget
libcurl3-nss \  
&& apt-get -y install libatlas3-base libopenblas-base \  
&& update-alternatives --set libblas.so.3 /usr/lib/openblas-base/libblas.so.3
\  
&& update-alternatives --set liblapack.so.3 /usr/lib/openblas-
base/liblapack.so.3 \  
&& ln -sfT /usr/lib/libblas.so.3 /usr/lib/libblas.so \  
&& ln -sfT /usr/lib/liblapack.so.3 /usr/lib/liblapack.so \  
&& wget http://apache.cs.uu.nl/spark/spark-2.3.0/spark-2.3.0-bin-hadoop2.7.tgz
-O /tmp/spark.tgz \  
&& echo
"258683885383480ba01485d6c6f7dc7cfd559c1584d6ceb7a3bbcf484287f7f57272278568f16227be46b4f92591768ba3d164420d87014a136bf66280508b46
/tmp/spark.tgz" | sha512sum -c \- \  
&& mkdir /spark \  
&& tar zxf /tmp/spark.tgz -C /spark --strip-components 1 \  
&& apt-get remove -y wget \  
&& apt-get clean -y \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& ldconfig  
  
ENV PATH=/spark/bin:$PATH  
  
CMD "spark-submit.sh"  

