FROM poad/docker-jupyter-notebook-pyspark-amazon:latest  
MAINTAINER Kenji Saito  
  
ENV SBT_VERSION 1.1.1  
ENV SCALA_VERSION 2.12.5  
ENV SBT_HOME /usr/local/sbt  
ENV PATH ${PATH}:${SBT_HOME}/bin  
  
# Install sbt  
RUN curl -sL
"https://github.com/sbt/sbt/releases/download/v${SBT_VERSION}/sbt-${SBT_VERSION}.tgz"
| tar -xz -C /usr/local  
  
RUN curl -sL "https://github.com/jupyter-scala/jupyter-
scala/archive/v0.4.2.tar.gz" | tar -xz -C /usr/local && \  
cd /usr/local/ && \  
ln -s jupyter-scala-0.4.2 jupyter-scala && \  
cd jupyter-scala && \  
sbt publishLocal  
  
RUN curl -sL "https://github.com/jupyter-scala/jupyter-
kernel/archive/v0.4.1.tar.gz" | tar -xz -C /usr/local &&\  
cd /usr/local/ && \  
ln -s jupyter-kernel-0.4.1 jupyter-kernel && \  
cd jupyter-kernel && \  
sbt publishLocal  
  
RUN curl -sL "https://raw.githubusercontent.com/alexarchambault/jupyter-
scala/master/jupyter-scala" -o /root/jupyter-scala.sh && \  
chmod 744 /root/jupyter-scala.sh && \  
sed -e "s/2.11.11/${SCALA_VERSION}/gi" /root/jupyter-scala.sh && \  
/root/jupyter-scala.sh && \  
rm -f /root/jupyter-scala.sh  
  
RUN pip install
https://dist.apache.org/repos/dist/dev/incubator/toree/0.2.0-incubating-
rc3/toree-pip/toree-0.2.0.tar.gz && \  
jupyter toree install  
  
WORKDIR /root  
  
COPY bootstrap.sh /etc/bootstrap.sh  
  
RUN chown root.root /etc/bootstrap.sh  
RUN chmod 700 /etc/bootstrap.sh  
  
EXPOSE 18080 7077 8888  
ENTRYPOINT ["/etc/bootstrap.sh"]  
CMD ["lab"]  
  

