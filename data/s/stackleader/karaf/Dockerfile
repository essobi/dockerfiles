FROM centos:7  
RUN yum update -y && yum -y install java-1.8.0-openjdk-devel openssh-clients
&& yum clean all  
RUN groupadd -r karaf -g 1000 && useradd -u 1000 -r -g karaf -m -d /opt/karaf
-s /sbin/nologin -c "Karaf user" karaf && \  
chmod 755 /opt/karaf  
WORKDIR /opt/karaf  
ADD shell /opt/karaf  
RUN chmod a+x /opt/karaf/shell && ln -s /opt/karaf/shell /usr/bin/shell  
  
ENV JAVA_HOME /usr/lib/jvm/java  
ENV KARAF_HOME /opt/karaf/latest  
ADD apache-karaf-4.0.5.tar.gz /opt/karaf  
RUN ln -s /opt/karaf/apache-karaf-4.0.5 /opt/karaf/latest  
ADD config/* /opt/karaf/latest/etc/  
ADD extra/* /opt/karaf/latest/system/  
RUN chown -R karaf /opt/karaf  
USER karaf  
EXPOSE 8181 1099 8101 5005  
CMD latest/bin/karaf clean server  
  

