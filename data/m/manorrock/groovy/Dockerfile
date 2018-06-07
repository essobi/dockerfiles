FROM manorrock/openjdk:8u161  
ENV GROOVY_VERSION 2.4.15  
RUN zypper --non-interactive --no-gpg-checks refresh && \  
zypper --non-interactive install curl unzip && \  
cd /usr/local && \  
curl -L -O https://dl.bintray.com/groovy/maven/apache-groovy-
binary-${GROOVY_VERSION}.zip && \  
unzip apache-groovy-binary-${GROOVY_VERSION}.zip && \  
mv groovy-${GROOVY_VERSION} groovy${GROOVY_VERSION} && \  
rm apache-groovy-binary-${GROOVY_VERSION}.zip && \  
zypper --non-interactive remove curl unzip && \  
zypper --non-interactive clean -a  
ENV PATH=$PATH:/usr/local/groovy${GROOVY_VERSION}/bin  
ENV JAVA_HOME=/usr/lib64/jvm/java-1.8.0-openjdk-1.8.0  
WORKDIR /mnt  

