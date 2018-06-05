FROM docker.io/centos  
  
MAINTAINER <christophe.gattardi@gmail.com>  
  
ENV JAVA_VERSION=1.8.0 \  
JSVER=1.9.11  
RUN yum install -y \  
java-${JAVA_VERSION}-openjdk \  
patch \  
postgresql \  
&& yum clean all  
  
RUN export JSURL='https://download.sos-berlin.com/JobScheduler.1.9'; \  
export JSARCHIVE="jobscheduler_linux-x64.${JSVER}.tar.gz"; \  
mkdir -p /tmp/install \  
&& mkdir -p /app \  
&& cd /tmp/install \  
&& curl -sSLf -O ${JSURL}/${JSARCHIVE} \  
&& tar xpf $JSARCHIVE \  
&& rm -f $JSARCHIVE \  
&& cd jobscheduler.$JSVER \  
&& mv setup.sh jobscheduler_linux-x64.${JSVER}.jar /app/ \  
&& rm -rf /tmp/install  
  
EXPOSE 4444  
ENTRYPOINT ["/app/entrypoint.sh"]  
  
CMD ["/opt/sos-berlin.com/jobscheduler/current/bin/jobscheduler.sh", "execfg"]  
  
COPY entrypoint.sh jobscheduler_install.$JSVER.xml jobscheduler.sh.patch
jobscheduler_environment_variables.sh.patch /app/  
  
RUN chmod 755 /app/*.sh  

