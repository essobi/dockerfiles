FROM ubuntu:16.04  
RUN apt-get update && apt-get install -yq sudo net-tools wget imagemagick
subversion git gcc g++ binutils autoconf automake autopoint libtool-bin make
bzip2 libncurses5-dev libreadline-dev zlib1g-dev flex bison patch texinfo
tofrodos gettext pkg-config ecj fastjar realpath perl libstring-crc32-perl
ruby ruby1.8 gawk python libusb-dev unzip intltool libacl1-dev libcap-dev
libc6-dev-i386 lib32ncurses5-dev gcc-multilib lib32stdc++6 libglib2.0-dev
iputils-ping  
RUN echo "auto eth0" >> /etc/network/interfaces && echo "iface eth0 inet dhcp"
>> /etc/network/interfaces && echo "dns-nameservers 8.8.8.8"  
RUN adduser --disabled-password --gecos "" freetz  

