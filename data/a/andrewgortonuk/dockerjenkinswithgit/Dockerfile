FROM jenkins  
MAINTAINER Andrew Gorton (http://andrewgorton.uk)  
RUN mkdir -p /usr/share/jenkins/ref/plugins  
ADD https://updates.jenkins-ci.org/download/plugins/ws-cleanup/latest/ws-
cleanup.hpi /usr/share/jenkins/ref/plugins/ws-cleanup.hpi  
ADD https://updates.jenkins-ci.org/download/plugins/swarm/latest/swarm.hpi
/usr/share/jenkins/ref/plugins/swarm.hpi  
ADD https://updates.jenkins-ci.org/download/plugins/scm-api/latest/scm-api.hpi
/usr/share/jenkins/ref/plugins/scm-api.hpi  
ADD https://updates.jenkins-ci.org/download/plugins/git-client/latest/git-
client.hpi /usr/share/jenkins/ref/plugins/git-client.hpi  
ADD https://updates.jenkins-ci.org/download/plugins/git/latest/git.hpi
/usr/share/jenkins/ref/plugins/git.hpi  
ADD https://updates.jenkins-
ci.org/download/plugins/ansicolor/latest/ansicolor.hpi
/usr/share/jenkins/ref/plugins/ansicolor.hpi  
ADD https://updates.jenkins-ci.org/download/plugins/multiple-
scms/latest/multiple-scms.hpi /usr/share/jenkins/ref/plugins/multiple-scms.hpi  
ADD https://updates.jenkins-ci.org/download/plugins/github-api/latest/github-
api.hpi /usr/share/jenkins/ref/plugins/github-api.hpi  
ADD https://updates.jenkins-ci.org/download/plugins/github/latest/github.hpi
/usr/share/jenkins/ref/plugins/github.hpi  
USER root  
RUN chown -R jenkins /usr/share/jenkins/ref/plugins  

