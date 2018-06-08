# Postgresql  
#  
# VERSION 0.0.1  
FROM ubuntu  
MAINTAINER Reza Jatnika "rezajatnika@gmail.com"  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN locale-gen $LANG; echo "LANG=\"${LANG}\"" > /etc/default/locale; dpkg-
reconfigure locales  
  
# prevent apt from starting postgres right after the installation  
RUN echo "#!/bin/sh\nexit 101" > /usr/sbin/policy-rc.d; chmod +x
/usr/sbin/policy-rc.d  
  
RUN dpkg-divert --local \--rename --add /sbin/initctl  
# RUN ln -s /bin/true /sbin/initctl  
RUN apt-get update  
RUN apt-get -y install postgresql-9.3 postgresql-contrib-9.3 vim-tiny  
  
# allow autostart again  
RUN rm /usr/sbin/policy-rc.d  
  
RUN echo 'host all all 0.0.0.0/0 md5' >> /etc/postgresql/9.3/main/pg_hba.conf  
RUN ex -sc "%s/#listen_addresses = 'localhost'/listen_addresses = '*'/g" -c
"x" /etc/postgresql/9.3/main/postgresql.conf  
  
EXPOSE 5432  
#CMD ["/bin/bash"]  
CMD ["su", "postgres", "sh", "-c", "/usr/lib/postgresql/9.3/bin/postgres -D
/var/lib/postgresql/9.3/main -c
config_file=/etc/postgresql/9.3/main/postgresql.conf"]  

