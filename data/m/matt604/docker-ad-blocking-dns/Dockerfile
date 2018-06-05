#  
# I don't use this, but fill your boots!  
FROM ubuntu:16.04  
MAINTAINER Matt Sawasy, sawasy@gmail.com  
  
# Update repos!  
RUN apt-get -q update  
  
# Patch All the things!  
RUN apt-get -qy upgrade  
  
#Install some useful things...  
RUN apt-get -y install bind9 wget supervisor  
  
#Copy the local version to the container  
ADD ./named.conf.options /etc/bind/named.conf.options  
  
#Pull down the excellent blacklist file of advertisers  
RUN wget -O /file
'http://pgl.yoyo.org/as/serverlist.php?hostformat=bindconfig&showintro=0&startdate%5Bday%5D=&startdate%5Bmonth%5D=&startdate%5Byear%5D='  
  
#Chop it up a bit for our use  
RUN sed -i -e '/<[^>]*>/d' -e '/^\s*$/d' -e 's/{/IN {/g' -e
's/null/\/etc\/bind\/null/g' /file  
  
#Copy it over to the container  
RUN mv /file /etc/bind/blacklist  
  
#Add it to the bottom of the named.conf  
RUN echo "include \"/etc/bind/blacklist\";" >> /etc/bind/named.conf  
  
#Copy a blank zone file.  
ADD null.zone.file /etc/bind/null.zone.file  
  
#Copy the supervisord config  
ADD supervisord.conf /etc/supervisor/conf.d/bind9.conf  
  
#Open up the port  
EXPOSE 53  
#Start things off!  
CMD ["/usr/bin/supervisord","-c","/etc/supervisor/supervisord.conf"]  

