# Run OrientDB Docker Container as follows:  
#  
# --name="" Assign a name to the container  
# -d, --detach=false Detached mode: run the container in the background and
print the new container ID  
# -p, --publish=[] Publish a container's port to the host  
#  
# docker run --name orientdb -d -p 2480:2480 -p 2424:2424
lighthopper/orientdb-centos:2.0.7  
FROM lighthopper/openjdk-centos:1.7.0-jre  
MAINTAINER Esen Sagynov <kadishmal@gmail.com>  
  
RUN yum install -y tar  
  
# install orientdb  
ENV ROOT /opt  
ENV ORIENT_SNAPSHOT_VERSION 2.0.7-SNAPSHOT  
ENV ORIENT_REPO_NAME orientdb-community  
ENV ORIENT_VERSION ${ORIENT_REPO_NAME}-${ORIENT_SNAPSHOT_VERSION}  
ENV ORIENT_TAR ${ORIENT_VERSION}.tar.gz  
ENV ORIENT_URL
https://oss.sonatype.org/content/repositories/snapshots/com/orientechnologies/${ORIENT_REPO_NAME}/${ORIENT_SNAPSHOT_VERSION}/${ORIENT_REPO_NAME}-2.0.7-20150414.041700-16-distribution.tar.gz  
  
RUN cd ${ROOT} \  
&& curl -o ${ORIENT_TAR} ${ORIENT_URL} \  
&& tar -xzf ${ORIENT_TAR} \  
&& ln -s ${ROOT}/${ORIENT_VERSION} ${ROOT}/orientdb \  
&& ln -s ${ROOT}/orientdb/bin/*.sh /usr/local/bin/ \  
&& mkdir /usr/local/log  
  
# cleanup  
RUN rm -rf ${ROOT}/${ORIENT_TAR} /tmp/* /var/tmp/*  
  
CMD ["/usr/local/bin/server.sh"]  

