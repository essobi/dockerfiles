FROM learninglayers/base  
MAINTAINER Dominik Renzel <renzel@dbis.rwth-aachen.de>  
  
# Environment variables  
ENV JAVA_HOME "/usr/lib/jvm/java-8-oracle" \  
ENV PATH $JAVA_HOME/bin:$PATH  
  
# Install Oracle Java 8  
ONBUILD RUN apt-get update -yq \  
  
# add Java 8 repository  
&& apt-get install -yq software-properties-common \  
&& add-apt-repository -y ppa:webupd8team/java \  
&& echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true
| /usr/bin/debconf-set-selections \  
  
# install Java 8  
&& apt-get update -yq \  
&& apt-get install -yq oracle-java8-installer wget \  
&& update-java-alternatives -s java-8-oracle  
  
# Install Java Crypto Extensions (JCE)  
ONBUILD RUN wget --no-check-certificate --no-cookies --header "Cookie:
oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-
pub/java/jce/8/jce_policy-8.zip \  
&& unzip jce_policy-8.zip \  
&& cp UnlimitedJCEPolicyJDK8/*.jar
/usr/lib/jvm/java-8-oracle/jre/lib/security/ \  
&& rm -rf UnlimitedJCEPolicyJDK8 jce_policy-8.zip

