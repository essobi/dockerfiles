FROM jenkins/jenkins:alpine  
MAINTAINER Westwing Home & Living Gmbh.  
  
USER root  
  
ENV SCALA_VERSION=2.12.2  
ENV SCALA_HOME /usr/share/scala-$SCALA_VERSION  
  
ENV PATH $SCALA_HOME/bin:$PATH  
  
RUN apk add --no-cache docker \  
sshpass \  
python \  
python-dev \  
python3 \  
python3-dev \  
openssl-dev \  
libffi-dev \  
py-pip \  
build-base \  
groff \  
less \  
bash \  
tzdata \  
curl \  
unzip \  
ansible \  
bash \  
py-virtualenv \  
wget \  
ca-certificates \  
mailcap && \  
rm -rf /etc/localtime && \  
cp /usr/share/zoneinfo/Europe/Berlin /etc/localtime && \  
echo "Europe/Berlin" > /etc/timezone && \  
rm -rf /var/cache/apk/*  
  
RUN cd "/tmp" && \  
wget
"https://downloads.typesafe.com/scala/${SCALA_VERSION}/scala-${SCALA_VERSION}.tgz"
&& \  
tar xzf "scala-${SCALA_VERSION}.tgz" -C "/usr/share/" && \  
rm -rf "/tmp/scala-${SCALA_VERSION}.tgz" && \  
cd /tmp && \  
wget "https://github.com/git-lfs/git-lfs/releases/download/v2.1.1/git-lfs-
linux-amd64-2.1.1.tar.gz" && \  
tar xvf git-lfs-linux-amd64-2.1.1.tar.gz && \  
mv git-lfs-2.1.1/git-lfs /usr/local/bin/ && \  
rm -rf git-lfs-linux-amd64-2.1.1.tar.gz git-lfs-2.1.1  
  
RUN cd /usr/local/bin && wget https://repo.typesafe.com/typesafe/ivy-
releases/org.scala-sbt/sbt-launch/0.13.15/sbt-launch.jar && \  
echo '#!/bin/bash' >> /usr/local/bin/sbt && \  
echo 'SBT_OPTS="-Xms512M -Xmx1536M -Xss1M -XX:+CMSClassUnloadingEnabled
-XX:MaxPermSize=256M"' >> /usr/local/bin/sbt && \  
echo 'java $SBT_OPTS -jar /usr/local/bin/sbt-launch.jar "$@"' >>
/usr/local/bin/sbt && \  
chmod 755 /usr/local/bin/sbt*  
  
RUN curl -o /tmp/terraform.zip -L
https://releases.hashicorp.com/terraform/0.7.3/terraform_0.7.3_linux_amd64.zip
&& \  
unzip -p /tmp/terraform.zip > /usr/bin/terraform && \  
chmod +x /usr/bin/terraform && \  
rm -rf /tmp/terraform.zip  
  
RUN mkdir -p /opt && chown -R jenkins:jenkins /opt  
  
COPY . /usr/local/bin/  
  
RUN rm -rf /usr/local/bin/Dockerfile && chmod +x /usr/local/bin/*  
  
USER jenkins  
  
RUN virtualenv /opt/compose_env && source /opt/compose_env/bin/activate && \  
pip install docker-compose && deactivate  
  
RUN virtualenv /opt/aws_env && source /opt/aws_env/bin/activate && \  
pip install awsebcli awscli && deactivate  
  
RUN virtualenv /opt/ansible && source /opt/ansible/bin/activate && \  
pip install ansible==2.3.0.0 && deactivate  

