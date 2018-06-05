FROM ubuntu:precise  
MAINTAINER Bryce Reynolds brycereynoldsdesign@gmail.com  
  
RUN apt-get update -q  
  
RUN apt-get install -qy \  
curl \  
vim \  
unzip \  
git \  
openssh-server \  
supervisor \  
mysql-server-5.5  
  
# Add my.cnf  
ADD my.cnf /etc/mysql/conf.d/my.cnf  
RUN chmod 664 /etc/mysql/conf.d/my.cnf  
  
# Base supervisor configuration  
ADD /supervisord.conf /etc/supervisor/supervisord.conf  
ADD /supervisord-env.sh /supervisord-env.sh  
ADD /supervisord-env.conf /etc/supervisor/conf.d/supervisord-env.conf  
  
# Setup SSH  
RUN apt-get install -qy openssh-server && mkdir /var/run/sshd  
ADD /set_root_pw.sh /set_root_pw.sh  
ADD /supervisord-sshd.sh /supervisord-sshd.sh  
ADD /supervisord-sshd.conf /etc/supervisor/conf.d/supervisord-sshd.conf  
  
# You can set a default ssh password by doing this - otherwise pass  
# an env variable (-e) of ROOT_PASS when building a docker container  
ENV ROOT_PASS unset  
  
  
# Base supervisor configuration  
ADD /supervisord-mysqld.sh /supervisord-mysqld.sh  
ADD /supervisord-mysqld.conf /etc/supervisor/conf.d/supervisord-mysqld.conf  
  
# Add conf to add symbolic link to bash file from includes  
# To take advantage of this you should run with volume
"path/to/local/includes:includes/"  
ADD /supervisord-bashrc.conf /etc/supervisor/conf.d/supervisord-bashrc.conf  
  
RUN chown -R mysql:mysql /var/lib/mysql  
VOLUME ["/var/lib/mysql"]  
  
# Add motd  
RUN rm -f /etc/motd  
ADD motd /etc/motd  
  
# We add standard .sh scripts to root. Make those executable.  
RUN chmod 755 /*.sh && chmod +x /*.sh  
  
EXPOSE 3306 22  
# Only use supervisord to add start scripts  
ENTRYPOINT ["supervisord"]  
CMD ["-n"]

