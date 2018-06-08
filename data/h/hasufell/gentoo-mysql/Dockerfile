FROM hasufell/gentoo-amd64-paludis:latest  
  
MAINTAINER Julian Ospald <hasufell@gentoo.org>  
  
# global flags  
RUN echo -e "*/* acl bash-completion ipv6 kmod openrc pcre readline unicode \  
zlib pam ssl sasl bzip2 urandom crypt tcpd \  
-acpi -cairo -consolekit -cups -dbus -dri -gnome -gnutls -gtk -ogg -opengl \  
-pdf -policykit -qt3support -qt5 -qt4 -sdl -sound -systemd -truetype -vim \  
-vim-syntax -wayland -X" \  
>> /etc/paludis/use.conf  
  
# update world with our USE flags  
RUN chgrp paludisbuild /dev/tty && cave resolve -c world -x  
  
# per-package flags  
# check these with "cave show <package-name>"  
RUN mkdir /etc/paludis/use.conf.d && \  
echo -e "dev-db/mysql client-libs community perl server ssl tools" \  
>> /etc/paludis/use.conf.d/mysql.conf  
  
# install mysql  
RUN chgrp paludisbuild /dev/tty && cave resolve -z dev-db/mysql -x --favour
dev-db/mysql  
  
# install pwgen, needed by runtime scripts  
RUN chgrp paludisbuild /dev/tty && cave resolve -z app-admin/pwgen -x  
  
# install tools  
RUN chgrp paludisbuild /dev/tty && cave resolve -z app-admin/supervisor sys-
process/htop -x  
  
# update etc files... hope this doesn't screw up  
RUN etc-update --automode -5  
  
# Add MySQL configuration  
RUN echo -e "\n\n!includedir /etc/mysql/conf.d/" >> /etc/mysql/my.cnf  
COPY my.cnf /etc/mysql/conf.d/my.cnf  
COPY mysqld_charset.cnf /etc/mysql/conf.d/mysqld_charset.cnf  
  
# Add MySQL scripts  
RUN cp /usr/share/mysql/scripts/mysql_install_db /usr/bin/mysql_install_db  
COPY import_sql.sh /import_sql.sh  
COPY run.sh /run.sh  
RUN chmod +x /run.sh /import_sql.sh /usr/bin/mysql_install_db  
  
ENV MYSQL_USER=admin \  
MYSQL_PASS=**Random** \  
ON_CREATE_DB=**False** \  
REPLICATION_MASTER=**False** \  
REPLICATION_SLAVE=**False** \  
REPLICATION_USER=replica \  
REPLICATION_PASS=replica \  
MYSQL_PORT=3306  
EXPOSE 3306  
CMD /run.sh  

