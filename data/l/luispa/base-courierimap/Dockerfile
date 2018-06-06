#  
# "courier-imap" base by Luispa, Dec 2014  
#  
# Servidor de correo IMAP con courier-imap  
#  
# \-----------------------------------------------------  
  
#  
# Desde donde parto...  
#  
FROM debian:jessie  
  
# Autor de este Dockerfile  
#  
MAINTAINER Luis Palacios <luis@luispa.com>  
  
# Pido que el frontend de Debian no sea interactivo  
ENV DEBIAN_FRONTEND noninteractive  
  
# Actualizo el sistema operativo e instalo lo mínimo  
#  
RUN apt-get update && \  
apt-get -y install locales \  
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
  
# HOME  
ENV HOME /root  
  
# \------- ------- ------- ------- ------- ------- -------  
# DEBUG ( Descomentar durante debug del contenedor )  
# \------- ------- ------- ------- ------- ------- -------  
#  
# Herramientas SSH, tcpdump y net-tools  
#RUN apt-get update && \  
# apt-get -y install openssh-server \  
# tcpdump \  
# net-tools  
# Setup de SSHD  
#RUN mkdir /var/run/sshd  
#RUN echo 'root:rootdocker' | chpasswd  
#RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
#RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
#ENV NOTVISIBLE "in users profile"  
#RUN echo "export VISIBLE=now" >> /etc/profile  
# Script que uso a menudo durante debug  
RUN echo "grep -vh '^[[:space:]]*#' \"\$@\" | grep -v '^//' | grep -v '^;' |
grep -v '^\$' | grep -v '^\\!' | grep -v '^--'" > /usr/bin/confcat  
RUN chmod 755 /usr/bin/confcat  
  
# \------- ------- ------- ------- ------- ------- -------  
# Instalo courier-imap  
# \------- ------- ------- ------- ------- ------- -------  
#  
# La instalación de courier-imap necesita authlib-mysql para poder  
# comprobar los usuario en una base de datos MySQL, también necesita  
# el paquete gamin (permite notificar cambios en el filesystem, es  
# un reemplazo más moderno al paquete FAM).  
#  
RUN mkdir -p /var/run/courier/authdaemon  
RUN > /var/run/courier/authdaemon/pid.lock  
RUN chown -R daemon:daemon /var/run/courier  
# Instalación de courier-imap  
RUN apt-get update && \  
apt-get -y install courier-imap \  
courier-imap-ssl \  
courier-authlib-mysql \  
gamin  
RUN rm -fr /var/run/courier  
  
# SSL  
WORKDIR /etc/courier  
  
##################################################################  
#  
# FICHEROS DE CONFIGURACIÓN DE Courier-Imap  
#  
# Utilizo ficheros externos desde el directorio de datos persistentes  
# En caso de no existir crearé una primera configuración válida.  
#  
# Utilizo la técnica de enlaces simbólicos (parecida a la de timezone)  
# debido a que el montaje de ficheros no funcionaba con docker 1.6.1.  
#  
# Afecta a cuatro ficheros de configuración.  
#  
# /etc/courier/imapd  
# /etc/courier/authdaemonrc  
# /etc/courier/imapd-ssl  
# /etc/courier/authmysqlrc  
# /etc/courier/imapd.cnf  
#  
#  
# 1) En el DOCKERFILE  
RUN mkdir -p /config/courierimap  
RUN rm -f /etc/courier/imapd && touch /config/courierimap/imapd && ln -s
/config/courierimap/imapd /etc/courier/  
RUN rm -f /etc/courier/authdaemonrc && touch /config/courierimap/authdaemonrc
&& ln -s /config/courierimap/authdaemonrc /etc/courier/  
RUN rm -f /etc/courier/imapd-ssl && touch /config/courierimap/imapd-ssl && ln
-s /config/courierimap/imapd-ssl /etc/courier/  
RUN rm -f /etc/courier/authmysqlrc && touch /config/courierimap/authmysqlrc &&
ln -s /config/courierimap/authmysqlrc /etc/courier/  
RUN rm -f /etc/courier/imapd.cnf && touch /config/courierimap/imapd.cnf && ln
-s /config/courierimap/imapd.cnf /etc/courier/  
#  
# 2) En el Script entrypoint:  
# if [ -d '/config/courierimap' ]; then  
# #  
# # Comprobar si existe cada uno de los cuatro ficheros y crearlos en caso
contrario...  
# #  
# fi  
#  
# 3) Al arrancar el contenedor, montar el volumen, a contiuación un ejemplo:  
# /Apps/data/correo/courierimap:/config/courierimap  
#  
# 4) Modificar la configuración:  
# 4.1.- Arrancar el contenedor una vez para que se creen los ficheros  
# 4.2.- Parar el contenedor  
# 4.3.- Modificar los ficheros y volver a arrancar el contenedor  
#  
  
# Generar los certificados  
#ADD imapd.cnf /etc/courier/imapd.cnf  
#RUN rm imapd.pem  
#RUN mkimapdcert  
  
# Puertos por el que escucha el servidor  
#  
EXPOSE 143  
  
#\-----------------------------------------------------------------------------------  
  
# Ejecutar siempre al arrancar el contenedor este script  
#  
ADD do.sh /do.sh  
RUN chmod +x /do.sh  
ENTRYPOINT ["/do.sh"]  
  
#  
# Si no se especifica nada se ejecutará lo siguiente:  
#  
CMD ["/usr/bin/supervisord", "-n -c /etc/supervisor/supervisord.conf"]  

