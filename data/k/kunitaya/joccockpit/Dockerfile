FROM java:8  
MAINTAINER kunitaya  
  
# install mysql-client  
RUN apt-get update  
RUN apt-get -y install mysql-client  
RUN apt-get clean all  
  
# download JOC Cockpit  
ADD https://download.sos-berlin.com/JobScheduler.1.11/joc_linux.1.11.4.tar.gz
/usr/local/src/  
#RUN curl https://download.sos-
berlin.com/JobScheduler.1.11/joc_linux.1.11.4.tar.gz -o
/usr/local/src/joc_linux.1.11.4.tar.gz  
RUN test -e /usr/local/src/joc_linux.1.11.4.tar.gz && tar zxvf
/usr/local/src/joc_linux.1.11.4.tar.gz -C /usr/local/src/  
RUN rm -f /usr/local/src/joc_linux.1.11.4.tar.gz  
RUN ln -s /usr/local/src/joc.1.11.4 /usr/local/src/joc  
COPY joc_install.xml /usr/local/src/joc/install.xml  
  
COPY init.sh /usr/local/bin/init_joc.sh  
RUN chmod +x /usr/local/bin/init_joc.sh  
  
EXPOSE 4446 40446  
CMD ["/usr/local/bin/init_joc.sh"]  

