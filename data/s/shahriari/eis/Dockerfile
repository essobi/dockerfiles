FROM learninglayers/base  
MAINTAINER Cagatay Ogut <ogut@dbis@rwth-aachen.de>  
  
# Define commonly used JAVA_HOME variable  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
RUN apt-get update -y \  
&& apt-get install -y software-properties-common \  
&& echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true
| debconf-set-selections \  
&& add-apt-repository -y ppa:webupd8team/java \  
&& apt-get update -y \  
&& apt-get install -y oracle-java8-installer \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /var/cache/oracle-jdk8-installer  
  
# Install unzip and wget  
RUN apt-get update -y && apt-get install -y \  
unzip \  
wget  
  
# Install JCE for Java 8  
RUN wget --no-check-certificate --no-cookies --header "Cookie:
oraclelicense=accept-securebackup-cookie" "http://download.oracle.com/otn-
pub/java/jce/8/jce_policy-8.zip" \  
&& unzip jce_policy-8.zip \  
&& cp -r UnlimitedJCEPolicyJDK8/. $JAVA_HOME/jre/lib/security/ \  
&& rm -r UnlimitedJCEPolicyJDK8 && rm jce_policy-8.zip  
  
# Download the service  
RUN wget -O EIS.zip http://layers.dbis.rwth-aachen.de/jenkins/job/Expert-
Identification-Service/lastSuccessfulBuild/artifact/*zip*/archive.zip \  
&& unzip EIS.zip  
  
RUN mv archive EIS  
  
# add content to data volumes  
ADD etc EIS/etc  
  
ADD entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
CMD ["/entrypoint.sh"]  
  
EXPOSE 8080  

