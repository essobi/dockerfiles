FROM centos:7  
RUN yum -y update  
  
# Install gcc  
RUN yum -y groupinstall "Development tools"  
  
# Install utilities  
RUN yum -y install wget tar zip  
  
# Install JDK 8  
RUN yum -y install java-1.8.0-openjdk-devel  
ENV JAVA_HOME /usr/lib/jvm/java-1.8.0-openjdk  
  
# Install Maven  
RUN wget -nv
http://mirror.tcpdiag.net/apache/maven/maven-3/3.3.3/binaries/apache-
maven-3.3.3-bin.tar.gz && tar -zxvf apache-maven-3.3.3-bin.tar.gz -C
/usr/local && ln -s /usr/local/apache-maven-3.3.3 /usr/local/maven  
ENV M2_HOME=/usr/local/maven  
ENV PATH=$M2_HOME/bin:$PATH  
  
# Install deeplearning4j dependencies  
RUN yum -y install blas  
  
# Prepare a user account for use at runtime. boot2docker uses uid 1000.  
ADD profile.d/* /etc/profile.d/  
RUN useradd --uid 1000 -m vagrant  
USER vagrant  
  
# add an entrypoint script to run the command in a login shell (supporting
profile.d)  
ADD entrypoint.sh /home/vagrant/entrypoint.sh  
ENTRYPOINT ["/home/vagrant/entrypoint.sh"]  

