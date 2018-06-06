FROM centos:7  
# HACK! for some reason $releasever is not working, so fixing to "7" in
https://repo.mongodb.org/yum/redhat/$releasever/mongodb-org/3.0/x86_64/  
RUN printf "[mongodb-org-3.0]\n\  
name=MongoDB Repository\n\  
baseurl=https://repo.mongodb.org/yum/redhat/7/mongodb-org/3.0/x86_64/\n\  
gpgcheck=0\n\  
enabled=1" > /etc/yum.repos.d/mongodb-org-3.0.repo  
  
RUN set -x \  
&& yum update -y \  
&& yum install -y \  
mongodb-org \  
mongodb-org-server \  
mongodb-org-shell \  
mongodb-org-mongos \  
mongodb-org-tools \  
&& mv /etc/mongod.conf /etc/mongod.conf.orig \  
&& mkdir -p /data/db && chown -R mongod:mongod /data/db  
  
VOLUME /data/db  
  
COPY docker-entrypoint.sh /entrypoint.sh  
RUN chown mongod:mongod /entrypoint.sh \  
&& chmod u+x /entrypoint.sh \  
&& touch /etc/mongod.conf  
  
EXPOSE 27017  
RUN curl -L https://github.com/tianon/gosu/releases/download/1.6/gosu-amd64 -o
/usr/local/sbin/gosu; \  
chmod +x /usr/local/sbin/gosu  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["mongod"]  

