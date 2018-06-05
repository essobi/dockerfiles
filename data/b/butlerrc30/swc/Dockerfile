FROM ubuntu:14.04  
MAINTAINER butlerrc30@gmail.com  
#Get updates and dependencies  
RUN apt-get update && apt-get upgrade -y &&\  
apt-get install software-properties-common -y &&\  
apt-add-repository ppa:brightbox/ruby-ng -y &&\  
apt-get update &&\  
apt-get install git ruby2.3-dev ruby2.3 postgresql-contrib postgresql redis-
server libpq-dev libgmp3-dev make g++ nodejs curl bundler -y &&\  
git clone https://github.com/aortbals/southwest-checkin.git  
  
#Create databse role and db template  
USER postgres  
RUN /etc/init.d/postgresql start &&\  
psql --command "CREATE USER root;" &&\  
psql --command "ALTER USER root CREATEDB;" &&\  
psql --command "GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO root;"
&&\  
psql --command "UPDATE pg_database SET datistemplate = FALSE WHERE datname =
'template1';" &&\  
psql --command "DROP DATABASE template1;" &&\  
psql --command "CREATE DATABASE template1 WITH TEMPLATE = template0 ENCODING =
'UNICODE';" &&\  
psql --command "UPDATE pg_database SET datistemplate = TRUE WHERE datname =
'template1';"  
#Get gems, populate DB and start app  
USER root  
WORKDIR "/southwest-checkin"  
RUN cp .env.example .env && gem install bundler && bundle install && bundle
update  
RUN /etc/init.d/postgresql start && /etc/init.d/redis-server start && rake
db:create db:migrate db:seed  
EXPOSE 3000  
CMD /etc/init.d/postgresql start && /etc/init.d/redis-server start && bundle
exec sidekiq -d -L sidekiq.log && /usr/local/bin/rails server -b 0.0.0.0  
  

