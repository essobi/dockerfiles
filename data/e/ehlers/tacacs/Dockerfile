FROM debian:stretch-slim  
  
COPY tac_passwd /usr/local/sbin/  
  
RUN set -ex \  
#  
# install tacacs+ server  
#  
&& export DEBIAN_FRONTEND=noninteractive \  
&& apt-get update \  
&& apt-get -y --no-install-recommends install \  
dumb-init tacacs+ \  
net-tools iproute2 ifupdown isc-dhcp-client inetutils-ping \  
telnet traceroute procps nano vim-tiny \  
&& rm -rf /var/lib/apt/lists/* \  
#  
# tac_plus.conf template for do_auth  
#  
&& /bin/echo -e '\  
\x23 My simple tacplus config that never needs to change\n\  
\x23 See https://github.com/jathanism/do_auth\n\  
key = mykey\n\  
\n\  
accounting file = /var/log/tacplus.acct\n\  
\n\  
default authentication = file /etc/tacacs+/passwd\n\  
\n\  
user = DEFAULT {\n\  
member = doauthaccess\n\  
}\n\  
\n\  
group = doauthaccess {\n\  
default service = permit\n\  
\n\  
service = exec {\n\  
priv-lvl = 15\n\  
idletime = 10\n\  
}\n\  
\n\  
enable = file /etc/tacacs+/passwd\n\  
after authorization "do_auth -i $address -u '\''$user'\'' -d $name -l
/var/log/do_auth.log -f /etc/tacacs+/do_auth.ini"\n\  
}' \  
> /etc/tacacs+/tac_plus.conf.do_auth \  
#  
# tacacs utilities  
#  
&& chmod 755 /usr/local/sbin/tac_passwd \  
&& ln -s tac_passwd /usr/local/sbin/tac_adduser \  
&& ln -s tac_passwd /usr/local/sbin/tac_deluser \  
&& /bin/echo -e '\  
\x23!/bin/sh\n\  
\n\  
tac_plus -C /etc/tacacs+/tac_plus.conf -P' \  
> /usr/local/sbin/tac_parse && chmod +x /usr/local/sbin/tac_parse \  
&& /bin/echo -e '\  
\x23!/bin/sh\n\  
\n\  
service tacacs_plus reload' \  
> /usr/local/sbin/tac_reload && chmod +x /usr/local/sbin/tac_reload \  
&& /bin/echo -e '\  
\x23!/bin/sh\n\  
\n\  
service tacacs_plus start' \  
> /usr/local/sbin/tac_start && chmod +x /usr/local/sbin/tac_start \  
&& /bin/echo -e '\  
\x23!/bin/sh\n\  
\n\  
service tacacs_plus stop' \  
> /usr/local/sbin/tac_stop && chmod +x /usr/local/sbin/tac_stop \  
&& chown -h root:root /usr/local/sbin/* \  
#  
# startup script  
#  
&& /bin/echo -e '\  
\x23!/bin/sh\n\  
[ $$ -eq 1 ] && exec dumb-init -- "$0" "$@"\n\  
\n\  
service tacacs_plus start\n\  
\n\  
cd /etc/tacacs+\n\  
exec bash -i' \  
> /etc/init.sh && chmod +x /etc/init.sh  
  
VOLUME [ "/etc/tacacs+" ]  
CMD [ "/etc/init.sh" ]  

