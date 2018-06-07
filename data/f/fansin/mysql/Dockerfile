FROM mysql  
  
ENV MYSQL_ROOT_PASSWORD root  
  
RUN set -ex \  
echo -e "GRANT ALL PRIVILEGES ON *.* TO 'root'@'%'IDENTIFIED BY 'root' WITH
GRANT OPTION;\nFLUSH PRIVILEGES" > /docker-entrypoint-
initdb.d/open_remote_privilege.sql &&\  
echo "create database if not exists test DEFAULT CHARSET utf8 COLLATE
utf8_general_ci; \  
use test;\  
create table if not exists Person(id bigint(19) not null auto_increment,name
varchar(20) not null ,id_card varchar(18) not null ,\  
bank_card varchar(19) not null ,mobile_phone varchar(14) not null ,age
tinyint(3) ,home varchar(256), office varchar(256),\  
create_datetime timestamp default current_timestamp, remark varchar(200),\  
primary key (id)\  
) comment '个人信息四要素' engine = InnoDB;CREATE UNIQUE INDEX
Person_id_card_name_bank_card_mobile_phone_uindex ON Person (id_card, name,
bank_card, mobile_phone);" > /docker-entrypoint-initdb.d/init_test.sql &&\  
echo
"bulk_insert_buffer_size=120M\nmax_allowed_packet=512M\nnet_buffer_length=16K"
>>/etc/mysql/mysql.conf.d/mysqld.cnf  
  
EXPOSE 3306/tcp  
CMD ["mysqld"]  

