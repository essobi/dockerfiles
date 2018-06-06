# TvHeadEnd pour free dans un container  
#  
# VERSION 0.0.1  
#  
FROM ubuntu:yakkety  
MAINTAINER Fwedoz "fwedoz@gmail.com"  
# Definition des constantes  
ENV login_ssh="docker"  
ENV password_ssh="docker"  
# Mise a jour des depots  
RUN (apt-get update && apt-get upgrade -y -q && apt-get -y -q autoclean &&
apt-get -y -q autoremove)  
  
# Ajout des depots necessaires  
RUN apt-get install -y -q wget nano git zip openssh-server php7.0 php7.0-xml
php7.0-gd php7.0-sqlite php7.0-mbstring php7.0-intl  
  
# Ajout utilisateur "${login_ssh}"  
RUN adduser --quiet --disabled-password --shell /bin/bash --home
/home/${login_ssh} \--gecos "User" ${login_ssh}  
  
# Modification du mot de passe pour "${login_ssh}"  
RUN echo "${login_ssh}:${password_ssh}" | chpasswd  
  
# Installation de Cops  
COPY install_cops.sh /root/install_cops.sh  
RUN chmod -f 755 /root/install_cops.sh  
RUN sh /root/install_cops.sh  
  
# Copie du script d'installation de l application de base  
COPY install_app.sh /root/install_app.sh  
RUN chmod -f 755 /root/install_app.sh  
  
# Installation de la bibliotheque manga  
RUN sh /root/install_app.sh manga  
COPY config_local_manga.php /home/apps/ebook/app/manga/config_local.php  
RUN chmod -f 755 /home/apps/ebook/app/manga/config_local.php  
COPY ebook_manga.conf /etc/apache2/sites-enabled/ebook_manga.conf  
  
# Installation de la bibliotheque bd  
RUN sh /root/install_app.sh bd  
COPY config_local_bd.php /home/apps/ebook/app/bd/config_local.php  
RUN chmod -f 755 /home/apps/ebook/app/bd/config_local.php  
COPY ebook_bd.conf /etc/apache2/sites-enabled/ebook_bd.conf  
  
# Installation de la bibliotheque comics  
RUN sh /root/install_app.sh comics  
COPY config_local_comics.php /home/apps/ebook/app/comics/config_local.php  
RUN chmod -f 755 /home/apps/ebook/app/comics/config_local.php  
COPY ebook_comics.conf /etc/apache2/sites-enabled/ebook_comics.conf  
  
# Installation de la bibliotheque mag  
RUN sh /root/install_app.sh mag  
COPY config_local_mag.php /home/apps/ebook/app/mag/config_local.php  
RUN chmod -f 755 /home/apps/ebook/app/mag/config_local.php  
COPY ebook_mag.conf /etc/apache2/sites-enabled/ebook_mag.conf  
  
# Installation de la bibliotheque book  
RUN sh /root/install_app.sh book  
COPY config_local_book.php /home/apps/ebook/app/book/config_local.php  
RUN chmod -f 755 /home/apps/ebook/app/book/config_local.php  
COPY ebook_book.conf /etc/apache2/sites-enabled/ebook_book.conf  
  
# Ajout du script services.sh au demarrage  
COPY services.sh /root/services.sh  
RUN chmod -f 755 /root/services.sh  
RUN echo "sh /root/services.sh" >> /root/.bashrc  
  
# Ports  
EXPOSE 22 80 9201 9202 9203 9204 9205  
# Point de montage  
VOLUME ["/home"]  

