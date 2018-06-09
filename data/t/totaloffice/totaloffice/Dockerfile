FROM debian:jessie  
MAINTAINER avinash.s@yukthi.com  
  
RUN apt-get update  
RUN apt-get -y dist-upgrade  
RUN apt-get -y install python-ldap  
RUN apt-get -y install python-apt  
RUN apt-get -y install python-daemon  
RUN apt-get -y install ldap-utils  
RUN apt-get -y install python-smbpasswd  
RUN apt-get -y install python-psycopg2  
RUN apt-get -y install python-cracklib  
RUN apt-get -y install python-flask  
RUN apt-get -y install nodejs  
RUN apt-get -y install npm  
RUN apt-get -y install git  
RUN ln -s /usr/bin/nodejs /usr/local/bin/node  
RUN npm install -g brunch@1.8.5 bower foreman  
RUN apt-get -y install python-requests  
# Cleanup  
RUN apt-get clean  
  
COPY run-totaloffice /  
  
EXPOSE 8080  
  
CMD ["/run-totaloffice"]  

