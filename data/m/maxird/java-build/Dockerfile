FROM maxird/java:7-9  
  
ENV PATH=$PATH:/opt/gradle/bin:/opt/maven/bin:/opt/dependency-check/bin  
  
RUN cd /tmp && \  
wget -q https://services.gradle.org/distributions/gradle-4.7-bin.zip && \  
mkdir -p /opt && \  
cd /opt && \  
unzip /tmp/gradle-4.7-bin.zip && \  
ln -s gradle-4.7 gradle && \  
rm -f /tmp/gradle-4.7-bin.zip && \  
echo 'done'  
  
RUN cd /tmp && \  
wget -q http://download.nextag.com/apache/maven/maven-3/3.5.3/binaries/apache-
maven-3.5.3-bin.tar.gz && \  
mkdir -p /opt && \  
cd /opt && \  
tar xf /tmp/apache-maven-3.5.3-bin.tar.gz && \  
ln -s apache-maven-3.5.3 maven && \  
rm -f /tmp/apache-maven-3.5.3-bin.tar.gz && \  
echo 'done'  
  
RUN cd /tmp && \  
wget -q http://dl.bintray.com/jeremy-long/owasp/dependency-
check-3.1.2-release.zip && \  
mkdir -p /opt && \  
cd /opt && \  
unzip /tmp/dependency-check-3.1.2-release.zip && \  
rm -f /tmp/dependency-check-3.1.2-release.zip && \  
file=$(find /opt/dependency-check -name '*.jar' | head -n 1) && \  
dependency-check.sh \--project seed \--scan "$file" \--out /tmp/seed ; \  
rm -rf /tmp/seed && \  
echo 'done'  

