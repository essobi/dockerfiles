# Dockerfile for running docker-compose in CircleCI 2.0  
FROM debian:jessie  
RUN apt-get update && apt-get install -y curl ssh git  
RUN curl -L --fail
"https://github.com/docker/compose/releases/download/1.12.0/docker-
compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose  
RUN chmod +x /usr/local/bin/docker-compose  

