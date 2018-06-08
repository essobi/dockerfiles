FROM ubuntu:14.04  
# packages  
RUN apt-get update  
RUN apt-get -y install \  
curl \  
mysql-server \  
openssh-server \  
git \  
python \  
make \  
g++ \  
gfortran \  
openjdk-6-jdk \  
subversion \  
libblas-dev \  
liblapack-dev \  
libatlas-base-dev \  
zlib1g-dev \  
python-dev \  
python-scipy  
  
RUN curl -kL https://bootstrap.pypa.io/get-pip.py | python  
  
# galaxy account  
RUN useradd -m galaxy  
RUN echo "galaxy:galaxy" | chpasswd  
RUN echo "galaxy ALL = NOPASSWD : ALL" >> /etc/sudoers  
  
# DBMS  
RUN printf "[mysql]\ndefault-character-set=utf8\n" >
/etc/mysql/conf.d/mysql_default_character_set_utf8.cnf  
RUN mysql_install_db  
RUN (mysqld_safe &); sleep 3; \  
mysql -uroot -e "create database galaxy default character set utf8;" ;\  
mysql -uroot -e "create user 'galaxy'@'localhost' identified by 'galaxy';" ;\  
mysql -uroot -e "grant all on galaxy.* to 'galaxy'@'localhost';" ;\  
mysql -uroot -e "SET PASSWORD FOR root@localhost=PASSWORD('galaxy');"  
  
# locale  
RUN locale-gen en_US.UTF-8 && update-locale LANG=en_US.UTF-8  
  
# sshd  
RUN mkdir -p /var/run/sshd  
RUN sed -i 's/^PermitRootLogin without-password/PermitRootLogin yes/g'
/etc/ssh/sshd_config  
RUN sed -i 's/.*session.*required.*pam_loginuid.so.*/session optional
pam_loginuid.so/g' /etc/pam.d/sshd  
  
# galaxy  
ENV GALAXY_FILE_PATH /opt/workdir/galaxy_files  
ENV GALAXY_NEW_FILE_PATH /opt/workdir/database/tmp  
ENV GALAXY_JOB_WORKING_DIRECTORY /opt/workdir/database/job_working_directory  
WORKDIR /home/galaxy  
  
RUN git clone https://github.com/pitagora-galaxy/install-0.2.3.git  
RUN git clone https://github.com/galaxyproject/galaxy  
RUN cd galaxy ; git checkout -b master origin/master  
  
RUN sed 's/^#host = 127.0.0.1/host = 0.0.0.0/' galaxy/config/galaxy.ini.sample
\  
> galaxy/config/galaxy.ini  
#RUN sed -i 's/^#port = 8080/port = 80/' galaxy/config/galaxy.ini  
RUN sed -i 's$^#database_connection =
sqlite:///./database/universe.sqlite?isolation_level=IMMEDIATE$database_connection
=
mysql://galaxy:galaxy@localhost:3306/galaxy?unix_socket=/var/run/mysqld/mysqld.sock$'
\  
galaxy/config/galaxy.ini  
RUN sed -i 's/^#database_engine_option_pool_recycle =
-1/database_engine_option_pool_recycle = 7200/' \  
galaxy/config/galaxy.ini  
RUN sed -i "s@^#file_path = database/files@file_path = $GALAXY_FILE_PATH@" \  
galaxy/config/galaxy.ini  
RUN sed -i "s@^#new_file_path = database/tmp@new_file_path =
$GALAXY_NEW_FILE_PATH@" \  
galaxy/config/galaxy.ini  
RUN sed -i "s@^#job_working_directory =
database/job_working_directory@job_working_directory =
$GALAXY_JOB_WORKING_DIRECTORY@" \  
galaxy/config/galaxy.ini  
RUN sed -i 's$^#tool_dependency_dir = None$tool_dependency_dir =
../tool_dependency$' \  
galaxy/config/galaxy.ini  
RUN sed -i 's/^#allow_user_dataset_purge = False/allow_user_dataset_purge =
True/' \  
galaxy/config/galaxy.ini  
  
RUN mkdir -p tool_dependency && chown galaxy.galaxy tool_dependency  
RUN cp galaxy/config/tool_conf.xml.sample galaxy/config/tool_conf.xml  
RUN chown -R galaxy.galaxy /home/galaxy  
  
ADD init.sh /usr/local/bin/init.sh  
ADD initialize_galaxy.sh /home/galaxy/initialize_galaxy.sh  
RUN /home/galaxy/initialize_galaxy.sh  
  
CMD ["/usr/local/bin/init.sh"]  
  

