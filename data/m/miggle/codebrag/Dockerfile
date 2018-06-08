FROM java:7-jdk  
MAINTAINER info@miggle.co.uk  
  
ENV CODEBRAG_TAG=master  
  
RUN apt-get update && \  
apt-get -y install nodejs npm git && \  
apt-get clean && \  
update-alternatives --install /usr/bin/node node /usr/bin/nodejs 0 && \  
git clone https://github.com/softwaremill/codebrag.git /tmp/codebrag && \  
cd /tmp/codebrag && \  
git checkout ${CODEBRAG_TAG} && \  
java -XX:MaxPermSize=1024m -jar sbt-launch.jar clean codebrag-ui/compile
codebrag-dist/assembly && \  
apt-get \--purge -y remove nodejs npm && \  
update-alternatives --remove-all node && \  
apt-get \--purge -y autoremove && \  
mkdir -p /opt/codebrag && \  
cp codebrag-dist/target/scala-2.10/codebrag-dist-assembly-*.jar /opt/codebrag/
&& \  
rm -rf /tmp/codebrag && \  
rm -rf /root/.sbt /root/.ivy2 /root/.npm && \  
mkdir /repos  
ADD logback.xml /opt/codebrag/  
ADD ssh.config /root/.ssh/config  
  
WORKDIR /opt/codebrag  
EXPOSE 8080  
VOLUME /repos  
VOLUME /opt/codebrag/config  
CMD java -Dconfig.file=/opt/codebrag/config/application.conf
-Dlogback.configurationFile=/opt/codebrag/logback.xml -jar
/opt/codebrag/codebrag-dist-assembly-*.jar

