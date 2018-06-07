FROM mariadb:10.1  
MAINTAINER "The Doalitic Team" <devops@doalitic.com>  
  
RUN apt-get update && \  
apt-get install -y wget && \  
rm -rf /var/lib/apt/lists/*  
  
ENV DOCKERIZE_VERSION v0.2.0  
RUN wget
https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-
linux-amd64-$DOCKERIZE_VERSION.tar.gz \  
&& tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz
\  
&& rm -f dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz  
  
RUN mkdir -p /etc/container/templates  
  
ADD ./mariadb.extra.cnf.tpl /etc/container/templates/  
  
ENTRYPOINT ["dockerize"]  
CMD ["-template",
"/etc/container/templates/mariadb.extra.cnf.tpl:/etc/mysql/conf.d/mariadb.extra.cnf",
\  
"docker-entrypoint.sh", "mysqld"]  

