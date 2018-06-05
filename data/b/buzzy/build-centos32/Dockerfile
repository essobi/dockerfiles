FROM redjack/centos32:5  
RUN linux32 yum -y groupinstall "Development Tools" \  
&& linux32 yum clean packages  
RUN linux32 yum -y install epel-release \  
&& linux32 yum clean packages  
RUN linux32 yum -y install \  
cmake28 \  
git \  
python \  
ssh \  
sudo \  
&& linux32 yum clean packages  
# Use cmake28 from EPEL  
RUN update-alternatives --install /usr/local/bin/cmake cmake /usr/bin/cmake28
10 \  
&& update-alternatives --set cmake /usr/bin/cmake28  
  
# Use devtools2 for newer GCC and ld. Note that we use this rather than gcc44  
# and g++44 from EPEL because we need the newer 'ld' executable to link
against  
# libcork.  
RUN rpm --import http://ftp.scientificlinux.org/linux/scientific/5x/i386/RPM-
GPG-KEYs/RPM-GPG-KEY-cern \  
&& curl -L -f http://linuxsoft.cern.ch/cern/devtoolset/slc5-devtoolset.repo -o
/etc/yum.repos.d/devtools-2.repo  
RUN linux32 yum -y install devtoolset-2  
  
# Download and install check 0.9.8: 0.9.3 (present in RHEL 5) is too old to  
# build our software. 0.9.8 is in RHEL 6, so it seems like a safe version for  
# compatibility.  
RUN mkdir -p /tmp/check \  
&& cd /tmp/check \  
&& curl -O -L -f
https://downloads.sourceforge.net/project/check/check/0.9.8/check-0.9.8.tar.gz
\  
&& tar zxf check-0.9.8.tar.gz \  
&& cd check-0.9.8 \  
&& ./configure \  
&& make \  
&& make install \  
&& rm -rf /tmp/check  
  
ENV PKG_CONFIG_PATH /usr/local/lib/pkgconfig  
  
COPY sudoers /etc/sudoers  
RUN chmod 0440 /etc/sudoers  
  
RUN useradd -m -G wheel buzzy  
  
RUN mkdir /home/buzzy/.ssh \  
&& chown buzzy:buzzy /home/buzzy/.ssh \  
&& chmod 0700 /home/buzzy/.ssh \  
&& ssh-keyscan github.com >> /home/buzzy/.ssh/known_hosts \  
&& chown buzzy:buzzy /home/buzzy/.ssh/known_hosts \  
&& chmod 0600 /home/buzzy/.ssh/known_hosts  
  
USER buzzy  
ENV HOME /home/buzzy  
WORKDIR /home/buzzy  
  
# Execute linux32 with devtoolset-2 enabled  
ADD entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["bash"]  

