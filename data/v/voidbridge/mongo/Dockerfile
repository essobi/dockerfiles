FROM voidbridge/centos7  
MAINTAINER Voidbridge <developers@voidbridge.com>  
  
LABEL io.k8s.description="MongoDB database" \  
io.k8s.display-name="MongoDB"  
  
# Install Mongo package  
ADD files/etc/yum.repos.d /etc/yum.repos.d  
RUN yum install -y --enablerepo=centosplus gettext epel-release && \  
yum install -y mongodb-org hostname bind-utils python-pip && \  
pip install j2cli && \  
yum clean all -y && \  
find /var/log/mongodb /var/lib/mongo -type d -exec chmod 777 {} + && \  
find /var/log/mongodb /var/lib/mongo -type f -exec chmod 666 {} + && \  
chmod 666 /etc/mongod.conf  
  
ADD files /  
ADD templates /tmp/templates  
RUN chmod 755 /usr/bin/run-mongod  
  
ENV MONGO_ENGINE_CACHE_FRACTION=0.5  
USER 184  
EXPOSE 5432  
VOLUME /mnt/data  
CMD ["run-mongod"]  

