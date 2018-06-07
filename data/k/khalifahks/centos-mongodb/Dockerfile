FROM centos:centos7  
  
# For details see:  
# https://docs.mongodb.com/manual/tutorial/install-mongodb-on-red-
hat/#install-mongodb-community-edition  
ADD ./mongodb-34-org.repo /etc/yum.repos.d/mongodb-34-org.repo  
  
RUN yum -y install https://dl.fedoraproject.org/pub/epel/epel-release-
latest-7.noarch.rpm \  
# Import the GPG key  
&& rpm --import \  
/etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7 \  
/etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-7 \  
  
&& yum -y update \  
# Install MongoDB.  
&& yum -y install mongodb-org \  
&& yum clean all  
  
ADD ./mongodb-34.conf /etc/mongod.conf  
  
EXPOSE 27017  
ENTRYPOINT ["/usr/bin/mongod"]  
  
# docker build -t khalifahks/centos-mongodb ./centos7-mongodb  
# docker run -d --rm -p 27017:27017 --name centos-mongodb -h centos_mongodb
khalifahks/centos-mongodb  
# docker run -it --rm -p 27017:27017 --name centos-mongodb -h centos_mongodb
khalifahks/centos-mongodb

