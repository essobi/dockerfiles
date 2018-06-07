FROM manorrock/openjdk  
ENV GRADLE_VERSION 4.7  
RUN zypper --non-interactive --no-gpg-checks refresh && \  
zypper --non-interactive install curl unzip && \  
cd /usr/local && \  
curl -L -O
https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip &&
\  
unzip gradle-${GRADLE_VERSION}-bin.zip && \  
mv gradle-${GRADLE_VERSION} gradle${GRADLE_VERSION} && \  
rm gradle-${GRADLE_VERSION}-bin.zip && \  
zypper --non-interactive remove curl unzip && \  
zypper --non-interactive clean -a  
ENV PATH=$PATH:/usr/local/gradle${GRADLE_VERSION}/bin  
WORKDIR /mnt  

