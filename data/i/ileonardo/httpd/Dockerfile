# x) - docker build -t ileonardo/httpd .  
# y) - Às Instruções fica nas Dependências e no final do arquivo: [REGRA] # z)  
### Base da Imagem  
FROM ileonardo/base-ubuntu  
  
### Autor  
MAINTAINER iLeonardo Carvalho <i.leonardo.c.c@outlook.com>  
  
### Dependências  
ENV HTTPD 2.4.26  
ENV APR 1.6.2  
ENV APRUTIL 1.6.0  
ENV APRICONV 1.2.1  
  
ENV LINK_APACHE http://ftp.unicamp.br/pub/apache/  
  
ENV SERVER_ROOT /usr/local/apache2  
ENV DOCUMENT_ROOT /var/www/html  
  
ADD ["${LINK_APACHE}/httpd/httpd-${HTTPD}.tar.gz", "/usr/local/src/"]  
ADD ["${LINK_APACHE}/apr/apr-${APR}.tar.gz", "/usr/local/src/"]  
ADD ["${LINK_APACHE}/apr/apr-util-${APRUTIL}.tar.gz", "/usr/local/src/"]  
ADD ["${LINK_APACHE}/apr/apr-iconv-${APRICONV}.tar.gz", "/usr/local/src/"]  
  
ADD ["./httpd", "/etc/init.d/httpd"]  
ADD ["./run.sh", "/usr/local/bin/run.sh"]  
  
ADD ["./httpd.conf", "/opt/"]  
ADD ["./envvars", "/opt/"]  
ADD ["./httpd-log", "/opt/httpd"]  
  
### Start  
# Expondo os sites do Document Root do Apache  
WORKDIR ${DOCUMENT_ROOT}  
# Portas necessárias  
EXPOSE 80 443  
  
# Arquivo inicial da execução do Docker  
CMD ["/usr/local/bin/run.sh"]  
  
# Executa os comandos definidos no diretório padrão  
RUN apt-get update  
RUN apt-get --no-install-recommends -qqy install \  
build-essential \  
libtool-bin \  
libssl-dev \  
libexpat1-dev \  
libpcre++-dev; \  
  
printf "Package: apache2\nPin:release *\nPin-Priority: -1\n" >
/etc/apt/preferences.d/apache2-noinstall; \  
  
### Instalando o Apache Web Server  
# Docker só extrair arquivos remotos se for local e não Docker Hub  
cd /usr/local/src/; \  
tar zxvf /usr/local/src/httpd-${HTTPD}.tar.gz; \  
tar zxvf /usr/local/src/apr-${APR}.tar.gz; \  
tar zxvf /usr/local/src/apr-util-${APRUTIL}.tar.gz; \  
tar zxvf /usr/local/src/apr-iconv-${APRICONV}.tar.gz; \  
  
# Colocando às de pendências em seus lugares  
cp -r /usr/local/src/apr-${APR} /usr/local/src/httpd-${HTTPD}/srclib/apr; \  
cp -r /usr/local/src/apr-util-${APRUTIL}
/usr/local/src/httpd-${HTTPD}/srclib/apr-util; \  
cp -r /usr/local/src/apr-iconv-${APRICONV}
/usr/local/src/httpd-${HTTPD}/srclib/apr-iconv; \  
  
# Configurando o usuário do Apache: httpd (não o www-data)  
groupadd httpd; \  
useradd httpd -g httpd -d /dev/null -s /sbin/nologin; \  
  
#Compilando o APR  
cd /usr/local/src/httpd-${HTTPD}/srclib/apr/; \  
./configure --prefix=/usr/local/apr \  
\--enable-threads \  
\--enable-shared \  
\--enable-malloc-debug; \  
make; \  
make install; \  
  
# Compilando o APR-ICONV  
cd /usr/local/src/httpd-${HTTPD}/srclib/apr-iconv/; \  
./configure --prefix=/usr/local/apr-icon \  
\--with-apr=/usr/local/apr/bin/apr-1-config; \  
make; \  
make install; \  
  
# Compilando o APR-UTIL  
cd /usr/local/src/httpd-${HTTPD}/srclib/apr-util/; \  
./configure --prefix=/usr/local/apr-util \  
\--with-apr=/usr/local/apr; \  
make; \  
make install; \  
  
# Compilando o Apache Web Server  
cd /usr/local/src/httpd-${HTTPD}/; \  
./configure --prefix=${SERVER_ROOT} \  
\--with-apr=/usr/local/apr/bin/apr-1-config \  
\--with-apr-util=/usr/local/apr-util/bin/apu-1-config \  
\--with-apr-iconv=/usr/local/apr-iconv/bin/apriconv \  
\--with-crypto \  
\--enable-mpms-shared \  
\--enable-ssl \  
\--enable-so \  
\--enable-rewrite \  
\--enable-usertrack \  
\--enable-headers \  
\--enable-expires \  
\--enable-disk-cache \  
\--enable-mem-cache \  
\--enable-file-cache \  
\--enable-cache \  
\--enable-vhost-alias \  
\--enable-cgi \  
\--enable-deflate \  
\--enable-deflate=shared \  
\--enable-expires=shared \  
\--enable-headers=shared \  
\--enable-rewrite=shared \  
\--enable-static-support; \  
make; \  
make install; \  
  
### Configurando o Apache Web Server  
#RUN logrotate --force /etc/logrotate.d/httpd  
  
mv ${SERVER_ROOT}/htdocs/index.html ${DOCUMENT_ROOT}; \  
rm -Rf ${SERVER_ROOT}/htdocs; \  
  
# Configurando os locais de Execução e de Log padrões no envvars  
mkdir /var/run/httpd/; \  
mkdir /var/log/httpd/; \  
touch /var/log/httpd/access.log /var/log/httpd/error.log; \  
  
# Permissões do Usuário do Sistema para previnir modificações usando o Usuário
do Apache  
chown -R root:root ${SERVER_ROOT}; \  
chown -R httpd:httpd /var/log/httpd; \  
chmod -R go-w ${SERVER_ROOT}; \  
chmod -R go-r ${SERVER_ROOT}/conf; \  
chmod -R go-r /var/log/httpd; \  
  
# Executáveis do Apache para serem enxergados pelo sistema sem a necessidade
do local completo  
cd /usr/sbin; \  
  
ln -sf ${SERVER_ROOT}/bin/apachectl; \  
ln -sf ${SERVER_ROOT}/bin/httpd; \  
ln -sf ${SERVER_ROOT}/bin/htpasswd; \  
ln -sf ${SERVER_ROOT}/bin/htdigest; \  
ln -sf ${SERVER_ROOT}/bin/apr-1-config; \  
ln -sf ${SERVER_ROOT}/bin/apu-1-config; \  
  
# SCRIPT executável e adaptado pelo Autor pelo comando: service httpd
(OPTIONS)  
chmod +x /etc/init.d/httpd; \  
chmod +x /usr/local/bin/run.sh; \  
  
# CONFIG HTTPD (Version 1.0)  
rm -Rf ${SERVER_ROOT}/conf/httpd.conf; \  
mv /opt/httpd.conf ${SERVER_ROOT}/conf/; \  
  
mv /opt/envvars ${SERVER_ROOT}; \  
  
chown httpd:httpd -R ${DOCUMENT_ROOT}; \  
chmod go-rwx ${DOCUMENT_ROOT}; \  
chmod go+x ${DOCUMENT_ROOT}; \  
chgrp httpd -R ${DOCUMENT_ROOT}; \  
chmod go-rwx -R ${DOCUMENT_ROOT}; \  
chmod g+rx -R ${DOCUMENT_ROOT}; \  
chmod g+rwx -R ${DOCUMENT_ROOT}; \  
  
### Limpando os Pacotes desnecessários  
apt remove -qqy --allow-remove-essential \  
build-essential; \  
  
apt-get -qqy autoremove; \  
apt-get autoclean; \  
apt-get clean; \  
  
rm -rf \  
/usr/local/src/* \  
/var/lib/apt/lists/* \  
/var/cache/apt/archives/* \  
/usr/share/doc/* \  
/usr/share/man/* \  
/tmp/* \  
/var/tmp/*;  
  
# z) docker run -d -p 80:80 -p 443:443 ileonardo/httpd  
# z) docker run -dit --name apache-app --publish=80:80 -v
"/home/aluno/public":/var/www/html/ ileonardo/httpd

