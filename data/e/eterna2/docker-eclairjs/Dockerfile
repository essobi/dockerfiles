FROM sequenceiq/spark:1.6.0  
MAINTAINER eterna2 <eterna2@hotmail.com>  
  
# Update to jdk8 (required for nashorn)  
RUN curl -LO http://download.oracle.com/otn-
pub/java/jdk/8u91-b14/jdk-8u91-linux-x64.rpm \  
-H 'Cookie: oraclelicense=accept-securebackup-cookie'  
RUN rpm -i jdk-8u91-linux-x64.rpm  
RUN rm jdk-8u91-linux-x64.rpm  
  
ENV JAVA_HOME /usr/java/default  
ENV PATH $PATH:$JAVA_HOME/bin  
RUN rm /usr/bin/java && ln -s $JAVA_HOME/bin/java /usr/bin/java  
  
# maven  
RUN curl -s http://www-eu.apache.org/dist/maven/maven-3/3.3.9/binaries/apache-
maven-3.3.9-bin.tar.gz | \  
tar -xz -C /usr/local/  
RUN cd /usr/local && ln -s apache-maven-3.3.9 maven  
ENV MAVEN_HOME /usr/local/maven  
ENV PATH $PATH:$MAVEN_HOME/bin  
  
# eclairJS nashorn  
RUN curl -s https://codeload.github.com/EclairJS/eclairjs-nashorn/tar.gz/v0.5
| \  
tar -xz -C /usr/local/  
RUN cd /usr/local && ln -s eclairjs-nashorn-0.5 nashorn  
  
# install conda  
RUN curl -O
https://repo.continuum.io/miniconda/Miniconda2-4.0.5-Linux-x86_64.sh && \  
/bin/bash Miniconda2-4.0.5-Linux-x86_64.sh -b -p /usr/local/conda && \  
rm Miniconda2-4.0.5-Linux-x86_64.sh  
ENV PATH /usr/local/conda/bin:$PATH  
  
# Toree  
RUN pip install toree==0.1.0.dev7  
  
# Jupyter  
RUN conda install -y jupyter  
  
# eclairJS nashorn  
RUN cd /usr/local/nashorn && mvn -Dmaven.test.skip=true package -Pnotebook  
RUN sed -i 's/<path to spark-kernel distribution>\/bin\/spark-
kernel/\/usr\/local\/conda\/lib\/python2.7\/site-
packages\/toree\/bin\/run.sh/g; s/<path to nashorn
jar>/\/usr\/local\/eclairjs-nashorn-0.5\/target\/eclairjs-nashorn-0.5-jar-
with-dependencies.jar/g; s/<path to spark 1.6.0
distribution>/\/usr\/local\/spark/g;' /usr/local/nashorn/kernel.json  
RUN mkdir -p /.local/share/jupyter/kernels/eclair && cp
/usr/local/nashorn/kernel.json /.local/share/jupyter/kernels/eclair  
  
WORKDIR /.jsNotebook  
EXPOSE 8888  
CMD ["jupyter","notebook", "--no-browser", "--ip", "0.0.0.0"]  

