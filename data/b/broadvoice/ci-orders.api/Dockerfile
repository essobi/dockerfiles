# Base on our custom image which uses MS base + Redis. This one adds MySQL to
the mix  
FROM broadvoice/ci-foundation:debian-1.0.1  
#set default environment variables  
ENV MYUSER=${MYUSER:-"devuser"} \  
MYPASSWORD=${MYPASSWORD:-"Password12!"} \  
MYSQL_USER=mysql \  
MYSQL_DATA_DIR=/var/lib/mysql \  
MYSQL_RUN_DIR=/run/mysqld \  
MYSQL_LOG_DIR=/var/log/mysql  
  
ENV DB_REMOTE_ROOT_PASS=${DB_REMOTE_ROOT_PASS:-"${MYPASSWORD}"} \  
DB_REMOTE_ROOT_NAME=${DB_REMOTE_ROOT_NAME:-"${MYUSER}"} \  
DEBIAN_FRONTEND=noninteractive \  
ASPNETCORE_URLS="http://*:5000"  
# Mount partition of MySQL  
VOLUME ["${MYSQL_DATA_DIR}", "${MYSQL_RUN_DIR}"]  
  
# Open ports for mysql & .net core kestrel  
EXPOSE 3306/tcp 5000/tcp  
  
# install MariaDB then cleanup list  
RUN apt-get clean \  
&& apt-get update -y \  
&& apt-get -f install -y software-properties-common apt-utils zip python-pip \  
&& apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80
0xcbcb082a1bb943db \  
&& add-apt-repository 'deb http://mirror.jmu.edu/pub/mariadb/repo/10.0/ubuntu
trusty main' \  
&& apt-get update -y \  
&& apt-get -f install -y mariadb-server --fix-missing \  
&& pip install boto3==1.3.0 \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /var/lib/mysql/*  
  
# See: https://github.com/sameersbn/docker-mysql  
COPY entrypoint.sh /sbin/entrypoint.sh  
  
# Configure & Run MySQL  
RUN /sbin/entrypoint.sh \  
&& service mysql stop  
  
# set launch point  
ENTRYPOINT ["/sbin/entrypoint.sh"]

