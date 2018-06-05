FROM sunithar/oracle-java8  
  
LABEL description="Install Ant"  
  
ARG ANT_DOWNLOAD_URI=http://archive.apache.org/dist/ant/binaries/  
  
  
ENV DEBIAN_FRONTEND noninteractive  
  
ENV ANT_VERSION 1.9.6  
RUN cd \  
&& wget -q ${ANT_DOWNLOAD_URI}apache-ant-${ANT_VERSION}-bin.tar.gz \  
&& tar -xzf apache-ant-${ANT_VERSION}-bin.tar.gz \  
&& mv apache-ant-${ANT_VERSION} /opt/ant \  
&& rm -v apache-ant-${ANT_VERSION}-bin.tar.gz  
  
ENV ANT_HOME /opt/ant  
ENV PATH ${PATH}:/opt/ant/bin  
  
CMD ["/bin/bash"]  
  

