FROM centos:centos7  
  
MAINTAINER Andy Pohl <apohl@morgridge.org>  
  
# HTCondor User details:  
ENV SUBMIT_USER submitter  
ENV GID 1000  
ENV UID 1000  
ENV PASS 123456  
ENV BOSCO_VERSION 1.2.6  
ENV HTCONDOR_VERSION 8.5.7  
# Build in one RUN  
RUN yum -y install \  
bind-utils \  
net-tools \  
openssh-clients \  
libgomp \  
# libgomp seems to be needed since version 1.2.6  
libssh2-devel \  
openssl-devel \  
libcurl-devel \  
ca-certificates \  
git \  
perl \  
rsync \  
sudo \  
wget \  
which \  
yum-utils \  
&& \  
yum clean all && \  
groupadd -g ${GID} ${SUBMIT_USER} && \  
useradd -m -u ${UID} -g ${GID} ${SUBMIT_USER} && \  
usermod -a -G wheel ${SUBMIT_USER} && \  
echo ${PASS} | passwd --stdin ${SUBMIT_USER} && \  
sed -i 's/\\(^Defaults.*requiretty.*\\)/#\1/; \  
s/^\\(%wheel[[:space:]]\\+ALL=(ALL)[[:space:]]\\+ALL[[:space:]]*$\\)/# \1/; \  
s/^#[[:space:]]*\\(%wheel.*NOPASSWD.*$\\)/\1/' /etc/sudoers  
  
USER ${SUBMIT_USER}  
  
RUN cd /home/${SUBMIT_USER} && \  
wget
ftp://ftp.cs.wisc.edu/condor/bosco/${BOSCO_VERSION}/bosco-${BOSCO_VERSION}-x86_64_RedHat7.tar.gz
&& \  
tar xfz bosco-${BOSCO_VERSION}-x86_64_RedHat7.tar.gz && \  
condor-${HTCONDOR_VERSION}-x86_64_RedHat7-stripped/bosco_install && \  
# fixing bosco_cluster. maybe remove this if it's fixed in the future  
sed -i 's/grid_resource = \$grid_res/grid_resource = \"\$grid_res\"/' \  
/home/${SUBMIT_USER}/bosco/bin/bosco_cluster && \  
echo "source ~/bosco/bosco_setenv" >> /home/${SUBMIT_USER}/.bashrc && \  
rm -rf bosco-${BOSCO_VERSION}-x86_64_RedHat7.tar.gz
condor-${HTCONDOR_VERSION}-x86_64_RedHat7-stripped/  
  
RUN sudo yum install -y epel-release && \  
sudo yum install -y 'R-*' && \  
sudo yum clean all && \  
sudo Rscript -e 'install.packages("devtools",
repos="https://cran.rstudio.com/")' && \  
sudo Rscript -e 'devtools::install_github("osg-bosco/GridR")'  
  
VOLUME ["/home/${SUBMIT_USER}/submit"]  
WORKDIR /home/${SUBMIT_USER}/submit  
  
CMD ["bash"]  

