#  
# Roundcube container by Luispa, Nov 2014  
#  
# -----------------------------------------------------  
#  
# Desde donde parto...  
#  
FROM luispa/base-apache  
  
# Autor  
#  
MAINTAINER Luis Palacios <luis@luispa.com>  
  
# Pido que el frontend de Debian no sea interactivo  
ENV DEBIAN_FRONTEND noninteractive  
  
# Instalo mis herramientas básicas y además un cliente de MySQL de modo que el  
# script do.sh pueda crear la base de datos 'roundcube' si es que no existe  
#  
RUN apt-get update && \  
apt-get -y install mysql-client \  
net-tools \  
vim \  
supervisor \  
wget \  
curl \  
rsyslog  
  
# Directorio de trabajo  
#  
WORKDIR /root  
  
# Pongo un fichero de virtual host personalizado para apache  
#  
ADD ./000-default.conf /etc/apache2/sites-available/000-default.conf  
  
# Descargo roundcubemail  
# Copia el 404.php  
#  
RUN wget
http://freefr.dl.sourceforge.net/project/roundcubemail/roundcubemail/1.0.3/roundcubemail-1.0.3.tar.gz
-O - | tar xz ;  
RUN rm -f /var/www/html/index.html  
ADD 404.php /  
  
# ------- ------- ------- ------- ------- ------- -------  
# DEBUG ( Descomentar durante debug del contenedor )  
# ------- ------- ------- ------- ------- ------- -------  
#  
# Herramientas SSH, tcpdump y net-tools  
#RUN apt-get update && \  
# apt-get -y install openssh-server \  
# tcpdump \  
# net-tools  
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
  
#-----------------------------------------------------------------------------------  
# Ejecutar siempre al arrancar el contenedor este script  
#  
ADD do.sh /do.sh  
RUN chmod +x /do.sh  
ENTRYPOINT ["/do.sh"]  
  
#  
# Si no se especifica nada se ejecutará lo siguiente:  
#  
CMD ["/usr/bin/supervisord", "-n -c /etc/supervisor/supervisord.conf"]  

