FROM catmaid/catmaid-standalone  
  
  
ENV DB_USER=catmaid_user  
ENV DB_PASS=catmaid_password  
ENV PGPASSWORD=${DB_PASS}  
ENV DB_NAME=catmaid  
ENV CM_EXAMPLE_PROJECTS=false  
ENV DB_CONF_FILE=/etc/postgresql/10/main/postgresql.conf  
ENV IMPORTED_SKELETON_FILE_MAXIMUM_SIZE=16777216  
VOLUME /backup  
  
#swapping to bash  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh && rm /bin/sh.distrib && ln -s
/bin/bash /bin/sh.distrib  
  
RUN apt-get -y -q update && apt-get -y -q install python-yaml python-psycopg2  
  
RUN echo -e "host: localhost\nport: 5432\ndatabase: catmaid\nusername:
catmaid_user\npassword: catmaid_password" > ~/.catmaid-db  
  
COPY catmaid_insert_project.py
/home/django/applications/catmaid/management/commands/catmaid_insert_project.py  
  
COPY modify_superuser.py /home/scripts/docker/modify_superuser.py  
  
COPY nginx-catmaid.conf /home/scripts/docker/nginx-catmaid.conf  
  
RUN echo "$(find /etc/ -name 'pg_hba.conf')" && sed -i
'1s/^/local\tall\tall\t\ttrust\n/' $(find /etc/ -name 'pg_hba.conf')  
  
RUN mkdir -p /opt/VFB  
  
COPY init.sh /opt/VFB/init.sh  
COPY backup.sh /opt/VFB/backup.sh  
  
RUN chmod -R 777 /opt/VFB  
  
RUN chmod +x /opt/VFB/*.sh  
  
RUN sed -i
"s/IMPORTED_SKELETON_FILE_MAXIMUM_SIZE.*/IMPORTED_SKELETON_FILE_MAXIMUM_SIZE=${IMPORTED_SKELETON_FILE_MAXIMUM_SIZE}/g"
/home/django/projects/mysite/settings_base.py  
  
RUN sed -i "s|#listen_addresses = 'localhost'|listen_addresses = '*'|g"
/etc/postgresql/10/main/postgresql.conf  
  
RUN echo -e "\nhost all all 0.0.0.0/0 md5\n" >>
/etc/postgresql/10/main/pg_hba.conf  
  
EXPOSE 5432  
RUN /home/scripts/docker/catmaid-entry.sh standalone \  
& sleep 10m \  
&& source /usr/share/virtualenvwrapper/virtualenvwrapper.sh \  
&& workon catmaid \  
&& cd /home/django/projects \  
&& ls -l ./mysite/ \  
&& cat /home/scripts/docker/modify_superuser.py | python manage.py shell  
  
ENV INSTANCE_MEMORY=65000  
ENTRYPOINT ["/opt/VFB/init.sh"]  

