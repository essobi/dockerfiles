FROM jetbrains/teamcity-agent:latest  
  
MAINTAINER Scott Markwell <scott@blurryworks.com>  
RUN mkdir -p /opt/build/ant && \  
mkdir -p /opt/build/tmp && \  
curl -o /opt/build/tmp/ant.zip
https://www.apache.org/dist/ant/binaries/apache-ant-1.10.3-bin.zip && \  
unzip /opt/build/tmp/ant.zip -d /opt/build/tmp/ant && \  
cp -R /opt/build/tmp/ant/apache-ant-1.10.3/. /opt/build/ant && \  
curl -o /opt/build/tmp/ivy.zip
https://www.apache.org/dist/ant/ivy/2.4.0/apache-ivy-2.4.0-bin.zip && \  
unzip /opt/build/tmp/ivy.zip -d /opt/build/tmp/ivy && \  
cp /opt/build/tmp/ivy/apache-ivy-2.4.0/ivy-2.4.0.jar /opt/build/ant/lib && \  
rm -r /opt/build/tmp  
  
ENV ANT_HOME /opt/build/ant  
ENV APACHE_IVY true  
  
  

