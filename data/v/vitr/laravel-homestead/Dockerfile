FROM ubuntu:16.04  
MAINTAINER vitr <vitdotonline@gmail.com>  
  
ENV DEBIAN_FRONTEND=noninteractive \  
TERM=xterm  
  
# Copy custom scripts  
COPY provision.sh /provision.sh  
COPY start.sh /start.sh  
RUN chmod +x /*.sh  
  
# create new user - vagrant password - vagrant  
RUN useradd vagrant -m -s /bin/bash && \  
echo vagrant:vagrant | /usr/sbin/chpasswd  
  
# Force Locale  
RUN apt-get clean && apt-get update && apt-get install -y locales  
RUN echo "LC_ALL=en_US.UTF-8" >> /etc/default/locale && \  
locale-gen en_US.UTF-8  
  
RUN ./provision.sh  
  
#ADD default-app.tar.gz /home/vagrant  
#RUN chown -Rf vagrant.vagrant /home/vagrant/default-app  
COPY homestead.app /etc/nginx/sites-available/  
RUN ln -sf /etc/nginx/sites-available/homestead.app /etc/nginx/sites-
enabled/homestead.app  
#COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
RUN mkdir /home/vagrant/apps  
  
# Volumes  
VOLUME ["/etc/nginx"]  
VOLUME ["/home/vagrant/apps"]  
VOLUME ["/var/cache/nginx"]  
VOLUME ["/var/log/nginx"]  
VOLUME ["/var/lib/mysql"]  
VOLUME ["/var/log/supervisor"]  
  
EXPOSE 80 22 35729 9876  
ENTRYPOINT ["/bin/bash","-c"]  
#CMD ["/usr/bin/supervisord"]  
#CMD ["tail -f /dev/null"]  
#CMD bash -C '/path/to/start.sh';'bash'  
CMD ["/start.sh"]  
  
# Set the default command to run when starting the container  
#CMD ["/usr/lib/postgresql/9.3/bin/postgres", "-D",
"/var/lib/postgresql/9.3/main", "-c",
"config_file=/etc/postgresql/9.3/main/postgresql.conf"]  

