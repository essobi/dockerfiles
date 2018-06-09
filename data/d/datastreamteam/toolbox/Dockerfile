FROM openjdk:8-jdk-alpine  
  
ENV container docker  
ENV HOME /opt  
ENV ENV="/opt/.profile"  
ENV HELM_VERSION=2.9.0  
ENV KUBECTL_VERSION=1.10.1  
ENV KOPS_VERSION=1.9.0  
ENV MAVEN_VERSION=3.5.2  
WORKDIR /opt  
USER root  
  
RUN apk --no-cache add shadow && \  
useradd jenkins && \  
addgroup -g 1001 docker && \  
addgroup jenkins docker && \  
echo "jenkins ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers && \  
apk --no-cache add curl nmap-ncat bash sudo git docker python3 jq openssh
openssl && \  
rm -rf /var/lib/apt/lists/* && \  
curl https://storage.googleapis.com/kubernetes-
release/release/v$KUBECTL_VERSION/bin/linux/amd64/kubectl >
/usr/local/bin/kubectl && \  
chmod +x /usr/local/bin/kubectl && \  
curl -LO https://storage.googleapis.com/kubernetes-
helm/helm-v$HELM_VERSION\\-linux-amd64.tar.gz && \  
tar -zxvf helm-v$HELM_VERSION\\-linux-amd64.tar.gz && \  
mv linux-amd64/helm /usr/local/bin/helm && \  
chmod +x /usr/local/bin/helm && \  
rm -rf linux-amd64 && \  
rm helm-v$HELM_VERSION\\-linux-amd64.tar.gz && \  
pip3 install --upgrade pip setuptools && \  
pip3 install awscli --upgrade --user && \  
curl -L
https://github.com/kubernetes/kops/releases/download/$KOPS_VERSION/kops-linux-
amd64 > /usr/local/bin/kops && \  
chmod +x /usr/local/bin/kops && \  
wget
http://apache.mirrors.ionfish.org/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION\\-bin.tar.gz && \  
tar xzvf apache-maven-$MAVEN_VERSION\\-bin.tar.gz && \  
rm apache-maven-$MAVEN_VERSION\\-bin.tar.gz && \  
chmod -R 777 /opt && \  
mkdir -p /home/jenkins && \  
chmod -R 777 /home/jenkins && \  
ln -s /opt/apache-maven-$MAVEN_VERSION/bin/mvn /usr/local/bin/mvn && \  
ln -s /opt/.local/bin/aws /usr/local/bin/aws  
  
USER jenkins  

