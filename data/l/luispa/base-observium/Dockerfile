#  
# "Observium" base by Luispa, Jan 2016  
#  
# \-----------------------------------------------------  
  
#  
# Parto desde Debian Jessie (8.x)  
#  
FROM debian:jessie  
  
# Autor de este Dockerfile  
#  
MAINTAINER Luis Palacios <luis@luispa.com>  
  
# Pido que el frontend de Debian no sea interactivo  
ENV DEBIAN_FRONTEND noninteractive  
  
# \------- ------- ------- ------- ------- ------- -------  
# Básico  
# \------- ------- ------- ------- ------- ------- -------  
  
# Actualizo el sistema operativo e instalo lo mínimo que suelo necesitar  
#  
RUN apt-get update && \  
apt-get -y install locales \  
tcpdump \  
net-tools \  
vim \  
supervisor \  
wget \  
curl \  
rsyslog  
  
# Preparo locales y Timezone  
#  
RUN locale-gen es_ES.UTF-8  
RUN locale-gen en_US.UTF-8  
RUN dpkg-reconfigure locales  
RUN echo "Europe/Madrid" > /etc/timezone; dpkg-reconfigure -f noninteractive
tzdata  
  
# Workaround para el Timezone, en vez de montar el fichero en modo read-only:  
# 1) En el DOCKERFILE  
RUN mkdir -p /config/tz && mv /etc/timezone /config/tz/ && ln -s
/config/tz/timezone /etc/  
# 2) En el Script entrypoint:  
# if [ -d '/config/tz' ]; then  
# dpkg-reconfigure -f noninteractive tzdata  
# echo "Hora actual: `date`"  
# fi  
# 3) Al arrancar el contenedor, montar el volumen, a contiuación un ejemplo:  
# /Apps/data/tz:/config/tz  
# 4) Localizar la configuración:  
# echo "Europe/Madrid" > /Apps/data/tz/timezone  
  
  
# \------- ------- ------- ------- ------- ------- ------- -------  
# Instalar dependencias  
#  
# Fuente: Documentación observium.org  
#  
# \------- ------- ------- ------- ------- ------- ------- -------  
  
#  
RUN apt-get update && \  
apt-get -y install locales \  
net-tools \  
vim \  
supervisor \  
wget \  
curl \  
rsyslog  
  
# Necesario para ejecutar Observium  
RUN apt-get -y install libapache2-mod-php5 php5-cli php5-mysql php5-gd
php5-mcrypt \  
php5-json php-pear snmp fping mysql-server mysql-client python-mysqldb \  
rrdtool subversion whois mtr-tiny ipmitool graphviz imagemagick  
  
# Necesario para poder monitorizar VMs del tipo libvirt  
RUN apt-get -y install libvirt-bin  
  
# Soy MySQL, tendré que escuchar no? y además en todas las IPs :)  
RUN sed -Ei 's/^(bind-address|log)/#&/' /etc/mysql/my.cnf  
EXPOSE 3306  
  
# Directorio al que conmuto...  
WORKDIR /opt  
  
# \------- ------- ------- ------- ------- ------- -------  
# DEBUG SSH y ATTACH  
# \------- ------- ------- ------- ------- ------- -------  
#  
# Conectar con este contenedor  
# docker exec -it ID_DEL_CONTENEDOR bash  
#  
# Conectar via SSH. descomentar lo siguiente  
# Para poder Herramientas SSH, tcpdump y net-tools  
#RUN apt-get update && \  
# apt-get -y install openssh-server  
## Setup de SSHD  
#RUN mkdir /var/run/sshd  
#RUN echo 'root:docker' | chpasswd  
#RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
#RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
#ENV NOTVISIBLE "in users profile"  
#RUN echo "export VISIBLE=now" >> /etc/profile  
  
## Script que uso a menudo durante las pruebas. Es como "cat" pero elimina
líneas de comentarios  
RUN echo "grep -vh '^[[:space:]]*#' \"\$@\" | grep -v '^//' | grep -v '^;' |
grep -v '^\$' | grep -v '^\\!' | grep -v '^--'" > /usr/bin/confcat  
RUN chmod 755 /usr/bin/confcat  
  
# Script muy util que espera hasta que mysql esta listo  
ADD mysql_wait_ready.sh /mysql_wait_ready.sh  
  
# Pongo un fichero de virtual host personalizado para apache  
#  
ADD ./000-default.conf /etc/apache2/sites-available/000-default.conf  
  
# Habilito php mcrypt y mod_rewrite  
#  
RUN php5enmod mcrypt  
RUN a2enmod rewrite  
  
# Copio el crontab  
ADD crontab.txt /crontab.txt  
  
  
#\-----------------------------------------------------------------------------------  
  
# Ejecutar siempre al arrancar el script "do.sh" que a su vez ejecutará el
comando de la última línea  
#  
ADD do.sh /do.sh  
RUN chmod +x /do.sh  
ENTRYPOINT ["/do.sh"]  
  
#  
#  
# Si no se especifica nada se ejecutará lo siguiente:  
#  
#CMD ["/usr/bin/supervisord", "-n -c /etc/supervisor/supervisord.conf"]  

