ARG CLONE_ARGS="--branch feedkit-update https://github.com/janLo/feedbin.git"  
FROM janlo/feedbin-base-onbuild:latest  
MAINTAINER Jan Losinski  
  
ADD config/database.yml /opt/app/config/database.yml  
ADD config/environments/production.rb
/opt/app/config/environments/production.rb  
  
EXPOSE 9292  

