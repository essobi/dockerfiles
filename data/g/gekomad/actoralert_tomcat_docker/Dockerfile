# ls tomcat/webapps/; docker build . -t actoralert_tomcat_docker  
  
FROM tomcat  
  
#cp check actor-alert.war  
ADD ["tomcat", "/usr/local/tomcat/"]  
  
#RUN apt-get update && apt-get install -y vim  
# create a network  
# docker network create actoralert-network  
# docker run --net=actoralert-network --name actoralert_tomcat_docker -it
actoralert_tomcat_docker  
# publish  
# docker login  
# docker commit actoralert_tomcat_docker actoralert_tomcat_docker:v0.3  
# docker tag actoralert_tomcat_docker:v0.3
gekomad/actoralert_tomcat_docker:v0.3  
# docker push gekomad/actoralert_tomcat_docker:v0.3  
# load:  
# docker run -d --net=actoralert-network --name actoralert_tomcat_docker
gekomad/actoralert_tomcat_docker:v0.3  

