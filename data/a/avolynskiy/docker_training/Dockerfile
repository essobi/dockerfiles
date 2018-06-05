FROM mysql  
COPY createdb.sql /opt/  
CMD service mysql start && mysql -se "create database discovery" && mysql -b
discovery < /opt/createdb.sql && mysql -e "GRANT SELECT ON discovery.* TO
'root'@'%' IDENTIFIED BY 'root'; FLUSH PRIVILEGES" && /bin/sh  

