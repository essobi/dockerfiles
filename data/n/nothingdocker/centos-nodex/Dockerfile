# Version 1.0.0  
FROM nothingdocker/centos-node  
ENV MONGODB_VER 3.4  
RUN echo -e "\n\  
[mongodb-org-3.4]\n\  
name=MongoDB Repository\n\  
baseurl=https://repo.mongodb.org/yum/redhat/\$releasever/mongodb-
org/3.4/x86_64/\n\  
gpgcheck=1\n\  
enabled=1\n\  
gpgkey=https://www.mongodb.org/static/pgp/server-3.4.asc\n\  
" >> /etc/yum.repos.d/mongodb-org-3.4.repo \  
&& yum install -y mongodb-org \  
&& yum clean all \  
&& systemctl enable mongod.service  
RUN mkdir -p /var/lib/mongo \  
&& mkdir -p /var/log/mongod \  
&& chown -R mongod:mongod /var/lib/mongo \  
&& chown -R mongod:mongod /var/log/mongodb  
VOLUME /var/lib/mongo /var/log/mongodb  
RUN yum install -y redis \  
&& yum clean all \  
&& systemctl enable redis.service  
  
COPY mongod.conf /etc/mongod.conf  
COPY entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["/usr/sbin/init"]  

