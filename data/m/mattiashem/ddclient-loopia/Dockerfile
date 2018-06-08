FROM centos:7  
MAINTAINER Mattias Hemmingsson  
  
  
LABEL name="ddclient for loopia.se"  
LABEL vendor="lifeandshell"  
  
RUN yum install perl perl-Net-IP perl-Net-DNS perl-IO-Socket-INET6 perl-IO-
Socket-SSL perl-File-Temp patch wget bzip2 sendmail -y  
RUN wget --no-http-keep-alive -O ddclient.tar.bz2
"http://downloads.sourceforge.net/project/ddclient/ddclient/ddclient-3.8.3.tar.bz2?r=https%3A%2F%2Fsourceforge.net%2Fprojects%2Fddclient%2F&ts=1467045226&use_mirror=tenet"  
RUN tar xvf ddclient.tar.bz2  
RUN mv ddclient-3.8.3 ddclient  
  
WORKDIR /ddclient  
RUN chmod +x ddclient  
RUN mkdir /etc/ddclient/  
RUN mkdir /var/cache/ddclient  
  
ADD ddclient.conf /etc/ddclient/ddclient.conf  
ADD set.sh /set.sh  
RUN chmod +x /set.sh  
  
CMD /set.sh && /ddclient/ddclient -foreground

