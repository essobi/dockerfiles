# Builds an OpenSuse 12 based docker with a fully working Synthese server
using MySQL  
# Dev tools installed  
# VPN installed and setup  
# MySQL root password : synthese_root  
# MySQL synthese password : synthese  
# root password : toto  
# To run it as the master :  
# docker run -i -t -p 1194:1194/udp --privileged -v /dev/net/tun:/dev/net/tun
opensuse12-distcc master  
FROM flavio/opensuse-12-3  
MAINTAINER Bastien Noverraz (TL)  
  
# Update  
RUN zypper --non-interactive --no-gpg-checks update -y --auto-agree-with-
licenses && \  
zypper clean  
  
# Install necessary librairies  
RUN \  
zypper --non-interactive --no-gpg-checks install -y --auto-agree-with-licenses
\  
wget pv unzip libopenssl0_9_8 glibc-locale sudo make nano ccache automake
libtool \  
&& \  
zypper clean  
  
# Adding the 11.1 repo for GCC 4.3  
RUN echo -e " \  
[openSUSE_11.1] \n\  
name=openSUSE_11.1 \n\  
baseurl=http://download.opensuse.org/distribution/11.1/repo/oss/ \n\  
type=yast2 \n\  
enabled=1 \n\  
autorefresh=0 \n\  
gpgcheck=1" > /etc/zypp/repos.d/openSUSE_11.1.repo  
  
# Install GCC 4.3  
RUN zypper --non-interactive --no-gpg-checks install -y --auto-agree-with-
licenses gcc43 gcc43-c++ gcc43-info gcc43-locale && \  
zypper clean && \  
cd /usr/bin && \  
ln -s gcc-4.3 gcc && \  
ln -s g++-4.3 g++ && \  
ln -s gcc-4.3 cc && \  
ln -s cpp-4.3 cpp && \  
ln -s g++-4.3 c++ && \  
ln -s gcov-4.3 gcov  
  
# Disable the old repo, to avoid old software  
RUN sed -i 's/enabled=1/enabled=0/g' /etc/zypp/repos.d/openSUSE_11.1.repo  
  
# Install and enable distcc  
RUN zypper --non-interactive --no-gpg-checks install -y --auto-agree-with-
licenses \  
avahi avahi-utils dbus-1 \  
http://download.opensuse.org/repositories/home:/mayerjosua:/Server/openSUSE_12.3/x86_64/distcc-3.2rc1-8.1.x86_64.rpm
&& \  
zypper clean && \  
mkdir -p /usr/lib64/distcc && \  
cd /usr/lib64/distcc && \  
ln -s /usr/bin/distcc gcc && \  
ln -s /usr/bin/distcc g++ && \  
ln -s /usr/bin/distcc cc && \  
ln -s /usr/bin/distcc c++ && \  
ln -s /usr/bin/distcc cpp && \  
/etc/init.d/dbus stop && \  
/etc/init.d/avahi-daemon stop && \  
/etc/init.d/avahi-dnsconfd stop  
  
# Enable distcc  
ENV PATH $PATH:/usr/lib64/distcc  
ENV CC distcc cc  
ENV CXX distcc c++  
ENV DISTCC_HOSTS +zeroconf  
ENV DISTCC_DIR /tmp  
  
# Install and configure OpenVPN  
RUN zypper --non-interactive --no-gpg-checks install -y --auto-agree-with-
licenses openvpn openvpn-auth-pam-plugin && \  
zypper clean  
  
# Copy the server keys and configs  
ADD openvpn /etc/openvpn  
RUN mkdir -p /dev/net  
  
# Setup the root password  
RUN echo root:toto | chpasswd  
  
# Add a user for distcc  
RUN useradd -m distcc  
  
# Use our starter by default  
ENTRYPOINT ["/opt/bin/env.sh"]  
  
# By default, start bash  
CMD bash  
  
# Add our own script to the path  
ENV PATH $PATH:/opt/bin  
  
# Add our starter  
ADD env.sh /opt/bin/env.sh  

