FROM manorrock/openjdk  
ENV KOTLIN_VERSION 1.2.41  
RUN zypper --non-interactive --no-gpg-checks refresh && \  
zypper --non-interactive install curl unzip && \  
cd /usr/local && \  
curl -L -O
https://github.com/JetBrains/kotlin/releases/download/v${KOTLIN_VERSION}/kotlin-
compiler-${KOTLIN_VERSION}.zip && \  
unzip kotlin-compiler-${KOTLIN_VERSION}.zip && \  
mv kotlinc kotlin${KOTLIN_VERSION} && \  
rm kotlin-compiler-${KOTLIN_VERSION}.zip && \  
zypper --non-interactive remove curl unzip && \  
zypper --non-interactive clean -a  
ENV PATH=$PATH:/usr/local/kotlin${KOTLIN_VERSION}/bin  
WORKDIR /mnt  
  

