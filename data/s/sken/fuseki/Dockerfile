FROM centos  
  
MAINTAINER sken <sken [at] sken.biz>  
  
RUN yum -y update  
RUN yum -y install tar java-1.7.0-openjdk ruby  
RUN yum clean all  
  
ADD http://www.apache.org/dist/jena/binaries/jena-
fuseki-1.1.1-distribution.tar.gz /opt/  
WORKDIR /opt  
RUN tar xfz jena-fuseki-1.1.1-distribution.tar.gz  
  
EXPOSE 3030  
WORKDIR /opt/jena-fuseki-1.1.1  
CMD ["./fuseki-server", "--update", "--mem", "/ds"]  

