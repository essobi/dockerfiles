FROM centos:6.7  
  
##########################################################################  
### update glibc-common for locale files  
RUN yum update -y glibc-common  
  
##########################################################################  
# all yum installations here  
RUN yum install -y sudo passwd openssh-server openssh-clients tar screen
crontabs strace telnet perl libpcap bc patch ntp dnsmasq unzip pax which git
nano || true  
  
##########################################################################  
# add epel repository  
RUN rpm -Uvh http://download.fedoraproject.org/pub/epel/6/x86_64/epel-
release-6-8.noarch.rpm  
  
RUN (yum install -y hiera lsyncd sshpass rng-tools || true)  
  
# start sshd to generate host keys, patch sshd_config and enable yum repos  
RUN (service sshd start; \  
sed -i 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config; \  
sed -i 's/#UsePAM no/UsePAM no/g' /etc/ssh/sshd_config; \  
sed -i 's/#PermitRootLogin yes/PermitRootLogin yes/' /etc/ssh/sshd_config; \  
sed -i 's/enabled=0/enabled=1/' /etc/yum.repos.d/CentOS-Base.repo)  
  
RUN (mkdir -p /root/.ssh/; \  
rm -f /var/lib/rpm/.rpm.lock; \  
echo "StrictHostKeyChecking=no" > /root/.ssh/config; \  
echo "UserKnownHostsFile=/dev/null" >> /root/.ssh/config)  
  
# terminfo for screen.xterm-256color  
ADD screen.xterm-256color /root/  
RUN tic /root/screen.xterm-256color  
##########################################################################  
#self action  
RUN (mkdir /elsesky; \  
cd /elsesky)  
  
##########################################################################  
# Set default environment variables  
ENV PORT_PASS "password"  
ENV METHOD "aes-256-cfb"  
ENV PROTOCOL "auth_aes128_md5"  
ENV PROTOCOL_PARAM ""  
ENV OBFS "tls1.2_ticket_auth_compatible"  
ENV OBFS_PARAM ""  
ENV ROOT_PASS "password"  
  
##########################################################################  
# Set default port pass variables  
ENV p1="password" \  
p2="password" \  
p3="password" \  
p4="password" \  
p5="password" \  
p6="password" \  
p7="password" \  
p8="password" \  
p9="password" \  
p10="password" \  
p11="password" \  
p12="password" \  
p13="password" \  
p14="password" \  
p15="password" \  
p16="password" \  
p17="password" \  
p18="password" \  
p19="password"  
  
  
##########################################################################  
#git clone  
RUN git clone -b manyuser https://github.com/shadowsocksr/shadowsocksr.git
/elsesky/shadowsocksr  
RUN chmod +x /elsesky/shadowsocksr/*.sh  
RUN chmod +x /elsesky/shadowsocksr/shadowsocks/*.sh  
RUN cp -n /elsesky/shadowsocksr/apiconfig.py
/elsesky/shadowsocksr/userapiconfig.py  
RUN cp -n /elsesky/shadowsocksr/config.json /elsesky/shadowsocksr/user-
config.json  
RUN cp -n /elsesky/shadowsocksr/mysql.json
/elsesky/shadowsocksr/usermysql.json  
  
##########################################################################  
# running shell  
COPY entrypoint.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/entrypoint.sh  
EXPOSE 22  
  
##########################################################################  
# Configure container to run as an executable  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]  

