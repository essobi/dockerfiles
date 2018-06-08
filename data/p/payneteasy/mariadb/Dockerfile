FROM mariadb:10.0.30  
  
RUN echo 'deb http://deb.debian.org/debian sid main' >> /etc/apt/sources.list
\  
&& apt-get update \  
&& apt-get -qq -t sid install -y curl \  
&& sed -i 's/^.bind-address/bind-address/' /etc/mysql/my.cnf  
  
COPY redir.sh /docker-entrypoint-initdb.d/redir.sh  
COPY developer.cnf /etc/mysql/conf.d/developer.cnf  

