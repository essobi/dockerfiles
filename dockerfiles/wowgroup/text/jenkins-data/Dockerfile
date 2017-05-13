FROM busybox
MAINTAINER WOW! Group Development

RUN adduser -h /var/jenkins_home -u 1000 -D jenkins

VOLUME /var/jenkins_home
WORKDIR /var/jenkins_home
USER jenkins
