# sudo useradd -g mail -u 150 vmail -d /home/vmail  
# sudo mkdir /home/vmail  
# sudo chown vmail:mail /home/vmail  
#  
# docker build -t yuanying/email-server .  
# docker run -d --link mysql:mysql -e "POSTFIX_MYSQL_PASSWORD=postfixpassword"
-e "POSTFIXADMIN_SETUP_PASSWORD=POSTFIXADMIN_SETUP_PASSWORD" -h
'mail.fraction.jp' -v /home/vmail:/var/vmail -p 25:25 -p 993:993 -p 8080:8080
yuanying/email-server  
#  
FROM phusion/baseimage:0.9.15  
MAINTAINER O. Yuanying "yuan-docker@fraction.jp"  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" >>
/etc/apt/sources.list  
RUN apt-get update  
RUN apt-get -y install software-properties-common  
RUN add-apt-repository -y ppa:ondrej/php5  
RUN add-apt-repository -y ppa:ansible/ansible  
RUN apt-get update  
  
#RUN apt-get install -y --no-install-recommends \  
# python-apt python-jinja2 python-paramiko python-pip python-yaml \  
# && apt-get clean \  
# && pip install ansible  
RUN apt-get -y install ansible  
  
# RUN dpkg-divert --local --rename --add /sbin/initctl  
# RUN ln -s /bin/true /sbin/initctl  
# RUN freshclam  
ADD ansible /.ansible  
WORKDIR /.ansible  
RUN chmod +x /.ansible/setup.sh && /.ansible/setup.sh  
  
ADD run /usr/local/bin/run  
RUN chmod +x /usr/local/bin/run  
  
EXPOSE 25 143 465 993 8080  
VOLUME ["/var/vmail"]  
  
CMD ["/usr/local/bin/run"]  
  

