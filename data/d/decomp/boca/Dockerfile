# VERSION 0.1  
FROM ubuntu:xenial  
  
RUN apt-get -y update  
RUN apt-get -y install tzdata locales software-properties-common python-
software-properties  
RUN apt-get -y upgrade  
RUN echo "America/Sao_Paulo" > /etc/timezone; dpkg-reconfigure -f
noninteractive tzdata  
RUN locale-gen en_US en_US.UTF-8 pt_BR.UTF-8  
RUN locale -a  
ENV LANGUAGE=pt_BR.UTF-8  
ENV LANG=pt_BR.UTF-8  
ENV LC_ALL=pt_BR.UTF-8  
RUN locale-gen pt_BR.UTF-8  
RUN DEBIAN_FRONTEND=noninteractive dpkg-reconfigure locales  
  
RUN add-apt-repository ppa:brunoribas/ppa-maratona  
RUN apt-get -y update  
RUN apt-get -y install maratona-boca  
  
ENV APACHE_CONFDIR /etc/apache2  
ENV APACHE_ENVVARS $APACHE_CONFDIR/envvars  
RUN echo APACHE_ENVVARS  
RUN set -ex \  
\  
# generically convert lines like  
# export APACHE_RUN_USER=www-data  
# into  
# : ${APACHE_RUN_USER:=www-data}  
# export APACHE_RUN_USER  
# so that they can be overridden at runtime ("-e APACHE_RUN_USER=...")  
&& sed -ri 's/^export ([^=]+)=(.*)$/: ${\1:=\2}\nexport \1/' "$APACHE_ENVVARS"
\  
\  
# setup directories and permissions  
&& . "$APACHE_ENVVARS" \  
&& for dir in \  
"$APACHE_LOCK_DIR" \  
"$APACHE_RUN_DIR" \  
"$APACHE_LOG_DIR" \  
/var/www/html \  
; do \  
rm -rvf "$dir" \  
&& mkdir -p "$dir" \  
&& chown -R "$APACHE_RUN_USER:$APACHE_RUN_GROUP" "$dir"; \  
done  
  
# Apache + PHP requires preforking Apache for best results  
RUN a2dismod mpm_event && a2enmod mpm_prefork  
# logs should go to stdout / stderr  
RUN set -ex \  
&& . "$APACHE_ENVVARS" \  
&& ln -sfT /dev/stderr "$APACHE_LOG_DIR/error.log" \  
&& ln -sfT /dev/stdout "$APACHE_LOG_DIR/access.log" \  
&& ln -sfT /dev/stdout "$APACHE_LOG_DIR/other_vhosts_access.log"  
  
# Add startup script to the container.  
COPY apache2-foreground /usr/local/bin/  
COPY init.sh /init.sh  
  
WORKDIR /var/www/boca  
  
EXPOSE 80  
# Execute the containers startup script which will start many
processes/services  
CMD ["/bin/bash", "/init.sh"]  
  

