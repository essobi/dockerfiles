# File: Dockerfile  
#  
# Author: Massimo Cannavo <massimo5cannavo@gmail.com>  
# Date: Sat May 12 21:36:25 PDT 2018  
#  
# Dockerfile that builds the Drupal CMS container from the Udemy  
# Docker Mastery courses.  
#  
# https://github.com/BretFisher/udemy-docker-mastery  
#  
# Usage: docker network create drupal-net  
#  
# docker volume create postgres-data  
# docker volume create drupal-data  
#  
# docker container run --detach --network drupal-net \  
# --env POSTGRES_DB=drupal \  
# --env POSTGRES_PASSWORD=postgres \  
# --volume postgres-data:/var/lib/postgresql/data \  
# --health-cmd "pg_isready -U postgres || exit 1" \  
# --name postgres-db postgres  
#  
# docker container run --detach --network drupal-net \  
# --volume drupal-data:/var/www/html \  
# --publish 8080:80 \  
# --name drupal-cms massimocannavo/drupal-cms  
  
FROM drupal  
  
RUN apt-get update && apt-get install -y git \  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR /var/www/html/themes  
  
RUN git clone --depth 1 --branch 8.x-3.x \  
https://git.drupal.org/project/bootstrap.git  
  
HEALTHCHECK CMD curl --fail http://localhost || exit 1  
  
EXPOSE 80  
WORKDIR /var/www/html  

