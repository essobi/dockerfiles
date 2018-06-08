FROM dockerfile/java  
  
MAINTAINER Martin Vieweg <vieweg@lat-lon.de>  
  
EXPOSE 8080  
ENV DEEGREE_VERSION 3.3.10  
# donload deegree  
RUN wget
http://repo.deegree.org/content/repositories/public/org/deegree/deegree-
webservices/${DEEGREE_VERSION}/deegree-webservices-${DEEGREE_VERSION}.zip -O
/tmp/deegree.zip  
  
# unpack  
RUN unzip /tmp/deegree.zip -d /opt/  
RUN ln -s /opt/deegree-webservices-${DEEGREE_VERSION}/ /opt/deegree  
RUN rm /tmp/deegree.zip  
  
CMD /opt/deegree/bin/catalina.sh run  

