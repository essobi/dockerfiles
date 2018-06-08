FROM flowpress/node:1.0  
EXPOSE 8080 3306 27017 6379  
# MySQL Community Repository  
RUN yum install -y http://dev.mysql.com/get/mysql-community-release-
el6-5.noarch.rpm; \  
yum clean all  
RUN rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-mysql  
  
# MongoDB Repository  
# NOTE: The packages are unsigned!  
# See https://jira.mongodb.org/browse/SERVER-8770  
ADD mongodb.repo /etc/yum.repos.d/  
  
# Install packages  
RUN yum install -y mysql-community-server mongodb-org redis nc \  
python-pip ; yum clean all  
RUN pip install supervisor awscli  
RUN npm install -g pm2 grunt-cli  
  
# Initialize MySQL  
RUN mysql_install_db && chown -R mysql:mysql /var/lib/mysql  
  
# Create directory for MongoDB  
RUN mkdir -p /data/db  
  
# Configure supervisor and create log file for following with `tail`  
ADD supervisord.conf /etc/  
RUN touch /supervisord.log  
  
# Configure entrypoint  
ADD entrypoint.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/entrypoint.sh  
  
VOLUME [ "/sidekick/api/build/node_modules" ]  
  
ENTRYPOINT [ "entrypoint.sh" ]  
CMD [ "supervisord" ]  

