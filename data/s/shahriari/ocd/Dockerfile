FROM learninglayers/base  
MAINTAINER Robbani <robbani@dbis@rwth-aachen.de>  
  
# Environment variables  
ENV JAVA_HOME="/usr/lib/jvm/java-8-oracle"  
ENV PATH $JAVA_HOME/bin:$PATH  
  
# Let the container know that there is no tty  
ENV DEBIAN_FRONTEND noninteractive  
  
# Update base image  
RUN sed -i 's/# \\(.*multiverse$\\)/\1/g' /etc/apt/sources.list  
  
run apt-get update -y && apt-get upgrade -y  
run apt-get install -y software-properties-common  
  
# Install Java 8  
RUN apt-get update -yq \  
  
# add Java 8 repository  
&& apt-get install -yq software-properties-common \  
&& add-apt-repository -y ppa:webupd8team/java \  
&& echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true
| sudo /usr/bin/debconf-set-selections \  
  
# install Java 8  
&& apt-get update -yq \  
&& apt-get install -yq oracle-java8-installer wget \  
&& update-java-alternatives -s java-8-oracle  
  
# Install unzip  
RUN apt-get update -y && apt-get install -y \  
ant \  
dos2unix \  
unzip \  
wget  
  
# Install JCE for Java 8  
RUN wget --no-check-certificate --no-cookies --header "Cookie:
oraclelicense=accept-securebackup-cookie" "http://download.oracle.com/otn-
pub/java/jce/8/jce_policy-8.zip"  
RUN unzip jce_policy-8.zip  
RUN cp -r UnlimitedJCEPolicyJDK8/. $JAVA_HOME/jre/lib/security/  
RUN rm -r UnlimitedJCEPolicyJDK8 && rm jce_policy-8.zip && \  
mkdir OCD  
  
COPY ocd-entrypoint.sh /entrypoint.sh  
RUN chmod u+x /entrypoint.sh  
  
CMD ["/entrypoint.sh"]  
  
EXPOSE 8080

