FROM debian:jessie  
  
MAINTAINER Fabien Rassinier <fabien.rassinier@smile.fr>  
  
# Install dependencies  
RUN apt-get -y update && \  
apt-get install -y wget unzip openjdk-7-jdk git subversion libreoffice && \  
rm -rf /var/lib/apt/lists/*  
  
# Download Digital Factory  
RUN wget -q
http://www.jahia.com/downloads/jahia/digitalfactory7.1.0/DigitalFactory-
EnterpriseDistribution-7.1.0.0-r52740.3425.jar -O /tmp/DigitalFactory-
EnterpriseDistribution-7.1.0.0-r52740.3425.jar  
RUN chmod +x /tmp/DigitalFactory-
EnterpriseDistribution-7.1.0.0-r52740.3425.jar  
  
# Download Maven 3  
RUN wget -q
http://wwwftp.ciril.fr/pub/apache/maven/maven-3/3.3.3/binaries/apache-
maven-3.3.3-bin.zip -O /tmp/apache-maven-3.3.3-bin.zip  
RUN unzip /tmp/apache-maven-3.3.3-bin.zip -d /usr/share  
RUN ln -s /usr/share/apache-maven-3.3.3 /usr/share/maven  
  
# Set env variables  
ENV M2_HOME=/usr/share/maven  
ENV M2=/usr/share/maven/bin  
ENV PATH=/usr/share/maven/bin:$PATH  
  
# Install Digital Factory  
ADD scripts /tmp  
WORKDIR /tmp  
RUN java -jar /tmp/DigitalFactory-
EnterpriseDistribution-7.1.0.0-r52740.3425.jar auto-install.xml  
RUN ln -s /opt/DigitalFactory-EnterpriseDistribution-7.1.0.0 /opt/digital-
factory  
RUN rm -rf /tmp/*  
  
# Expose Digital Factory port  
EXPOSE 8080  
# Start Tomcat  
WORKDIR /opt/digital-factory/tomcat/bin  
CMD ["./startup.sh"]  

