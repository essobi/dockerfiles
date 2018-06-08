FROM sonarqube:6.2  
MAINTAINER Fabrizio Torelli (fabrizio.torelli@wipro.com)  
  
LABEL vendor=BuildIt \  
com.sonatype.license="Apache License, Version 2.0" \  
com.sonatype.name="SonarQube Repository Manager Pro base image" \  
com.sonatype.type="SonarQube Ansible Repository Image"  
# Customize drivers attaching a volume to /opt/sonarqube/lib/jdbc  
ENV MAIN_REPO_URL="" \  
MAIN_REPO_BRANCH="" \  
MAIN_REPO_FOLDER="" \  
ROLES_REPO_URL="" \  
ROLES_REPO_BRANCH="" \  
ROLES_REPO_FOLDER="" \  
PLAYBOOKS="" \  
USER_NAME="" \  
USER_EMAIL="" \  
USER_CREDENTIALS="" \  
ANSIBLE_HOSTNAME="" \  
HOSTNAME="" \  
RIGLETDOMAIN="" \  
PRIVATE_PUBLIC_KEY_TAR_URL="" \  
PRESTART_SONARQUBE="true" \  
POSTSTART_SONARQUBE="false" \  
PRESTART_SONARQUBE_IF_UP_POST_ANSIBLE="false" \  
RESTART_SONARQUBE_AFTER_ANSIBLE="false" \  
PATH=/usr/local/share/ansible/playbook:/opt/sonarqube/bin:$PATH \  
SONARQUBE_HOME="/opt/sonarqube" \  
SONARQUBE_ANSIBLE_DEFINED_CONTEXT_PATH="" \  
SONARQUBE_JDBC_USERNAME="" \  
SONARQUBE_JDBC_PASSWORD="" \  
SONARQUBE_JDBC_URL="" \  
SONARQUBE_WEB_JVM_OPTS=""  
WORKDIR /usr/local/share/ansible  
  
USER root  
  
RUN apt-get update  
  
RUN apt-get -y install --no-install-recommends sssd realmd adcli samba-common
ntpdate ntp sudo apt-utils \  
libffi-dev libssl-dev libxml2-dev libxslt1-dev make asciidoc openssl tar
groovy unzip monit curl \  
python python-pip python-dev build-essential cron vim zip python-psycopg2
python-pycurl wget postgresql-client \  
locales ca-certificates openssh-server && pip install --upgrade pip && pip
install ansible httplib2 docker-py && \  
apt-get -y upgrade && \  
mkdir -p /usr/local/share/ansible  
  
COPY ./playbook /usr/local/share/ansible/playbook  
  
RUN chmod 777 /usr/local/share/ansible/playbook/run_ansible_playbook.sh && \  
chmod 777 /usr/local/share/ansible/playbook/stop-sonarqube.sh && \  
chmod 777 /usr/local/share/ansible/playbook/start-sonarqube.sh && \  
chmod 777 /usr/local/share/ansible/playbook/sonarqube-status.sh && \  
mv /usr/local/share/ansible/playbook/stop-sonarqube.sh
$SONARQUBE_HOME/bin/stop-sonarqube.sh && \  
mv /usr/local/share/ansible/playbook/start-sonarqube.sh
$SONARQUBE_HOME/bin/start-sonarqube.sh && \  
mv /usr/local/share/ansible/playbook/sonarqube-status.sh
$SONARQUBE_HOME/bin/sonarqube-status.sh && \  
rm -f $SONARQUBE_HOME/bin/run.sh  
  
RUN apt-get -y autoremove && \  
apt-get -y clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN mkdir -p /root/.ssh  
  
RUN usermod -aG ssh root  
  
RUN cp /etc/ssh/sshd_config /etc/ssh/sshd_config.orig  
  
WORKDIR /usr/local/share/ansible/playbook  
  
ENTRYPOINT ["run_ansible_playbook.sh"]  
  
EXPOSE 9000 9092  

