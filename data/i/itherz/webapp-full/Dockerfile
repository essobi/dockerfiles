FROM itherz/webapp-full:d7  
  
RUN apt install -y sudo curl unzip && \  
echo "dev ALL=(root) NOPASSWD: /bin/chmod, /usr/bin/setfacl" >
/etc/sudoers.d/devsudo && \  
sed -i "s/StrictModes.*/StrictModes no/ig" /etc/ssh/sshd_config  
  
ADD 01-root.conf /etc/nginx/conf.d/  
ADD 05-php.conf /etc/nginx/conf.d/  
  
EXPOSE 80 22  
VOLUME /var/www/html  

