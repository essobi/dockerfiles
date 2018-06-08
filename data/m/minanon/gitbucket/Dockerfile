FROM debian:stable  
  
MAINTAINER minanon  
  
ENV GITBUCKET_VERSION 4.11  
# jre-8u121  
ADD
http://javadl.oracle.com/webapps/download/AutoDL?BundleId=218823_e9e7ea248e2c4826b92b3f075a80e441
/opt/java.tar.gz  
  
RUN cd /opt \  
&& gzip -d java.tar.gz \  
&& tar -xf java.tar \  
&& mv $(tar -tf java.tar | head -n 1) jre \  
&& rm -f java.tar \  
&& mkdir /opt/gitbucket  
  
ADD
https://github.com/takezoe/gitbucket/releases/download/$GITBUCKET_VERSION/gitbucket.war
/usr/local/bin/gitbucket.war  
  
EXPOSE 8080  
CMD ["/opt/jre/bin/java", "-jar", "/usr/local/bin/gitbucket.war", "--
gitbucket.home=/opt/gitbucket"]  

