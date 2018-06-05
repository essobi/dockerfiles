# add a base image  
FROM centos:7  
  
ENV CRCBASE_HOME=/model \  
CRCBASE_USER=crcuser \  
CRCBASE_UID=979 \  
CRCBASE_GROUP=crcuser \  
CRCBASE_GID=979  
  
# install necessary packages  
RUN yum install -y epel-release \  
expat expat-devel \  
which \  
perl ruby \  
wget git \  
autoconf flex bison pkgconfig \  
install cmake make gcc gcc-c++ gcc-gfortran \  
libtool libtool-ltdl-devel \  
zip unzip \  
openmpi openmpi-devel.x86_64 \  
openssh-clients openssh-server \  
tcl tcl-devel \  
netcdf-devel \  
libjpeg libxml2 \  
glib2-devel \  
ncurses-devel ncurses  
  
ENV PATH $PATH:/usr/lib64/openmpi/bin  
ENV LD_LIBRARY_PATH $LD_LIBRARY_PATH:/usr/lib64/openmpi/lib  
  
RUN mkdir $CRCBASE_HOME  
RUN groupadd -r $CRCBASE_GROUP -g $CRCBASE_GID && \  
useradd -u $CRCBASE_UID -r -g $CRCBASE_USER -d $CRCBASE_HOME -s /sbin/nologin
-c "Docker image user" $CRCBASE_USER && \  
chown -R $CRCBASE_USER:$CRCBASE_GROUP $CRCBASE_HOME  

