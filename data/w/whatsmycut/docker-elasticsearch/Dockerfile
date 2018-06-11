FROM docker.io/whatsmycut/docker-fedora-systemd:latest  
MAINTAINER mike@whatsmycut.com  
  
# undocumented requirement for docker containers  
ENV container=docker  
# systemd init variables  
ENV init /lib/systemd/systemd  
ENV SYSTEMD_IGNORE_CHROOT=true  
ENV ES_SKIP_SET_KERNEL_PARAMETERS=true  
# get the latest updates  
RUN yum -y update  
  
# Export HTTP & Transport  
EXPOSE 9200 9300  
# Java home var  
ENV JAVA_HOME /usr/bin/java  
  
# Volume for systemd:cgroup  
#VOLUME ['/sys/fs/cgroup:/sys/fs/cgroup:ro']  
# Install Elasticsearch 6.0 with yum  
#RUN find / -name java  
COPY elasticsearch.repo /etc/yum.repos.d/  
  
RUN yum update; yum upgrade -y&& yum -y install sudo which;  
RUN export ES_SKIP_SET_KERNEL_PARAMETERS=true && yum -y install elasticsearch;  
RUN yum -y clean all;  
RUN chkconfig --add elasticsearch;  
RUN echo '>>> elasticsearch installed...'  
  
# Add Elasticsearch to the WORKDIR  
ENV PATH $PATH:/usr/share/elasticsearch:/usr/bin/java  
ENV ES_HOME /usr/share/elasticsearch  
RUN $ES_HOME/bin/elasticsearch-plugin install --batch x-pack  
  
# Copy configuration  
COPY config/* /etc/elasticsearch/  
  
# ES Permissions  
COPY elasticsearch.service /etc/systemd/system/  
  
RUN mkdir -p /data /data/log; \  
chown -R elasticsearch:elasticsearch $ES_HOME; \  
chown -R elasticsearch:elasticsearch /data; \  
chown -R elasticsearch:elasticsearch /etc/elasticsearch; \  
chmod 1644 /etc/systemd/system/elasticsearch.service; \  
chmod -R 1755 /data /etc/elasticsearch;  
#sudo - service /etc/systemd/system/elasticsearch.service start \  
RUN echo "NM_CONTROLLED=no" >> /etc/sysconfig/network-scripts/ifcfg-lo; \  
echo 'BOOTPROTO="static"' >> /etc/sysconfig/network-scripts/ifcfg-lo; \  
echo "NETMASK=255.255.255.0" >> /etc/sysconfig/network-scripts/ifcfg-lo;  
#find / -name elastic*.y*; \  
#cat /etc/sysconfig/network-scripts/ifcfg-lo;  
# Volume for Elasticsearch data  
VOLUME /data  
  
# allow for memlock  
#ulimit -l unlimited  
RUN ls -al /etc/security/limits.d; \  
#echo '* hard nofile 32768' > /etc/security/limits.conf; \  
#echo '* soft nofile 32768' > /etc/security/limits.conf; \  
echo "# allow user 'elasticsearch' mlockall" > /etc/security/limits.conf; \  
echo 'elasticsearch soft memlock unlimited' >> /etc/security/limits.conf; \  
echo 'elasticsearch hard memlock unlimited' >> /etc/security/limits.conf; \  
echo 'elasticsearch - nproc 4096' >> /etc/security/limits.conf; \  
echo 'elasticsearch - nofile 65536' >> /etc/security/limits.conf; \  
echo "# End of file" >> /etc/security/limits.conf; \  
cat /etc/security/limits.conf;  
RUN /sbin/sysctl -p;  
RUN chmod -R 1777 /sys/fs/cgroup/  
RUN mkdir -p /data/log; chmod -R 1777 /data;  
#RUN systemctl start elasticsearch  
RUN echo 'data volumes set. running...'  
# Copy run script and run.  
COPY run.sh /  
#RUN /run.sh  
#RUN cat /usr/lib/systemd/system/elasticsearch.service  
#RUN find / -name elasticsearch.pid  
#ENTRYPOINT [ 'umount /sys/fs/cgroup/systemd', "exec /usr/sbin/init"]  
CMD ["/run.sh"]  
  
#RUN sudo -H -u elasticsearch /bin/sh -c "source /etc/elasticsearch/.env;
ulimit -u 4096; $ES_HOME/bin/elasticsearch"  

