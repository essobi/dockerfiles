# vuurmuur container for teaching students some basic firewall settings:  
# this container needs extendet host privileges to add kernel-modules  
# run with extendet privileges eg:  
# docker run -it --cap-add=NET_ADMIN --cap-add=SYS_MODULE  
# -v /lib/modules:/lib/modules --name=vuurmuur fugitivus/vuurmuur bash  
  
FROM fugitivus/debian:latest  
MAINTAINER fugitivus <fugitivus@gmx.net>  
  
#environment-variables for non-interactive shell:  
#ENV DEBIAN_FRONTEND noninteractive  
#ENV DEBCONF_NOWARNINGS yes  
  
#install some packages to build vuurmuur:  
RUN apt-get update && apt-get -y --no-install-recommends install \  
wget libtool debhelper automake autoconf gcc g++ libc6-dev iptables\  
libncurses5-dev conntrack libnfnetlink-dev libnetfilter-log-dev kmod\  
ca-certificates unzip\  
  
#download,build and install vuurmuur:  
&& wget https://github.com/inliniac/vuurmuur/archive/master.zip\  
&& unzip master.zip\  
&& cd vuurmuur-master\  
&& ./autogen.sh\  
&& ./configure\  
&& dpkg-buildpackage -d\  
&& dpkg -i /vuurmuur_0.8~rc5-1_amd64.deb\  
&& rm -r /vuurmuur*\  
&& ln -s /etc/vuurmuur/ /usr/local/etc/vuurmuur\  
&& chmod -R 600 /etc/vuurmuur\  
&& echo "VUURMUUR_START=1" > /etc/default/vuurmuur\  
&& sed -i -e 46c'MODULES_TO_LOAD="ip_tables iptable_filter\  
iptable_mangle iptable_nat ip_conntrack ipt_state\  
ip_conntrack_ftp ip_nat_ftp"' /etc/init.d/vuurmuur\  
  
#do some cleanup:  
&& apt-get remove --purge wget libtool debhelper automake autoconf\  
gcc g++ libc6-dev libncurses5-dev ca-certificates unzip -y\  
&& apt-get clean autoclean\  
&& apt-get autoremove -y\  
&& rm -rf /var/lib/{apt,dpkg,cache,log}/  
  
#automatic startup for vuurmuur service:  
#ENTRYPOINT ["/etc/init.d/vuurmuur", "start"]  

