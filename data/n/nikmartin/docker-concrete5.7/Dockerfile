FROM centurylink/apache-php:latest  
MAINTAINER CenturyLink  
  
# Install packages  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get -y upgrade && \  
DEBIAN_FRONTEND=noninteractive apt-get -y install supervisor pwgen unzip && \  
apt-get -y install mysql-client  
  
# Download Concrete5.7 into /app  
RUN rm -fr /app && mkdir /app && \  
curl -O http://www.concrete5.org/download_file/-/view/74619 && \  
unzip 74619 -d /tmp && \  
cp -a /tmp/concrete*/. /app && \  
rm -rf /tmp/concrete* && \  
rm 74619  
# Add script to create 'concrete5' DB  
ADD run.sh run.sh  
RUN chmod 755 /*.sh  
RUN mkdir -p /var/www/html/application/config/ && \  
mkdir -p /var/www/html/application/files/ && \  
mkdir -p /var/www/html/packages/  
RUN chmod -R 777 /var/www/html/application/config/
/var/www/html/application/files/ /var/www/html/packages/  
  
EXPOSE 80  
CMD ["/run.sh"]  

