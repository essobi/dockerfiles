FROM debian:stable-slim  
LABEL Description="Cron" Vendor="brumbrum" Version="1.0"  
MAINTAINER Alessandro Lattao <alessandro.lattao@brumbrum.it>  
  
# Configura la timezone  
ENV TZ=Europe/Rome  
  
# Installo le dipendenze  
RUN apt-get update && \  
apt-get install --no-install-recommends -y && \  
apt-get install --no-install-recommends -o Dpkg::Options::="--force-confnew"
-y cron locales bash rsyslog awscli mysql-client curl && \  
locale-gen && \  
apt-get autoremove && \  
apt-get clean  
  
# Aggiungo i file di configurazione  
COPY /data /data  
COPY /bin/entrypoint.sh /entrypoint.sh  
COPY /var/log/cronjob.log /var/log/cronjob.log  
COPY /bin/setup.sh /setup.sh  
COPY /bin/database_backup.sh /database_backup.sh  
COPY /bin/database_restore.sh /database_restore.sh  
COPY /bin/annunci_backup.sh /annunci_backup.sh  
COPY /bin/pricing_backup.sh /pricing_backup.sh  
COPY /bin/export_auto.sh /export_auto.sh  
  
# Sistemo bashrc per essere eseguito anche da cron  
# http://stackoverflow.com/questions/11245144/replace-whole-line-containing-a-
string-using-sed  
RUN sed -i '/[ -z "$PS1" ] && return/c\\#' /etc/bash.bashrc  
  
RUN chmod +x /*.sh  
RUN chmod +x /data/*.sh  
  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime  
RUN echo $TZ > /etc/timezone  
  
# Avvio l'entrypoint  
ENTRYPOINT ["/entrypoint.sh"]  

