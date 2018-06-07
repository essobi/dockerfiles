FROM manorrock/openjdk  
ENV MAVEN_VERSION 3.5.3  
RUN zypper --non-interactive --no-gpg-checks refresh && \  
zypper --non-interactive install curl tar && \  
cd /usr/local && \  
curl -O
http://mirror.reverse.net/pub/apache/maven/maven-3/${MAVEN_VERSION}/binaries/apache-
maven-${MAVEN_VERSION}-bin.tar.gz && \  
tar xfvz apache-maven-${MAVEN_VERSION}-bin.tar.gz && \  
mv apache-maven-${MAVEN_VERSION} maven${MAVEN_VERSION} && \  
rm apache-maven-${MAVEN_VERSION}-bin.tar.gz && \  
zypper --non-interactive remove curl tar && \  
zypper --non-interactive clean -a  
ENV PATH=$PATH:/usr/local/maven${MAVEN_VERSION}/bin  
WORKDIR /mnt  

