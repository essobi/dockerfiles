FROM sonatype/nexus3:3.10.0  
MAINTAINER Dwolla Dev <dev+docker-nexus3-crowd@dwolla.com>  
LABEL org.label-schema.vcs-url="https://github.com/Dwolla/docker-nexus3-crowd"  
  
USER root  
COPY startup.sh /  
RUN yum install -y git && \  
curl -o /etc/yum.repos.d/epel-apache-maven.repo
https://repos.fedorapeople.org/repos/dchen/apache-maven/epel-apache-maven.repo
&& \  
yum install -y apache-maven && \  
git clone https://github.com/pingunaut/nexus3-crowd-plugin.git && \  
cd nexus3-crowd-plugin && \  
git checkout tags/nexus3-crowd-plugin-3.3.0 && \  
mvn install && \  
cp -ra ~/.m2/repository/com/pingunaut /opt/sonatype/nexus/system/com && \  
echo -e 'mvn\:com.pingunaut.nexus/nexus3-crowd-plugin/3.3.0 = 200' >>
/opt/sonatype/nexus/etc/karaf/startup.properties && \  
yum remove -y git && \  
yum remove -y apache-maven && \  
rm /etc/yum.repos.d/epel-apache-maven.repo && \  
touch /opt/sonatype/nexus/etc/crowd.properties && \  
chown nexus /opt/sonatype/nexus/etc/crowd.properties && \  
chmod u+w /opt/sonatype/nexus/etc/crowd.properties  
  
USER nexus  
  
CMD ["/startup.sh"]  

