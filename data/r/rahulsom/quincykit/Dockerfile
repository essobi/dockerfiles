FROM tutum/lamp:latest  
  
MAINTAINER Rahul Somasunderam  
  
RUN rm -rf /app && \  
git clone https://github.com/TheRealKerni/QuincyKit.git /opt/QuincyKit && \  
cp -r /opt/QuincyKit/server /app && \  
rm -rf /app/local  
RUN cat /app/config.php.sample |\  
sed -e "s/your.server.com/localhost/g" |\  
sed -e "s/database_username/root/g" |\  
sed -e "s/'database_password'/NULL/g" |\  
sed -e "s/database_name/quincydb/g" > /app/config.php  
  
ADD createdb.sh /createdb.sh  
RUN mv /run.sh /run.sh.bak  
RUN cat /run.sh.bak | sed -e
"s/create_mysql_admin_user.sh/create_mysql_admin_user.sh \\\&\\\&
\\\/createdb.sh/g" > /run.sh  
RUN chmod u+x /run.sh && chmod u+x /createdb.sh  
RUN apt-get update -y  
RUN apt-get install -y php5-curl  
  
EXPOSE 80 3306  
  
CMD ["/run.sh"]  

