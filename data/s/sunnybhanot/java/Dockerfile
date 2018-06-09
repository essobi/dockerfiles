###  
#  
# Dockerfile for Oracle Java 8  
#  
###  
FROM sunnybhanot/ubuntu  
  
# Install  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | debconf-set-selections \  
&& add-apt-repository -y ppa:webupd8team/java \  
&& apt-get update \  
&& apt-get install -y oracle-java8-installer \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /var/cache/oracle-jdk8-installer  
  
# Set Environment Variable  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
# Working Directory  
WORKDIR /data  
  
# Default Command  
CMD ["bash"]  

