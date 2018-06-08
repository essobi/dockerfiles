# DockerFile for SL6 with a working parrot+cvmfs installation + HTCondor
worker node  
# + Ready to install IceCube software using system packages  
#  
#  
# cern/slc6-base:20160405 is Scientific Linux 6.8 image from CERN  
# http://cern.ch/linux/scientific6/  
#  
# Scientific Linux CERN 5 is a Linux distribution build within the framework
of Scientific Linux  
# which in turn is rebuilt from the freely available Red Hat Enterprise Linux
6 (Server) product  
# sources under terms and conditions of the Red Hat EULA. Scientific Linux
CERN is built to integrate  
# into the CERN computing environment but it is not a site-specific product:
all CERN site  
# customizations are optional and can be deactivated for external users.  
#  
  
FROM cern/slc6-base:20161206  
  
MAINTAINER Tomasz Palczewski TPalczewski@lbl.gov  
  
#--- Environment variables  
ENV TEST_USER="testuser"  
ENV TEST_USER_HOME='/home/testuser"  
  
ENV PATH=/opt/cctools/cctools-5.2.3-x86_64-redhat/bin:$PATH  
# CCTOOLS  
ENV
CCTOOLS_URL=http://ccl.cse.nd.edu/software/files/cctools-5.2.3-x86_64-redhat6.tar.gz
\  
CCTOOLS_PATH=/opt/cctools  
# Compile flag  
ENV MJ=4  
# Comm Req  
ENV COMM_REQ="git cmake tar unzip gcc gcc-c++ patch zlib-devel openssl-devel \  
openssl-devel make which vim libcap-2-devel wget xz"  
# Root  
ENV ROOT_REQ="autoconf automake libtool libxml2-devel libX11-devel libXpm-
devel \  
libXft-devel libXext-devel mesa-libGLU-devel CGAL-devel subversion"  
# AliRoot  
ENV ALIROOT_REQ="libXpm compat-libgfortran-41 tcl \  
compat-libtermcap redhat-lsb-core"  
# IceCube  
ENV ICECUBE_REQ="compat-gcc-34-g77 bzip2-devel doxygen expat-devel freeglut-
devel gcc gcc-c++ \  
gcc-gfortran.$ARCH libX11-devel libXext-devel libXfixes-devel libXft-devel
libXi-devel \  
libXmu-devel libXpm-devel libXrandr-devel libXt-devel libxml2-devel freetype-
devel \  
ncurses-devel openssl-devel openssh-clients pcre-devel python-devel python-
setuptools \  
rpm-build rsync subversion tcl-devel texinfo vim wget python-urwid"  
  
ENV SSH_REQ="openssh openssh-server screen" \  
  
ENV_PYTHON27_REQ="zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-
devel \  
readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-utils xz-devel"  
  
#--- End of Environment variables  
  
# Initialize the log files and give them proper permissions  
RUN touch /var/run/utmp /var/log/{btmp,lastlog,wtmp} && \  
chgrp -v utmp /var/run/utmp /var/log/lastlog && \  
chmod -v 664 /var/run/utmp /var/log/lastlog  
  
# Install common req  
RUN yum install -y $COMM_REQ  
RUN yum groupinstall -y "Development tools"  
  
# Install python 2.7 ( in /usr/local/bin/python2.7); the The system version of
Python 2.6.6 will  
# continue to be available as /usr/bin/python, /usr/bin/python2 and
/usr/bin/python2.6  
  
RUN yum install -y $ENV_PYTHON27_REQ  
RUN cd /  
RUN wget http://python.org/ftp/python/2.7.6/Python-2.7.6.tar.xz  
RUN tar xf Python-2.7.6.tar.xz  
RUN cd /Python-2.7.6 && \  
./configure --prefix=/usr/local \--enable-unicode=ucs4 --enable-shared
LDFLAGS="-Wl,-rpath /usr/local/lib" &&\  
make && make altinstall  
RUN cd /  
RUN rm -rf Python-2.7.6.tar.xz  
  
# Install Python Python 3.4.5 (in /usr/local/bin/python3.3); The system
version of Python 2.6.6 will  
# continue to be available as /usr/bin/python, /usr/bin/python2 and
/usr/bin/python2.6  
  
RUN wget http://python.org/ftp/python/3.4.5/Python-3.4.5.tar.xz  
RUN tar xf Python-3.4.5.tar.xz  
RUN cd /Python-3.4.5 && \  
./configure --prefix=/usr/local \--enable-shared LDFLAGS="-Wl,-rpath
/usr/local/lib" && \  
make && make altinstall  
RUN cd /  
RUN rm -rf Python-3.4.5.tar.xz  
  
# install pip  
RUN yum install -y python-pip python-wheel  
RUN pip install --upgrade pip  
RUN easy_install -U distribute  
  
# install pip2.7  
# install pip3.4  
RUN wget --no-check-certificate https://bootstrap.pypa.io/ez_setup.py  
RUN python2.7 ez_setup.py  
RUN python3.4 ez_setup.py  
# Now install pip using the newly installed setuptools:  
RUN easy_install-2.7 pip  
RUN easy_install-3.4 pip  
  
RUN yum install -y python-setuptools  
RUN yum upgrade python-setuptools  
  
# install req for numpy and scipy  
RUN yum groupinstall -y "Development Tools"  
RUN yum install -y blas blas-devel lapack lapack-devel atlas atlas-devel
python-devel  
  
# install numpy, scipy, matplotlib, ...  
  
RUN pip2.7 install urllib3  
RUN pip2.7 install numpy  
RUN pip2.7 install scipy  
RUN pip2.7 install matplotlib  
RUN pip2.7 install -U scikit-learn  
RUN pip2.7 install pandas  
  
RUN pip3.4 install urllib3  
RUN pip3.4 install numpy  
RUN pip3.4 install scipy  
RUN pip3.4 install matplotlib  
RUN pip3.4 install -U scikit-learn  
RUN pip3.4 install pandas  
  
RUN yum install -y $SSH_REQ  
RUN yum install -y redhat-lsb-core  
RUN yum install -y redhat-lsb  
  
RUN export DISTRO=$(lsb_release -si) && \  
export VERSION=$(lsb_release -sr) && \  
export ARCH=$(uname -m)  
  
RUN yum install -y $ICECUBE_REQ  
RUN mkdir -p $CCTOOLS_PATH && \  
mkdir -p /cvmfs/.modulerc && \  
curl -o $CCTOOLS_PATH/cctools.tar.gz $CCTOOLS_URL && \  
tar -xvf $CCTOOLS_PATH/cctools.tar.gz -C$CCTOOLS_PATH  
  
# Setting up a test user  
RUN adduser $TEST_USER -d $TEST_USER_HOME  
RUN chown -R $TEST_USER $TEST_USER_HOME  
  
# Root & AliRoot stuff (Icecube dosen't like root though)  
RUN yum install -y $ROOT_REQ $ALIROOT_REQ  
  
# Condor setup  
RUN curl -o /etc/yum.repos.d/htcondor-development-rhel6.repo \  
http://research.cs.wisc.edu/htcondor/yum/repo.d/htcondor-development-
rhel6.repo && \  
yum install -y condor  
  
#------------  
#  
# IceCube Software  
#  
#------------  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

