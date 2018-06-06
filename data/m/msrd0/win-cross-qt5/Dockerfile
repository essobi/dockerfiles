FROM debian  
  
RUN apt-get -y update && apt-get -y install --no-install-recommends \  
bzip2 \  
ca-certificates \  
dirmngr \  
git \  
grep \  
gnupg \  
make \  
sed \  
sudo \  
xz-utils \  
&& echo "deb http://pkg.mxe.cc/repos/apt/debian jessie main" | tee
/etc/apt/sources.list.d/mxe.list \  
&& apt-key adv --keyserver keyserver.ubuntu.com --recv-keys
D43A795B73B16ABE9643FE1AFD8FFF16DB45C6AB \  
&& apt-get -y update && apt-get -y install --no-install-recommends \  
mxe-i686-w64-mingw32.static-qtbase \  
&& mkdir -p /etc/sudoers.d \  
&& useradd -m -d /home/user user \  
&& echo 'user ALL=(ALL) NOPASSWD:ALL' >/etc/sudoers.d/user \  
&& rm -rf /var/lib/apt/lists/*  
ENV PATH /usr/lib/mxe/usr/bin:$PATH  
  
USER user  
ENV HOME /home/user  
WORKDIR /home/user  
CMD ["/bin/bash"]  

