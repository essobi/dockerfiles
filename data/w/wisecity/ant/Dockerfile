FROM java:6  
USER root  
ENV ANT_VERSION 1.9.4  
WORKDIR /tmp  
  
RUN cd && \  
wget -q http://archive.apache.org/dist/ant/binaries/apache-
ant-${ANT_VERSION}-bin.tar.gz && \  
tar -xzf apache-ant-${ANT_VERSION}-bin.tar.gz && \  
mv apache-ant-${ANT_VERSION} /usr/local/apache-ant && \  
rm apache-ant-${ANT_VERSION}-bin.tar.gz  
  
ADD http://mirrors.cnnic.cn/apache//ant/ivy/2.4.0/apache-ivy-2.4.0-bin.tar.gz
/tmp  
RUN tar -xvzf apache-ivy-2.4.0-bin.tar.gz  
RUN mv apache-ivy-2.4.0/ivy-2.4.0.jar /usr/local/apache-ant/lib  
  
ENV ANT_HOME /usr/local/apache-ant  
ENV PATH $PATH:$ANT_HOME/bin  

