# DockerFile for Centos6 with a working parrot+cvmfs installation.  
#  
# See: github.com/cvmfs/cvmfs and cernvm.cern.ch/portal/filesystem  
# See: github.com/cooperative-computing-lab/cctools and  
# http://ccl.cse.nd.edu/software/manuals/parrot.html  
  
FROM centos:centos6  
MAINTAINER Matteo Concas mconcas@cern.ch  
  
# Environment variables.  
ENV TEST_USER="parrotuser" TEST_USER_HOME="/home/parrotuser" \  
PATH=/opt/cctools/cctools-5.2.3-x86_64-redhat6/bin:$PATH \  
# CCTools  
CCTOOLS_URL=http://ccl.cse.nd.edu/software/files/cctools-5.2.3-x86_64-redhat6.tar.gz
\  
CCTOOLS_PATH=/opt/cctools \  
  
# Compile flag  
MJ=9 \  
# Generic prerequisites, currently deprecated and not installed.  
COMM_REQ="git cmake tar unzip gcc gcc-c++ patch zlib-devel openssl-devel \  
openssl-devel make which vim libcap-2-devel" \  
# Software-specific requisites  
# See: https://dberzano.github.io/install-aliroot  
# Root  
ROOT_REQ="autoconf automake libtool libxml2-devel libX11-devel libXpm-devel \  
libXft-devel libXext-devel mesa-libGLU-devel CGAL-devel subversion" \  
  
# AliRoot  
ALIROOT_REQ="libXpm compat-libgfortran-41 tcl \  
compat-libtermcap redhat-lsb-core" \  
  
# Condor Password  
CONDOR_SECRET="@mycondorpassword@"  
  
# Adding interactive parrot-wrapper, useful for debug and development.  
COPY opt/p_cvmfs_env.sh /home/$TEST_USER/p_cvmfs_env.sh  
COPY opt/cern-it1.cern.ch.pub /etc/cvmfs/keys/cern.ch/cern-it1.cern.ch.pub  
RUN mkdir $CCTOOLS_PATH && \  
mkdir -p /cvmfs/.modulerc && \  
rpm \--import /etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-6 && \  
# Installing prerequisites.  
yum install -y which tar vim git && \  
curl -o $CCTOOLS_PATH/cctools.tar.gz $CCTOOLS_URL && \  
tar -xvf $CCTOOLS_PATH/cctools.tar.gz -C$CCTOOLS_PATH && \  
# Setting up a test user  
useradd -d $TEST_USER_HOME $TEST_USER && \  
chown -R $TEST_USER $TEST_USER_HOME && \  
chown -R $TEST_USER /etc/cvmfs/keys/cern.ch/cern-it1.cern.ch.pub && \  
runuser -l $TEST_USER -c "echo \"alias ali='source
/cvmfs/alice.cern.ch/etc/login.sh'\" \  
>> $TEST_USER_HOME/.bashrc" && \  
# Root & AliRoot stuff  
yum install -y $ROOT_REQ $ALIROOT_REQ  
  
# Condor setup.  
RUN curl -o /etc/yum.repos.d/htcondor-development-rhel6.repo \  
http://research.cs.wisc.edu/htcondor/yum/repo.d/htcondor-development-
rhel6.repo && \  
yum install -y condor  
  
# This tricks the alienv script...  
COPY opt/os-release /etc/os-release  
  
# Pilot injection.  
COPY opt/condor-centos6-worker-pilot /tmp/condor-centos6-worker-pilot  
RUN chmod +x /tmp/condor-centos6-worker-pilot  

