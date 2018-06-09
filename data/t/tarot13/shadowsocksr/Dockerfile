FROM python:2-alpine  
  
LABEL maintainer "Ian Li <OpenSource@ianli.xyz>"  
  
RUN apk add --no-cache bash curl git unzip && \  
cd /root && \  
curl -O https://raw.githubusercontent.com/tests-always-included/mo/master/mo
&& \  
mv mo /usr/local/bin && \  
chmod +x /usr/local/bin/mo && \  
curl -SL "https://github.com/shadowsocksrr/shadowsocksr/archive/manyuser.zip"
-o shadowsocksr.zip && \  
unzip shadowsocksr.zip -d ./ && \  
curl -SL "https://github.com/nakagami/CyMySQL/archive/master.zip" -o
CyMySQL.zip && \  
unzip CyMySQL.zip -d ./ && \  
mv CyMySQL-master/cymysql/ shadowsocksr-manyuser/ && \  
rm -rf CyMySQL-master && \  
rm CyMySQL.zip shadowsocksr.zip && \  
chmod +x shadowsocksr-manyuser/*.sh && \  
chmod +x shadowsocksr-manyuser/shadowsocks/*.sh && \  
curl -L https://github.com/techotaku/docker-
files/raw/master/shadowsocksr/entrypoint.sh -o /entrypoint.sh && \  
mkdir -p /etc/mo/template && \  
curl -L https://github.com/techotaku/docker-
files/raw/master/shadowsocksr/template/userapiconfig.py.template -o
/etc/mo/template/userapiconfig.py.template && \  
curl -L https://github.com/techotaku/docker-
files/raw/master/shadowsocksr/template/user-config.json.template -o
/etc/mo/template/user-config.json.template && \  
curl -L https://github.com/techotaku/docker-
files/raw/master/shadowsocksr/template/usermysql.json.template -o
/etc/mo/template/usermysql.json.template && \  
cd /root/shadowsocksr-manyuser && \  
rm -f userapiconfig.py > /dev/null 2>&1 && \  
rm -f user-config.json > /dev/null 2>&1 && \  
rm -f usermysql.json > /dev/null 2>&1 && \  
rm -f mudb.json > /dev/null 2>&1 && \  
chmod +x /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]

