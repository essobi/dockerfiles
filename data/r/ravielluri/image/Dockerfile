#Dockerfile for pbench-controller  
FROM centos/tools  
MAINTAINER Naga Ravi Chaitanya Elluri <nelluri@redhat.com>  
  
ENV KUBECONFIG /root/.kube/config  
  
# Setup pbench, sshd, pbench-ansible, svt and install dependencies  
RUN yum clean all && rpm -ivh https://dl.fedoraproject.org/pub/epel/epel-
release-latest-7.noarch.rpm && \  
curl -s https://copr.fedorainfracloud.org/coprs/ndokos/pbench-
interim/repo/epel-7/ndokos-pbench-interim-epel-7.repo > /etc/yum.repos.d/copr-
pbench.repo && \  
curl -s https://packagecloud.io/install/repositories/github/git-
lfs/script.rpm.sh | bash && \  
yum --enablerepo=ndokos-pbench-interim install -y configtools openssh-clients
pbench-agent \  
iproute sysvinit-tools openssh-server git ansible which bind-utils blktrace
ethtool findutils \  
gnuplot golang httpd-tools hwloc iotop iptables-services kernel ltrace mailx
maven netsniff-ng \  
net-tools ntp ntpdate numactl pciutils perf python-docker-py python-flask
python-pip python-rbd \  
python2-boto3 powertop psmisc rpm-build screen sos strace tar tcpdump tmux
vim-enhanced xauth wget git-lfs \  
yum-utils rpmdevtools ceph-common glusterfs-fuse iscsi-initiator-utils
openssh-server openssh-clients initscripts && \  
yum clean all && \  
source /etc/profile.d/pbench-agent.sh && \  
mkdir -p /root/.go && echo "GOPATH=/root/.go" >> ~/.bashrc && \  
echo "export GOPATH" >> ~/.bashrc && \  
echo "PATH=\$PATH:\$GOPATH/bin" >> ~/.bashrc && \  
source ~/.bashrc && \  
mkdir -p /root/.ssh && \  
curl -L
https://github.com/openshift/origin/releases/download/v1.2.1/openshift-origin-
client-tools-v1.2.1-5e723f6-linux-64bit.tar.gz | tar -zx && \  
mv openshift*/oc /usr/local/bin && \  
rm -rf openshift-origin-client-tools-* && \  
git clone https://github.com/distributed-system-analysis/pbench.git
/root/pbench && \  
git clone https://github.com/openshift/svt.git /root/svt && \  
mkdir -p /usr/libexec/atomic-openshift && \  
#git clone https://github.com/chaitanyaenr/files.git /root/files && \  
#cd /root/files && git-lfs pull && \  
#mv /root/files/extended.test /root/extended.test && \  
mv /opt/pbench-agent/config/pbench-agent.cfg.example /opt/pbench-
agent/config/pbench-agent.cfg && \  
sed -i "s/#Port 22/Port 2022/" /etc/ssh/sshd_config && \  
touch /etc/sysconfig/network && \  
systemctl enable sshd  
  
# Expose ports  
EXPOSE 2022 9090  
  
# Run pbench as a service  
COPY pbench.service /etc/systemd/system/pbench.service  
COPY run.sh /root/run.sh  
RUN chmod +x /root/run.sh  
RUN systemctl enable pbench.service  
ENTRYPOINT ["/usr/sbin/init"]  

