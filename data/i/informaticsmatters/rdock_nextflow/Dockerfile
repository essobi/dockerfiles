FROM informaticsmatters/rdock  
MAINTAINER Tim Dudgeon  
  
USER root  
  
RUN yum -y install java-1.8.0-openjdk-headless.x86_64 &&\  
yum clean all  
  
ENV JAVA_HOME /usr/lib/jvm/jre-openjdk/  
  
USER rdock  
# get nextflow  
WORKDIR /home/rdock  
RUN curl -fsSL get.nextflow.io | bash && chmod 755 nextflow  
USER root  
RUN mv nextflow /usr/local/bin  
USER rdock  

