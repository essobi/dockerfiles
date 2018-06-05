FROM postgres:9.2  
RUN apt-get update && apt-get install -y curl  
  
COPY pt_BR /usr/share/i18n/locales/pt_BR  
  
RUN localedef -i de_DE -c -f ISO-8859-1 -A /usr/share/i18n/locales/pt_BR
pt_BR.ISO-8859-1  
ENV LANG pt_BR.ISO-8859-1  
RUN export LC_ALL=pt_BR  
RUN echo LC_ALL=pt_BR >> /etc/environment  
  
COPY postgresql.conf /setup/postgresql.conf  
  
COPY entrypoint/config-db.sh /docker-entrypoint-initdb.d/  
COPY entrypoint/config-roles.sql /docker-entrypoint-initdb.d/  
COPY entrypoint/vacuum.sql /docker-entrypoint-initdb.d/  
  
RUN curl -SL https://github.com/edsondewes/docker-postgres-
ecidade/releases/download/2.3.46/e-cidade-2.3.46.tar.gz | tar -xz -C /docker-
entrypoint-initdb.d/  

