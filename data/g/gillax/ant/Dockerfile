From java:8  
ENV ANT_VERSION 1.9.6  
ENV ANT_HOME /opt/ant  
ENV PATH ${PATH}:${ANT_HOME}/bin  
  
RUN wget -q http://archive.apache.org/dist/ant/binaries/apache-
ant-${ANT_VERSION}-bin.tar.gz \  
&& tar -xzf apache-ant-${ANT_VERSION}-bin.tar.gz \  
&& mv apache-ant-${ANT_VERSION} ${ANT_HOME} \  
&& rm apache-ant-${ANT_VERSION}-bin.tar.gz  

