# 1.베이스 이미지 지정  
FROM centos:latest  
  
# 2.작성자 정보  
MAINTAINER 0.1 ck1214.lee@gmail.com  
  
# 3.Apache HTTP Server 설치  
RUN yum -y install httpd  
  
# 4.Web 컨텐츠  
ADD html/ /var/www/html/  
  
# 5.포트 번호  
EXPOSE 80  
# 6.httpd 실행  
CMD ["/usr/sbin/httpd","-D", "FOREGROUND"]  

