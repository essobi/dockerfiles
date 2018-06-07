FROM debian:wheezy  
  
RUN mkdir /tftp  
WORKDIR /tftp  
ADD https://raw.githubusercontent.com/jpetazzo/pipework/master/pipework
/usr/bin/  
ADD http://boot.ipxe.org/undionly.kpxe /tftp/undionly.kpxe  
ADD http://boot.ipxe.org/ipxe.iso /tftp/ipxe.iso  
ADD https://www.kernel.org/pub/linux/utils/boot/syslinux/syslinux-6.02.tar.bz2
/root/syslinux-6.02.tar.bz2  
ADD http://jruby.org.s3.amazonaws.com/downloads/1.7.13/jruby-bin-1.7.13.tar.gz
/root/jruby-bin-1.7.13.tar.gz  
  
# FROM phusion/baseimage  
# ENV ARCH amd64  
#ENV DIST wheezy  
#ENV MIRROR http://ftp.nl.debian.org  
RUN apt-get -q update  
RUN apt-get -qy install dnsmasq wget iptables  
RUN apt-get -qy install p7zip-full ruby1.9.1 ruby1.9.1-dev  
RUN apt-get -qy install bzip2 git-core  
RUN apt-get -qy install openjdk-6-jdk  
RUN apt-get -qy install postgresql libpq-dev build-essential  
RUN gem install bundler --no-ri --no-rdoc  
  
RUN mkdir pxelinux.cfg  
RUN chmod +x /usr/bin/pipework  
RUN 7z e -ssc- ./ipxe.iso ipxe.krn  
RUN tar xvfjO /root/syslinux-6.02.tar.bz2
syslinux-6.02/bios/com32/menu/menu.c32 > menu.c32  
RUN tar xvfjO /root/syslinux-6.02.tar.bz2 syslinux-6.02/bios/core/pxelinux.0 >
pxelinux.0  
RUN tar xvfC /root/jruby-bin-1.7.13.tar.gz /opt  
RUN printf "DEFAULT linux\nKERNEL linux\nAPPEND initrd=initrd.gz\n"
>pxelinux.cfg/default  
  
# Mondodb  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv 7F0CEB10  
RUN echo 'deb http://downloads-distro.mongodb.org/repo/debian-sysvinit dist
10gen' > /etc/apt/sources.list.d/mongodb.list  
RUN apt-get update  
RUN apt-get -qy install mongodb-org  
  
#  
RUN git clone https://github.com/csc/Hanlon.git /opt/hanlon  
WORKDIR /opt/hanlon  
RUN PATH=/opt/jruby-1.7.13/bin:$PATH jgem install bundler  
RUN PATH=/opt/jruby-1.7.13/bin:$PATH bundle install  
WORKDIR /opt/hanlon/script  
RUN PATH=/opt/jruby-1.7.13/bin:$PATH ./create_war.sh  
  
WORKDIR /opt/hanlon  
# enable compilation of c stuff, doesn't work with Jruby  
RUN sed -i 's/^#\\(.*\\)/\1/g' Gemfile  
RUN gem install bundler  
RUN bundle install  
RUN bundle exec ./hanlon_init  
  
CMD \  
echo Setting up iptables... &&\  
iptables -t nat -A POSTROUTING -j MASQUERADE &&\  
echo Waiting for pipework to give us the eth1 interface... &&\  
/pipework --wait &&\  
echo Starting DHCP+TFTP server...&&\  
dnsmasq --interface=eth1 \  
\--dhcp-range=192.168.242.2,192.168.242.99,255.255.255.0,1h \  
\--dhcp-boot=pxelinux.0,pxeserver,192.168.242.1 \  
\--pxe-service=x86PC,"Install Linux",pxelinux \  
\--enable-tftp --tftp-root=/tftp/ --no-daemon  
# Let's be honest: I don't know if the --pxe-service option is necessary.  
# The iPXE loader in QEMU boots without it. But I know how some PXE ROMs  
# can be picky, so I decided to leave it, since it shouldn't hurt.  
#RUN sed -i 's/^#\\(.*\\)/\1/g' Gemfile # would enable compilation of c stuff,
doesn't work with Jruby  
##### bson_ext installation seem to be recommended  
# ** Notice: The native BSON extension was not loaded. **  
# For optimal performance, use of the BSON extension is recommended.  
# To enable the extension make sure ENV['BSON_EXT_DISABLED'] is not set  
# and run the following command:  
# gem install bson_ext  
# If you continue to receive this message after installing, make sure that  
# the bson_ext gem is in your load path.  
###### but after 'gem install bson_ext' I get  

