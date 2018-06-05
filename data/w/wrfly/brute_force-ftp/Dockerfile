FROM wrfly/alpine-cn:latest  
MAINTAINER wrfly <mr.wrfly@gmail.com>  
RUN apk --update add vsftpd  
COPY e.sh top100.txt /  
COPY vsftpd.conf /etc/vsftpd.conf  
RUN chmod +x /e.sh  
CMD ["/e.sh"]

