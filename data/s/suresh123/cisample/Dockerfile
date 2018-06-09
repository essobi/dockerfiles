#  
# Version 0.1.0  
  
#FROM ubuntu:14.04  
  
#FROM centos:latest  
FROM limengyu1990/redhat-base  
#CMD echo "This is a docker container"  
RUN mkdir /home/TTU  
ADD Dockerfile /home/TTU/Dockerfile  
ADD testfile.sh /home/TTU/testfile.sh  
RUN chmod 777 /home/TTU/testfile.sh  
RUN touch /home/TTU/logfile.log  
RUN cat /home/TTU/testfile.sh >> /home/TTU/logfile.log  
RUN cat /home/TTU/Dockerfile >> /home/TTU/logfile.log  
RUN sh /home/TTU/testfile.sh >> /home/TTU/logfile.log  
  
#ADD ./*.rpm /home/TTU/clients/  
#RUN yum install -y createrepo  
#RUN createrepo /home/TTU/clients  
#ADD ./ttu.repo /etc/yum.repos.d  
#RUN yum install -y bteq  
  
  
#ADD cliv2-15.10.00.00-1.noarch.rpm /home/TTU/clients/  
  
#RUN cp cliv2-15.10.00.00-1.noarch.rpm /home/cliv2dir/  
#RUN sudo apt-get install rpm  
#RUN rpm -ivh cliv2-15.10.00.00-1.noarch.rpm  
# supervisor  
#RUN apt-get install supervisor -y  
#RUN update-rc.d -f supervisor disable  
  
#ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# start script  
#ADD startup /usr/local/bin/startup  
#RUN chmod +x /usr/local/bin/startup  
  
#CMD ["/usr/local/bin/startup"]  
  
# environment  
  
# sources  
  
# ppas  
  
# mysql-server  
#RUN apt-get install mysql-server -y  
#RUN update-rc.d -f mysql disable  
  
#VOLUME ["/var/lib/mysql", "/var/log/mysql", "/etc/mysql/conf.d"]  
  
#EXPOSE 3306  

