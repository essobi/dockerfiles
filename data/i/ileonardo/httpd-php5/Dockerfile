# x) - docker build -t ileonardo/httpd-php5 .  
# y) - Às Instruções fica nas Dependências e no final do arquivo: [REGRA] # z)  
### Base da Imagem  
FROM ileonardo/httpd  
  
### Autor  
MAINTAINER iLeonardo Carvalho <i.leonardo.c.c@outlook.com>  
  
### Dependências  
ENV PHP5 5.6.31  
  
ADD ["http://br1.php.net/get/php-${PHP5}.tar.gz/from/this/mirror",
"/usr/local/src/"]  
  
### Start  
# Usando a base do Container Original.  
# ----------  
# WORKDIR DOCUMENT_ROOT  
# PORTS 80 443  
# CMD run.sh  
# Pacotes Essenciais  
RUN apt-get update; \  
apt-get --no-install-recommends -qqy install \  
autoconf \  
libtool \  
build-essential \  
libxml2-dev; \  
  
printf "Package: php5\nPin:release *\nPin-Priority: -1\n" >
/etc/apt/preferences.d/php5-noinstall; \  
### Instalando o PHP5  
# Docker só extrair arquivos remotos se for local e não Docker Hub  
cd /usr/local/src/; \  
tar zxvf /usr/local/src/php-${PHP5}.tar.gz; \  
# Compilando o PHP5  
cd /usr/local/src/php-${PHP5}/; \  
./buildconf --force; \  
./configure --with-apxs2=/usr/local/apache2/bin/apxs \  
\--with-mysql; \  
make; \  
make install; \  
  
cp php.ini-production /usr/local/lib/php.ini; \  
### Configurando o PHP5  
#sed -ie 's/#LoadModule php5_module/LoadModule php5_module/g'
${SERVER_ROOT}/conf/​httpd.conf; \  
  
cd ${DOCUMENT_ROOT}; \  
rm index.html; \  
  
echo "<?php phpinfo(); ?>" > index.php; \  
### Limpando os Pacotes desnecessários  
apt remove -qqy --allow-remove-essential \  
autoconf \  
libtool \  
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
/var/tmp/*

