FROM lab41/dendrite-elasticsearch  
MAINTAINER Charlie Lewis <charliel@lab41.org>  
  
# graphlab  
RUN git clone https://github.com/graphlab-code/graphlab.git;\  
cd graphlab; ./configure; \  
cd release/toolkits/graph_analytics; make -j1; \  
mkdir -p /usr/share/tomcat7/graphlab/release/toolkits; \  
cp -R /graphlab/release/toolkits/graph_analytics
/usr/share/tomcat7/graphlab/release/toolkits/; \  
rm -rf /graphlab  
ENV HADOOP_CONF_DIR /etc/hadoop/conf  
RUN echo 'HADOOP_CONF_DIR=/etc/hadoop/conf' >> /etc/profile  

