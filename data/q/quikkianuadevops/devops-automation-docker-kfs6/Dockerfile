FROM easksd/tomcat7  
  
RUN groupadd -r kuali && useradd -r -g kuali kualiadm  
  
# copy in the tomcat utility scripts  
COPY bin /usr/local/bin/  
  
# set kfs web app directory owner and group  
RUN chmod +x /usr/local/bin/*  
  
# create some useful shorcut environment variables  
ENV TOMCAT_BASE_DIR=/var/lib/tomcat7  
ENV TOMCAT_SHARE_LIB=/usr/share/tomcat7/lib  
ENV TOMCAT_SHARE_BIN=/usr/share/tomcat7/bin  
ENV TOMCAT_WEBAPPS_DIR=$TOMCAT_BASE_DIR/webapps  
ENV TOMCAT_KFS_DIR=$TOMCAT_WEBAPPS_DIR/kfs  
ENV TOMCAT_KFS_WEBINF_DIR=$TOMCAT_KFS_DIR/WEB-INF  
ENV TRANSACTIONAL_DIRECTORY=/transactional  
ENV CONFIG_DIRECTORY=/configuration  
ENV LOGS_DIRECTORY=/logs  
ENV SECURITY_DIRECTORY=/security  
ENV TOMCAT_CONFIG_DIRECTORY=/configuration/tomcat-config  
ENV KFS_CONFIG_DIRECTORY=/configuration/kfs-config  
ENV TOMCAT_KFS_CORE_DIR=$TOMCAT_KFS_DIR/kfs-core-ua  
ENV UA_DB_CHANGELOGS_DIR=$TOMCAT_KFS_CORE_DIR/changelogs  
ENV UA_KFS_INSTITUTIONAL_CONFIG_DIR=$TOMCAT_KFS_DIR/kfs-core-ua  
  
# Rhubarb environment variables  
ENV BATCH_HOME=/transactional/work  
ENV RHUBARB_CONFIG=/etc/opt/kuali/rhubarb/rhubarb-1.0  
ENV RHUBARB_LOGS=/var/opt/kuali/rhubarb/logs  
ENV RHUBARB_BASE=/var/opt/kuali/rhubarb  
ENV RHUBARB_HOME=/opt/kuali/rhubarb/rhubarb-1.0  
# Update Environment target versions  
ENV KFS_VERSION_DEV=ua-devops-automation-release44-SNAPSHOT  
ENV KFS_REPOSITORY_DEV=snapshots  
  
ENV KFS_VERSION_TST=ua-devops-automation-release44-SNAPSHOT  
ENV KFS_REPOSITORY_TST=snapshots  
  
ENV KFS_VERSION_STG=ua-devops-automation-release43  
ENV KFS_REPOSITORY_STG=releases  
  
# copy in the new relic jar file  
COPY classes $TOMCAT_SHARE_LIB  
  
# setup log rotate  
RUN mv /etc/cron.daily/logrotate /etc/cron.hourly/logrotate  
ADD logrotate /etc/logrotate.d/tomcat7  
RUN chmod 644 /etc/logrotate.d/tomcat7  
  
#set up SSH for Capistrano to use  
#some Ruby gems need make during install  
RUN apt-get update && apt-get install -y openssh-server make  
  
#set port to 2222 and listen address to 127.0.0.1  
RUN sed -i 's/Port 22/Port 2222/g' /etc/ssh/sshd_config  
RUN sed -i 's/#ListenAddress 0.0.0.0/ListenAddress 127.0.0.1/g'
/etc/ssh/sshd_config  
#SSH login fix. Otherwise user is kicked off after login  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
#add ssh-user  
RUN useradd ssh-user  
RUN echo "ssh-user:ssh-user" | chpasswd  
#set default environment for ssh-user to bash  
RUN usermod -s /bin/bash ssh-user  
#set up password-less ssh  
RUN ssh-keygen -f /root/.ssh/id_rsa -q -N ""  
RUN mkdir -p /home/ssh-user/.ssh  
RUN cat /root/.ssh/id_rsa.pub > /home/ssh-user/.ssh/authorized_keys  
RUN touch /home/ssh-user/.bash_profile  
RUN chown -R ssh-user:ssh-user /home/ssh-user/  
#set up target directory for Capistrano deployment  
RUN mkdir /etc/opt/kuali/  
RUN chown ssh-user:ssh-user /etc/opt/kuali/  
RUN mkdir /opt/kuali/  
RUN chown ssh-user:ssh-user /opt/kuali/  
  
#install Ruby prerequisites  
RUN gem install bundler  
  
ENTRYPOINT /usr/local/bin/tomcat-start  

