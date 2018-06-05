FROM centos:latest  
MAINTAINER "Kostiantyn Iarovyi" <kiarovyi@cisco.com>  
  
# ++++ Set Environmental variables  
ENV container docker  
ENV CONSUL_VERSION 0.6.4  
#ENV AMBARI_REPO_URL http://public-
repo-1.hortonworks.com/ambari/centos7/2.x/updates/2.2.0.0/ambari.repo  
#ENV AMBARI_REPO_URL http://128.107.33.156/repo/7/Ambari-
trunk/RPMS/ambari.repo  
ENV AMBARI_REPO_URL http://128.107.33.156/repo/7/ambari/2.2.0/RPMS/ambari.repo  
ENV JDK jdk-8u60-linux-x64.tar.gz  
ENV JDK_VER jdk1.8.0_60  
ENV JAVA_HOME /usr/jdk64/$JDK_VER/  
ENV PATH $PATH:$JAVA_HOME/bin  
ENV PGDATA /var/lib/pgsql/data  
# ++++ Fix systemd issues  
RUN yum -y update; yum clean all; \  
(cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == \  
systemd-tmpfiles-setup.service ] || rm -f $i; done); \  
rm -f /lib/systemd/system/multi-user.target.wants/*;\  
rm -f /etc/systemd/system/*.wants/*;\  
rm -f /lib/systemd/system/local-fs.target.wants/*; \  
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \  
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \  
rm -f /lib/systemd/system/basic.target.wants/*;\  
rm -f /lib/systemd/system/anaconda.target.wants/*;  
VOLUME [ "/sys/fs/cgroup" ]  
ENTRYPOINT ["/usr/sbin/init"]  
  
# ++++ Install packages  
RUN yum -y install wget && \  
wget $AMBARI_REPO_URL -O /etc/yum.repos.d/ambari.repo && \  
yum -y install epel-release python-pip curl tar initscripts unzip ambari-
server openssh-clients dnsmasq  
  
# ++++ Install Java 8  
RUN mkdir /usr/jdk64 && \  
cd /usr/jdk64 && \  
wget http://public-repo-1.hortonworks.com/ARTIFACTS/$JDK && \  
tar -xf $JDK && \  
rm -f $JDK  
RUN wget http://public-repo-1.hortonworks.com/ARTIFACTS/jce_policy-8.zip -P
/var/lib/ambari-server/resources/ && \  
cd /var/lib/ambari-server/resources && \  
unzip jce_policy-8.zip && \  
rm -f jce_policy-8.zip && \  
mv UnlimitedJCEPolicyJDK8/*.jar . && \  
rm -rf UnlimitedJCEPolicyJDK8  
  
# Download Pangea stacks and views (MANTL & Kubernetes) and unpack them  
RUN wget http://128.107.33.156/repo/7/mantl.tar.gz -P /var/lib/ambari-
server/resources/stacks/  
RUN wget http://128.107.33.156/repo/ambari-views.tar.gz -P /var/lib/ambari-
server/resources/views/  
RUN wget http://128.107.33.156/repo/7/pangea_kubernetes.tar.gz -P
/var/lib/ambari-server/resources/stacks/  
RUN wget http://128.107.33.156/repo/7/pangea_kubernetes_views.tar.gz -P
/var/lib/ambari-server/resources/views/  
RUN cd /var/lib/ambari-server/resources/stacks && for file in *.tar.gz; do tar
-zxf $file; done && rm -rf *.tar.gz && \  
cd /var/lib/ambari-server/resources/views && for file in *.tar.gz; do tar -zxf
$file; done && rm -rf *.tar.gz  
  
# Pre-start postgresql with some minor patches  
COPY ./service-stub.sh /usr/bin/  
RUN sed -i 's/\/usr\/bin\/env service/\/usr\/bin\/service-stub.sh/g' \  
/usr/lib/python2.6/site-packages/ambari_server/dbConfiguration_linux.py && \  
sed -i 's/exit 1/PGDATA=\/var\/lib\/pgsql\/data; PGPORT=5432/g' \  
/usr/bin/postgresql-setup && service-stub.sh postgresql initdb && service-
stub.sh postgresql start  
  
# Run Ambari setup  
RUN ambari-server setup -s -j /usr/jdk64/$JDK_VER/  
  
# Patch Ambari Zookeeper common service to let it function properly when
inherited in stack other than HDP  
RUN sed -i 's/if Script.is_hdp_stack_greater_or_equal.*$/if config:/g' \  
/var/lib/ambari-server/resources/common-
services/ZOOKEEPER/3.4.5.2.0/package/scripts/params_linux.py  
# Install & pre-configure Consul server & DNSMASQ  
RUN yum install -y consul consul-ui  
ADD ./consul.json /etc/consul/consul.json  
RUN touch /etc/dnsmasq.d/10-consul && chmod 777 /etc/dnsmasq.d/10-consul && \  
echo "server=/consul/127.0.0.1#8600" > /etc/dnsmasq.d/10-consul && \  
echo "server=/consul/in-addr.arpa/127.0.0.1#8600" >> /etc/dnsmasq.d/10-consul
&& \  
(echo "server=8.8.8.8"; echo "server=8.8.4.4") >> /etc/dnsmasq.d/10-consul &&
\  
chsh -s /bin/bash consul  
  
ADD ./ifup-local.sh /sbin/ifup-local  
RUN chmod +x /sbin/ifup-local  
  
# Enable services that need to be running when container starts (Consul,
Ambari, DNSMASQ)  
ADD ./ambari-server.service /usr/lib/systemd/system/  
RUN systemctl enable consul && \  
systemctl enable ambari-server && \  
systemctl enable dnsmasq  
  
# Expose ports  
EXPOSE 8080 6181 53 8500 8400 8300 8301 8302

