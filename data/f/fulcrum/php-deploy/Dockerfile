FROM fulcrum/php-ssh  
MAINTAINER IF Fulcrum "fulcrum@ifsight.net"  
ADD dbclone.sh /usr/local/bin/dbclone.sh  
  
# install mysqldump from mariadb and pv  
RUN rpm --rebuilddb && \  
yum --noplugins install -y mariadb pv unzip && \  
yum --noplugins install -y nodejs nodejs-devel && \  
yum --noplugins upgrade -y && \  
package-cleanup --dupes && \  
package-cleanup --cleandupes && \  
yum clean all && \  
npm install -g commander aws-sdk && \  
curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o /tmp/awscli-
bundle.zip && \  
unzip -d /tmp /tmp/awscli-bundle.zip && \  
/tmp/awscli-bundle/install -i /aws  

