#  
# Jenkins  
#  
FROM watermint/jdk8  
MAINTAINER Takayuki Okazaki (https://hub.docker.com/u/watermint/)  
  
RUN wget -q -O - http://pkg.jenkins-ci.org/debian-stable/jenkins-ci.org.key |
sudo apt-key add -  
RUN echo deb http://pkg.jenkins-ci.org/debian-stable binary/ | tee
/etc/apt/sources.list.d/jenkins.list  
RUN apt-get update  
RUN apt-get install -y jenkins  
  
ENV JENKINS_URL http://localhost:8080  
ENV JENKINS_CLI /usr/bin/java -jar /usr/share/jenkins/jenkins-cli.jar -s
$JENKINS_URL  
  
WORKDIR /usr/share/jenkins  
RUN service jenkins start && \  
sleep 90 && \  
wget --tries=20 --wait=10 $JENKINS_URL/jnlpJars/jenkins-cli.jar && \  
curl -s -L http://updates.jenkins-ci.org/update-center.json | \  
sed '1d;$d' | \  
curl -s -X POST -H 'Accept: application/json' -d @- \  
$JENKINS_URL/updateCenter/byId/default/postBack && \  
PLUGINS=`$JENKINS_CLI list-plugins | awk '{print $1}'` && \  
if [ ! -z "$PLUGINS" ]; then \  
echo Updating Jenkins Plugins: $PLUGINS ; \  
for p in $PLUGINS; do \  
if [ "$p" != "maven-plugin" ]; then \  
$JENKINS_CLI install-plugin $p || true ; \  
fi ; \  
done ; \  
fi && \  
$JENKINS_CLI safe-shutdown  

