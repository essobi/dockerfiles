FROM kalabox/drush:v0.6.0  
ADD drushrc.php /root/.drush/drushrc.php  
RUN ln -s /usr/local/src/drush6/drush /usr/bin/drush  
RUN apt-get update && apt-get install openssh-server mysql-client php5-mysql
-y  
RUN drush dl registry_rebuild  
  
RUN mkdir /var/run/sshd  
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
  
# SSH login fix. Otherwise user is kicked off after login  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
  
EXPOSE 22  
CMD echo $AUTHORIZED_KEYS > /root/.ssh/authorized_keys && /usr/sbin/sshd -D  

