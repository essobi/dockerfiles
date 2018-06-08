FROM ubuntu:14.10  
MAINTAINER Danil Kutkevich <danil@kutkevich.org>, Maksym Bodnarchuk
<bodnarchuk@gmail.com>  
  
ENV REFRESHED_AT 2015-02-19  
RUN localedef --force --inputfile=en_US --charmap=UTF-8 --alias-
file=/usr/share/locale/locale.alias en_US.UTF-8  
ENV LANG en_US.UTF-8  
RUN apt-get -y update  
RUN apt-get -y upgrade  
RUN apt-get install -y curl git openjdk-8-jdk postgresql-9.4  
  
ENV PGDATA /var/lib/postgresql/9.4/main  
ENV PGBIN /usr/lib/postgresql/9.4/bin  
RUN echo 'host all all 0.0.0.0/0 md5' >> "$PGDATA"/pg_hba.conf  
RUN echo 'local all all trust' >> "$PGDATA"/pg_hba.conf  
RUN echo "listen_addresses='*'" >> "$PGDATA"/postgresql.conf  
  
USER postgres  
  
RUN $PGBIN/pg_ctl -w --pgdata $PGDATA start \  
&& psql --command="UPDATE pg_database SET datistemplate = FALSE WHERE datname
= 'template1';" \  
&& psql --command="DROP DATABASE template1;" \  
&& psql --command="CREATE DATABASE template1 WITH TEMPLATE = template0
ENCODING = 'UNICODE';" \  
&& psql --command="UPDATE pg_database SET datistemplate = TRUE WHERE datname =
'template1';" \  
&& psql --command="CREATE ROLE fhirwall WITH SUPERUSER LOGIN PASSWORD
'fhirwall';" \  
&& psql --command="CREATE DATABASE fhirwall WITH OWNER fhirwall ENCODING =
'UTF8';"  
  
USER root  
  
RUN useradd --user-group --create-home --shell /bin/bash fhir && echo
'fhir:fhir' | chpasswd && adduser fhir sudo  
RUN echo 'fhir ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers  
  
USER fhir  
  
ENV HOME /home/fhir  
ENV PATH /home/fhir/bin:$PATH  
  
RUN mkdir -p /home/fhir/bin  
RUN curl
https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein >
/home/fhir/bin/lein  
RUN chmod a+x /home/fhir/bin/lein  
  
WORKDIR /home/fhir  
RUN lein new deps  
ADD ./depsproject.clj /home/fhir/deps/project.clj  
WORKDIR /home/fhir/deps  
RUN lein deps  
  
ADD . /home/fhir/fhirwall  
WORKDIR /home/fhir/fhirwall  
RUN sudo chown fhir:fhir -R ./  
RUN git submodule init  
RUN git submodule update  
RUN lein deps  
RUN lein javac  
  
USER postgres  
  
RUN $PGBIN/pg_ctl -w --pgdata $PGDATA start && psql fhirwall <
/home/fhir/fhirwall/oauth.sql  
  
EXPOSE 6000  
USER fhir  
  
ENV HOME /home/fhir  
ENV PATH /home/fhir/bin:$PATH  
  
ENV FHIRPLACE_URI fhirplace.health-samurai.io:80  
ENV FHIRWALL_ROUTE_OAUTH oauth  
ENV FHIRWALL_ROUTE_FHIR fhir  
  
WORKDIR /home/fhir/fhirwall  
  
CMD sudo --user=postgres $PGBIN/pg_ctl --pgdata $PGDATA -w start \  
&& echo "{:fhirwall-web-port 6000 \  
:fhirwall-subprotocol \"postgresql\" \  
:fhirwall-subname \"//127.0.0.1:5432/fhirwall\" \  
:fhirwall-user \"fhirwall\" \  
:fhirwall-password \"fhirwall\" \  
:fhirwall-proxy-backend \"http://$FHIRPLACE_URI\" \  
:fhirwall-route-oauth \"$FHIRWALL_ROUTE_OAUTH\" \  
:fhirwall-route-fhir \"$FHIRWALL_ROUTE_FHIR\"}" \  
> .lein-env \  
&& lein run  

