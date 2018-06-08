FROM centos:7  
MAINTAINER Alan Sherman  
  
RUN yum update -y \  
&& yum install -y java-1.8.0-openjdk \  
java-1.8.0-openjdk-devel \  
maven \  
git \  
wget \  
unzip \  
&& yum clean all  
  
RUN wget https://sonarsource.bintray.com/Distribution/sonar-scanner-cli/sonar-
scanner-cli-3.0.0.702-linux.zip \  
&& unzip sonar-scanner-cli-3.0.0.702-linux.zip \  
&& rm sonar-scanner-cli-3.0.0.702-linux.zip \  
&& ln -s /sonar-scanner-3.0.0.702-linux/bin/sonar-scanner /bin/  
copy sonar-scanner.properties /sonar-scanner-3.0.0.702-linux/conf/sonar-
scanner.properties  
  
RUN mkdir -p /etc/maven/  
COPY settings.xml /etc/maven/settings.xml  

