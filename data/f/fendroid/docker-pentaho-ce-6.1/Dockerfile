FROM fendroid/docker-pentaho-base-master  
  
MAINTAINER fendroid@gmail.com  
  
# Install useful command line utilities  
RUN apt-get install -y man vim  
RUN apt-get install -y zip unzip  
  
# Postgres AUFS bug hack  
RUN mkdir /etc/ssl/private-copy; mv /etc/ssl/private/* /etc/ssl/private-copy/;
rm -r /etc/ssl/private; mv /etc/ssl/private-copy /etc/ssl/private; chmod -R
0700 /etc/ssl/private; chown -R postgres /etc/ssl/private  
  
# Download and extract pentaho BA Server binary  
WORKDIR /home/pentaho/  
RUN wget
https://sourceforge.net/projects/pentaho/files/Business%20Intelligence%20Server/6.1/biserver-
ce-6.1.0.1-196.zip  
  
RUN unzip biserver-ce-6.1.0.1-196.zip -d biserver-ce-6.1.0.1-196  
RUN rm biserver-ce-6.1.0.1-196.zip  
  
ADD ojdbc7.jar /home/pentaho/biserver-ce-6.1.0.1-196/biserver-ce/tomcat/lib/  
  
# Add/run script to load default tables  
ADD loaddb.sh /home/pentaho/  
RUN chmod +x /home/pentaho/loaddb.sh  
#RUN /etc/init.d/postgresql start && \  
# printf 'password\n' | /home/pentaho/loaddb.sh  
# Add script to start biserver  
ADD start.sh /home/pentaho/  
RUN chmod +x /home/pentaho/start.sh  
  
# Redirect Tomcat output  
ENV CATALINA_OUT /dev/stdout  
  
# Start Service  
EXPOSE 8080 22 5432  
CMD /home/pentaho/start.sh && /usr/bin/supervisord  
  

