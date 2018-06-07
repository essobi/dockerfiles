FROM ubuntu:trusty  
  
  
# Install packages  
ENV DEBIAN_FRONTEND noninteractive  
ENV PROJECT_NAME myproject  
  
# Set locale (fix the locale warnings)  
RUN locale-gen --purge en_US.UTF-8  
RUN echo 'LANG="en_US.UTF-8"' > /etc/default/locale  
RUN echo 'LANGUAGE="en_US:en"' >> /etc/default/locale  
  
  
# Set timezone  
RUN echo "Asia/Jerusalem" > /etc/timezone  
RUN dpkg-reconfigure --frontend noninteractive tzdata  
  
RUN rm /etc/apt/sources.list  
ADD stuff/sources.local.list /etc/apt/sources.list  
  
  
RUN apt-get update -y  
RUN apt-get install -y software-properties-common python-software-properties
openssh-server supervisor \  
apache2 libapache2-mod-wsgi python-pip python-dev\  
postgresql postgresql-contrib libpq-dev postgresql-server-dev-9.3  
  
  
  
  
RUN mkdir /src  
  
############################## SSH
############################################################  
RUN mkdir /root/.ssh  
RUN mkdir /var/run/sshd  
  
ADD sshkey.pub /root/.ssh/authorized_keys  
RUN chown root:root /root/.ssh/authorized_keys  
RUN sed -i "s/UsePrivilegeSeparation.*/UsePrivilegeSeparation no/g"
/etc/ssh/sshd_config && sed -i "s/UsePAM.*/UsePAM no/g" /etc/ssh/sshd_config  
  
  
  
############################## APACHE2
############################################################  
  
  
#uncomment if your vps is slow  
#RUN rm /etc/apache2/mods-available/mpm_event.conf  
#ADD stuff/mpm_event.conf /etc/apache2/mods-available/mpm_event.conf  
  
ADD stuff/vhost /etc/apache2/sites-available/vhost.conf  
RUN a2enmod headers \  
&& a2dissite 000-default.conf \  
&& a2ensite vhost.conf \  
&& service apache2 stop  
  
  
  
############################## POSTGRES
##############################################  
  
ADD stuff/requirements.txt /src/requirements.txt  
RUN pip install -r /src/requirements.txt  
  
  
  
RUN sed -i "s/^auto.*/manual/g" /etc/postgresql/9.3/main/start.conf \  
&& echo "host all all 0.0.0.0/0 md5" >> /etc/postgresql/9.3/main/pg_hba.conf \  
&& echo "listen_addresses='*'" >> /etc/postgresql/9.3/main/postgresql.conf  
  
ADD stuff/first_run /src/first_run  
ADD stuff/run_postgresql.sh /src/run_postgresql.sh  
ADD stuff/create_db.sh /var/lib/postgresql/create_db.sh  
  
RUN chmod +x /src/first_run && \  
chmod +x /src/run_postgresql.sh && \  
chmod +x /var/lib/postgresql/create_db.sh  
  
  
  
  
  
################################# DJANGO
#############################################  
  
RUN ln -s /usr/local/bin/django-admin.py /usr/bin/django-admin  
ADD stuff/settings.py /src/settings.py  
ADD stuff/wsgi.py /src/wsgi.py  
ADD stuff/create_admin.py /src/create_admin.py  
  
############################## SUPERVISOR
##############################################  
  
  
  
RUN mkdir -p /var/log/supervisor  
ADD stuff/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
  
  
EXPOSE 22  
CMD env | grep _ >> /etc/environment && /usr/bin/supervisord  

