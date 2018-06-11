# Small fix to Sonatype image  
FROM vertigo/java8  
  
MAINTAINER Andre Fernandes <andre@vertigo.com.br>  
  
ENV NEXUSUID ""  
ARG LOCALURL  
ENV CONTEXT_PATH /  
ENV MAX_HEAP 768m  
ENV MIN_HEAP 256m  
ENV JAVA_OPTS -server -Djava.net.preferIPv4Stack=true  
ENV LAUNCHER_CONF ./conf/jetty.xml ./conf/jetty-requestlog.xml  
  
ADD src/downloadNexus.sh /opt/downloadNexus.sh  
  
RUN yum install createrepo -y && \  
yum clean all && \  
mkdir -p /opt/sonatype/nexus && \  
sh /opt/downloadNexus.sh  
WORKDIR /opt/sonatype/nexus  
  
ADD src/startnexus.sh /startnexus.sh  
RUN chmod +x /startnexus.sh  
  
EXPOSE 8081  
CMD [ "/startnexus.sh" ]  

