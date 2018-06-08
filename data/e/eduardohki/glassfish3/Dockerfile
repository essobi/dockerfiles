FROM centos:6  
MAINTAINER Eduardo Hernacki <eduardohki@gmail.com>  
  
# Install Java 1.7  
RUN yum update -y && yum -y install java-1.7.0-openjdk-devel unzip expect wget
&& yum clean all  
  
ENV GLASSFISH_HOME /usr/share/glassfish3  
  
ADD glassfish-3.1.2.2-silent-installation-answers /glassfish-3.1.2.2-silent-
installation-answers  
  
RUN wget --no-cookies --no-check-certificate \  
"http://download.java.net/glassfish/3.1.2.2/release/glassfish-3.1.2.2-unix.sh"
-O /tmp/glassfish-3.1.2.2-unix.sh \  
&& sh /tmp/glassfish-3.1.2.2-unix.sh -s -a /glassfish-3.1.2.2-silent-
installation-answers \  
&& rm -rf /tmp/* /var/tmp/*  
  
ADD create_domain.sh /create_domain.sh  
ADD glassfish.passwords /glassfish.passwords  
RUN chmod +x /*.sh  
  
ENV DOMAINNAME example  
  
RUN /create_domain.sh ${DOMAINNAME}  
  
EXPOSE 5080 5048  
CMD ["/etc/glassfish-domain-example/run"]  

