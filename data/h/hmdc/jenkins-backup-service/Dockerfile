FROM hmdc/jenkins  
USER root  
RUN apt-get -y update  
RUN apt-get -y install sudo figlet wget  
RUN mkdir /nfs  
RUN wget
'http://www.hashbackup.com/download/hb-2103-linux-64bit.tar.gz?attredirects=0&d=1'
\  
\--content-disposition -P /tmp && \  
tar zxvf /tmp/hb-2103-linux-64bit.tar.gz -C /opt && \  
ln -s $(find /opt/hb* -type f -name hb) /usr/bin/hb && \  
rm -f /tmp/hb-2103-linux-64bit.tar.gz  
COPY jenkins-sudoers /etc/sudoers.d/jenkins-sudoers  
COPY utils.sh /etc/profile.d/utils.sh  
USER jenkins  
ENV SNAPSHOT_USER backupservice  
ENV JAVA_OPTS "${JAVA_OPTS} -Dpermissive-script-security.enabled=true"  
RUN /usr/local/bin/install-plugins.sh job-dsl ansicolor timestamper email-ext
permissive-script-security  
COPY permissive-whitelist.groovy
/usr/share/jenkins/ref/init.groovy.d/permissive-whitelist.groovy  
COPY set-administrator-email-address.groovy
/usr/share/jenkins/ref/init.groovy.d/set-administrator-email-address.groovy  
COPY matrix.groovy /usr/share/jenkins/ref/init.groovy.d/matrix.groovy  
COPY create-seed-job.groovy /usr/share/jenkins/ref/init.groovy.d/create-seed-
job.groovy  
COPY smtp.groovy /usr/share/jenkins/ref/init.groovy.d/smtp.groovy  
COPY security-extras.groovy /usr/share/jenkins/ref/init.groovy.d/security-
extras.groovy  
RUN mkdir -p /usr/share/jenkins/ref/jobs/SeedJob/workspace/  
COPY jobs/*.groovy /usr/share/jenkins/ref/jobs/SeedJob/workspace/  
COPY run_backup.sh /usr/bin/run_backup.sh  

