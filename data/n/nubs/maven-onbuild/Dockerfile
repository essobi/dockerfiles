FROM nubs/maven-build:latest  
  
MAINTAINER Spencer Rinehart <anubis@overthemonkey.com>  
  
# Add the project code to the correct spot  
ONBUILD ADD . /code  
  
# Install the dependencies  
ONBUILD RUN mvn  

