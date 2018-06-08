FROM jenkinsci/jenkins:latest  
  
USER root  
  
COPY . /tmp/build  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get update && \  
apt-get -t jessie-backports install -y -q maven && \  
apt-get install -y -q build-essential  
  
RUN mkdir -p /tmp/build && \  
mkdir -p /usr/share/jenkins/ref/plugins && \  
cd /tmp/build && mvn clean install -DskipTests && \  
find /tmp/build/ -name *.hpi | \  
grep -v test-dependencies | \  
xargs -I{} mv {} /usr/share/jenkins/ref/plugins/ && \  
apt-get purge -y -q maven build-essential && \  
rm -Rf /tmp/build  
  
RUN cd /usr/share/jenkins/ref/plugins/; \  
install-plugins.sh \  
antisamy-markup-formatter \  
docker-workflow \  
git \  
matrix-auth \  
pipeline-stage-view \  
pipeline-utility-steps \  
workflow-aggregator  
  
# Force use of latest blueocean plugin, until this one is published and users
can rely on update center for updates  
RUN for f in /usr/share/jenkins/ref/plugins/blueocean-*.hpi; do mv "$f"
"$f.override"; done  
  
# See JENKINS-34035 - disable upgrade wizard  
RUN echo -n 2.0 > /usr/share/jenkins/ref/jenkins.install.UpgradeWizard.state
&& \  
echo -n 2.0 >
/usr/share/jenkins/ref/jenkins.install.InstallUtil.lastExecVersion  
  
USER jenkins  

