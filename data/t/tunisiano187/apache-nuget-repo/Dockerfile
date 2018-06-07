FROM ubuntu  
  
# Pre configuration of postfix  
RUN echo "postfix postfix/mailname string di.bowlman.org" | debconf-set-
selections  
RUN echo "postfix postfix/main_mailer_type string 'Internet Site'" | debconf-
set-selections  
  
# Install required packages  
RUN apt-get -y update && apt-get install -y apache2 curl git incron nano
postfix  
  
# Start services on docker run  
RUN echo "/etc/init.d/apache2 restart" >> /etc/bash.bashrc  
RUN echo "/etc/init.d/incrond restart" >> /etc/bash.bashrc  
  
# add administrator mail  
RUN echo "root : user@mail.com" >> /etc/aliases  
RUN newaliases  
  
# Create the repository  
RUN mkdir -p /data/repos && chown -R $(whoami):$(whoami) /data  
  
# Cloning repository  
RUN git clone https://github.com/tunisiano187/apache-nuget-repo.git
/data/repos/nuget  
  
# Create repository packages folder  
RUN mkdir /data/repos/nuget/nupkg  
  
RUN chmod u+x /data/repos/nuget/generate-manifest.sh  
  
# Force apache2 to accept this folder  
RUN echo "<Directory /sshfs-pointer-int/>" >> /etc/apache2/apache2.conf  
RUN echo " Options Indexes FollowSymLinks" >> /etc/apache2/apache2.conf  
RUN echo " AllowOverride None" >> /etc/apache2/apache2.conf  
RUN echo " Require all granted" >> /etc/apache2/apache2.conf  
RUN echo "</Directory>" >> /etc/apache2/apache2.conf  
  
# Configuring apache2  
RUN cp /data/repos/nuget/misc/data.conf /etc/apache2/conf-available/  
RUN a2enconf data  
RUN ln -s /data/repos /var/www/html/  
  
# Restart apache to take care of changes  
RUN service apache2 restart  
  
# Creating incron user table for the repository  
RUN cp /data/repos/nuget/misc/incron-nuget-repo.conf
/var/spool/incron/$(whoami)  
RUN cp /data/repos/nuget/misc/incron-nuget-repo.conf
/var/spool/incron/$(whoami)  
RUN chmod 600 /var/spool/incron/$(whoami)  
RUN service incron restart  
  
RUN chmod u+x /data/repos/nuget/misc/download-some-packages.sh  
RUN cd /data/repos/nuget && ./misc/download-some-packages.sh  
  

