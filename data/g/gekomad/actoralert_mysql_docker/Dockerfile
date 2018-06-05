# docker build . -t actoralert_mysql_docker  
  
FROM mysql:latest  
  
RUN cp -r /var/lib/mysql /var/lib/mysql-no-volume  
  
CMD ["--datadir", "/var/lib/mysql-no-volume"]  
  
# docker login  
  
# docker run --name actoralert_mysql_docker -e
MYSQL_ROOT_PASSWORD=790c426b8191910bd774cfb0ac -it actoralert_mysql_docker  
  
# docker exec -i actoralert_mysql_docker mysql -uroot
-p790c426b8191910bd774cfb0ac <create_mysql_schema.sql  
# docker exec -i actoralert_mysql_docker mysql -uroot
-p790c426b8191910bd774cfb0ac actoralert <dump_full.sql  
  
# check  
# docker exec -it actoralert_mysql_docker mysql -uroot actoralert
-p790c426b8191910bd774cfb0ac  
# show tables;exit;  
  
# publish  
# docker commit actoralert_mysql_docker actoralert_mysql_docker:v0.1  
# docker tag actoralert_mysql_docker:v0.1 gekomad/actoralert_mysql_docker:v0.1  
# docker push gekomad/actoralert_mysql_docker:v0.1  
  
  
# create a network  
# docker network create actoralert-network  
  
# docker run -d --net=actoralert-network --name actoralert_mysql_docker
gekomad/actoralert_mysql_docker:v0.1  

