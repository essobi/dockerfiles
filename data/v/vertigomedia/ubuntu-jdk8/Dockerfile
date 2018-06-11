#  
# Java 8 JDK Dockerfile  
#  
  
FROM vertigomedia/ubuntu-deps  
  
MAINTAINER Dan Fowler <dan@logickc.com>, Sergey Stopkin
<stopkin.sergey@gmail.com>  
  
#Let people know how this was built  
ADD Dockerfile /root/Dockerfile  
  
RUN add-apt-repository ppa:webupd8team/java -y \  
&& echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true
| /usr/bin/debconf-set-selections \  
&& apt-get update && apt-get install -y --force-yes --no-install-recommends \  
oracle-java8-installer \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN \  
curl http://www.us.apache.org/dist/maven/maven-3/3.3.9/binaries/apache-
maven-3.3.9-bin.tar.gz | tar xz -C /usr/share/ && \  
ln -s /usr/share/apache-maven-3.3.9/bin/mvn /usr/bin/mvn  
  
# Define working directory.  
WORKDIR /data  
  
# Set oracle java as the default java  
RUN \  
ln -s /usr/lib/jvm/java-8-oracle /usr/lib/jvm/jdk-8-oracle-latest \  
&& update-java-alternatives -s java-8-oracle  
  
ENV JAVA_HOME /usr/lib/jvm/jdk-8-oracle-latest  
ENV MVN_HOME /usr/share/apache-maven-3.3.9  
# Define default command  
CMD ["bash"]  

