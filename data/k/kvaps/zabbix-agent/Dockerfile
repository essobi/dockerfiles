FROM ubuntu:16.04  
  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections \  
&& apt-get -y update \  
&& apt-get -y install wget apt-transport-https  
  
RUN wget -O zabbix-release.deb
'http://repo.zabbix.com/zabbix/3.4/ubuntu/pool/main/z/zabbix-release/zabbix-
release_3.4-1+xenial_all.deb' \  
&& dpkg -i zabbix-release.deb \  
&& rm -f zabbix-release.deb \  
&& apt-get -y update \  
&& apt-get -y install zabbix-agent \  
&& mkdir -p /var/run/zabbix \  
&& chown zabbix:zabbix /var/run/zabbix  
  
RUN apt -y install sysstat bc \  
&& wget https://raw.githubusercontent.com/lesovsky/zabbix-
extensions/master/files/iostat/iostat.conf -O
/etc/zabbix/zabbix_agentd.d/iostat.conf \  
&& mkdir -p /usr/libexec/zabbix-extensions/scripts/ \  
&& wget https://raw.githubusercontent.com/lesovsky/zabbix-
extensions/master/files/iostat/scripts/iostat-parse.sh -O /usr/libexec/zabbix-
extensions/scripts/iostat-parse.sh \  
&& wget https://raw.githubusercontent.com/lesovsky/zabbix-
extensions/master/files/iostat/scripts/iostat-collect.sh -O
/usr/libexec/zabbix-extensions/scripts/iostat-collect.sh \  
&& chmod +x /usr/libexec/zabbix-extensions/scripts/iostat-parse.sh
/usr/libexec/zabbix-extensions/scripts/iostat-collect.sh  
  
CMD [ "runuser", "-u", "zabbix", "-p", "--", "/usr/sbin/zabbix_agentd", "-f" ]  

