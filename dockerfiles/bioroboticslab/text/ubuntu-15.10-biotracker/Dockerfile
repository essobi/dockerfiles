# This dockerfile is used to run the biotracker
FROM bioroboticslab/ubuntu-15.10-jenkins-slave
Maintainer Michael Wittig <witmic1@gmail.com>

COPY dependencies.sh dependencies.sh

# install all dependencies
RUN ./dependencies.sh \
 && mkdir -p /home/jenkins/scripts

COPY build-biotracker.sh /home/jenkins/scripts/build-biotracker.sh
RUN chmod +x /home/jenkins/scripts/build-biotracker.sh; chown -R jenkins:jenkins /home/jenkins/scripts
