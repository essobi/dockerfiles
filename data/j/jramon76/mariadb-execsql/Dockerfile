# vim:set ft=dockerfile:  
FROM mariadb:10.0.17  
MAINTAINER javier.ramon@gmail.com  
  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections \  
&& apt-get update \  
&& apt-get install -qq -y locales \  
&& apt-get autoremove \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
RUN localedef en_US.UTF-8 -i en_US -fUTF-8  
  
ENV SQL_EXEC_DELAY 30  
ENV SQL_MAX_ALLOWED_PACKET 32M  
ENV SQL_INNODB_LOG_FILE_SIZE 50M  
  
ENV SQL_DEFAULT_CHARSET utf8  
ENV SQL_DEFAULT_CHARSET_COLLATION utf8_general_ci  
  
EXPOSE 3306  
COPY entrypoint.sh /  
COPY execute-sql.sh /  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["mysqld"]  
  

