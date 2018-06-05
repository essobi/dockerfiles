# Dockerfile for Rundeck and integration tests  
  
FROM debian:wheezy  
MAINTAINER Oliver Tupman  
  
ENV DEBIAN_FRONTEND=noninteractive \  
SERVER_PORT=4440 \  
SERVER_HOSTNAME=localhost \  
SERVER_URL=http://localhost:4440 \  
RUNDECK_APITOKEN=pFLdEn0FVkIIdTHvpbu19Wq3XttqfAj3 \  
RUNDECK_VERSION=${RUNDECK_VERSION:-"2.7.1-1-GA"} \  
JOB_LOCATION=/tmp/noop_rundeck_job.yml \  
RUNDECK_PROJECTNAME=ci-project \  
ADMIN_PASSWORD=0*820p6{I7  
  
RUN apt-get -qq update && apt-get -qqy upgrade && apt-get -qqy install --no-
install-recommends \  
bash \  
curl \  
supervisor \  
procps \  
sudo \  
ca-certificates \  
openjdk-7-jre-headless \  
openssh-client \  
mysql-server \  
mysql-client \  
pwgen && \  
apt-get clean  
  
ADD run /opt/run  
  
# Download and install Rundeck & then set correct permissions  
RUN curl http://download.rundeck.org/deb/rundeck-$RUNDECK_VERSION.deb -o
/tmp/rundeck.deb && \  
dpkg -i /tmp/rundeck.deb && rm /tmp/rundeck.deb && \  
chown rundeck:rundeck /tmp/rundeck && \  
chmod u+x /opt/run && \  
mkdir -p /var/lib/rundeck/.ssh && \  
chown -R rundeck:rundeck /var/lib/rundeck/ && \  
chown -R rundeck:rundeck /var/log/rundeck && \  
chown -R rundeck:rundeck /var/rundeck  
  
# Supervisor setup for Rundeck & build-in MySQL  
ADD rundeck.conf /etc/supervisor/conf.d/rundeck.conf  
ADD rundeck /opt/supervisor/rundeck  
ADD mysql_supervisor /opt/supervisor/mysql_supervisor  
  
RUN mkdir -p /var/log/supervisor && mkdir -p /opt/supervisor && \  
chmod u+x /opt/supervisor/rundeck && chmod u+x
/opt/supervisor/mysql_supervisor  
  
# Add our pre-defined configuration for Rundeck  
ADD etc/rundeck/tokens.properties /etc/rundeck/tokens.properties  
ADD etc/rundeck/framework.properties /etc/rundeck/framework.properties  
ADD etc/rundeck/apitoken.aclpolicy /etc/rundeck/apitoken.aclpolicy  
  
# Make sure some key rundeck directories are owned correctly  
RUN chown -R rundeck /var/log/rundeck && \  
chown -R rundeck /var/lib/rundeck && \  
sed -ri "s/ADMIN_PASSWORD/$ADMIN_PASSWORD/" /etc/rundeck/framework.properties
&& \  
sed -ri "s,SERVER_URL,$SERVER_URL," /etc/rundeck/framework.properties && \  
sed -ri "s/SERVER_HOSTNAME/$SERVER_HOSTNAME/"
/etc/rundeck/framework.properties && \  
sed -ri "s/SERVER_PORT/$SERVER_PORT/" /etc/rundeck/framework.properties  
  
# Prepare for Rundeck auto-setup (setup DB then create project & import jobs)  
ADD noop_rundeck_job.yml /tmp/noop_rundeck_job.yml  
ADD initialize-db.sh /tmp/initialize-db.sh  
ADD setup-project.sh /tmp/setup-project.sh  
RUN /tmp/initialize-db.sh  
  
# Finally, we add our pre-defined node list (just localhost)  
ADD var.rundeck.project.nodes.xml
/var/rundeck/projects/$RUNDECK_PROJECTNAME/etc/resources.xml  
VOLUME /var/lib/mysql  
EXPOSE 4440 4443  
  
# Start Supervisor  
CMD ["/opt/run"]  

