#  
# Dockerfile for Optware-ng Compile ENV  
#  
FROM ubuntu:14.04  
MAINTAINER tofuliang@gmail.com  
  
RUN apt-get update && apt-get -y install software-properties-common openssh-
server bc \  
# add-apt-repository -y ppa:saiarcot895/myppa  
# apt-get update  
# apt-get -y install apt-fast  
&& apt-get -y install ant build-essential git subversion cvs openjdk-7-jre
openjdk-7-jdk texinfo m4 libglib2.0-dev flex bison yasm libxml2-dev ruby
intltool unicode-data rcs gperf python-mako scons itstool libxml2-utils icon-
naming-utils g++-multilib doxygen libgdk-pixbuf2.0-dev txt2man xmlto xsltproc
docbook docbook-xsl asciidoc gcj-jdk cmake libncurses5-dev libx11-dev
fakechroot \  
&& echo debconf shared/accepted-oracle-license-v1-1 select true |debconf-set-
selections \  
&& echo debconf shared/accepted-oracle-license-v1-1 seen true |debconf-set-
selections \  
&& add-apt-repository -y ppa:webupd8team/java && apt-get update && apt-get -y
install oracle-java8-installer \  
&& cd /usr/local/src/ && wget
http://ftp.gnu.org/gnu/texinfo/texinfo-4.13a.tar.gz -O- |tar xzf - \  
&& cd /usr/local/src/texinfo-4.13 \  
&& ./configure && make install \  
&& cd /usr/local/src && rm -fr texinfo* \  
&& for f in $(cd /usr/lib/x86_64-linux-gnu; ls *crt*.o); do ln -s
x86_64-linux-gnu/${f} /usr/lib/${f}; done \  
&& { find /usr/local/bin /usr/local/sbin -type f -executable -exec strip
--strip-all '{}' \+ || true; } \  
&& rm -fr /var/cache/oracle-jdk8-installer \  
&& DEBIAN_FRONTEND=noninteractive && apt-get autoremove -y \  
&& sed -i "s/PermitRootLogin without-password/PermitRootLogin yes/"
/etc/ssh/sshd_config \  
&& mkdir -p /var/run/sshd \  
&& locale-gen en_US.UTF-8 && { locale-gen -no-purge -lang en_US.UTF-8 || true
;}  
  
CMD ["/usr/sbin/sshd", "-D"]  

