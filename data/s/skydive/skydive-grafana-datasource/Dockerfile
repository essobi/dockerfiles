FROM centos  
ENV container docker  
  
RUN yum -y update; yum clean all  
RUN yum -y install systemd; yum clean all; \  
(cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == systemd-
tmpfiles-setup.service ] || rm -f $i; done); \  
rm -f /lib/systemd/system/multi-user.target.wants/*;\  
rm -f /etc/systemd/system/*.wants/*;\  
rm -f /lib/systemd/system/local-fs.target.wants/*; \  
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \  
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \  
rm -f /lib/systemd/system/basic.target.wants/*;\  
rm -f /lib/systemd/system/anaconda.target.wants/*;  
RUN yum install -y https://s3-us-west-2.amazonaws.com/grafana-
releases/release/grafana-4.4.1-1.x86_64.rpm epel-release git make gcc-c++; yum
install -y nodejs npm; yum clean all;  
RUN git clone https://github.com/skydive-project/skydive-grafana-
datasource.git; \  
cd skydive-grafana-datasource; \  
npm install; \  
./node_modules/grunt-cli/bin/grunt; \  
mkdir -p /var/lib/grafana/plugins; \  
ln -s `pwd`/dist /var/lib/grafana/plugins/skydive-grafana-datasource;  
RUN systemctl enable grafana-server  
  
#build :  
# docker build --rm -t centos7-systemd-grafana-skydive .  
#run the container with :  
# docker run --privileged --network="host" -p 3000:3000 -ti -e
container=docker -v /run -v /sys/fs/cgroup:/sys/fs/cgroup:ro --name grafana
centos7-systemd-grafana-skydive /usr/sbin/init  

