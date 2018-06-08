FROM alpine:latest  
RUN apk add --update-cache mariadb mariadb-client su-exec pwgen bash tzdata  
ADD https://releases.hashicorp.com/consul-template/0.16.0/consul-
template_0.16.0_linux_amd64.zip /tmp/consul-template.zip  
RUN unzip /tmp/consul-template.zip  
RUN mv /consul-template /usr/bin/consul-template \  
&& chmod +x /usr/bin/consul-template  
ADD templates /etc/consul-template/templates  
RUN chown -R mysql:mysql /etc/consul-template/templates  
RUN echo "skip-name-resolve" | awk '{ print } $1 == "[mysqld]" && c == 0 { c =
1; system("cat") }' /etc/mysql/my.cnf > /tmp/my.cnf \  
&& mv /tmp/my.cnf /etc/mysql/my.cnf  
RUN echo "skip-host-cache" | awk '{ print } $1 == "[mysqld]" && c == 0 { c =
1; system("cat") }' /etc/mysql/my.cnf > /tmp/my.cnf \  
&& mv /tmp/my.cnf /etc/mysql/my.cnf  
RUN mkdir -p /var/run/mysqld \  
&& chown -R mysql:mysql /var/run/mysqld \  
&& chmod 777 /var/run/mysqld  
RUN sed -i 's/\/run\/mysqld\/mysqld.sock/\/var\/run\/mysqld\/mysqld\\.sock/'
/etc/mysql/my.cnf  
VOLUME /var/lib/mysql  
COPY docker-entrypoint.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/docker-entrypoint.sh  
RUN ln -s /usr/local/bin/docker-entrypoint.sh /  
RUN mkdir -p /docker-entrypoint-initdb.d && \  
chown -R mysql:mysql /docker-entrypoint-initdb.d  
ENTRYPOINT ["docker-entrypoint.sh"]  
EXPOSE 3306  
CMD ["mysqld"]  

