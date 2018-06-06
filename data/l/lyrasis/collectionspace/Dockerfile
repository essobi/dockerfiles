FROM postgres:9.4  
  
RUN localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias
en_US.UTF-8  
  
ENV DB_CSADMIN_PASSWORD 123456  
ENV LANG en_US.utf8  
  
ADD setup.sh /docker-entrypoint-initdb.d/setup.sh

