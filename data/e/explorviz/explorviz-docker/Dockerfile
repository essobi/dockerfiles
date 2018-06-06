FROM tomcat:8.5-alpine  
MAINTAINER ExplorViz Team <explorviz-developers-request@listserv.dfn.de>  
  
# ENV  
ENV DUMMY_MODE=false  
  
# Install Git, use --no-cache instead of  
# 'apk update' and 'rm -rf /var/cache/apk/*'  
Run \  
apk --no-cache add git  
  
WORKDIR webapps  
  
Run \  
git clone https://github.com/ExplorViz/explorviz-docker.git explorviz-frontend
&&\  
mv explorviz-frontend/*.war ./ &&\  
mkdir explorviz-backend &&\  
unzip -qq explorviz-backend.war -d explorviz-backend &&\  
rm explorviz-backend.war &&\  
mv explorviz-frontend/explorviz-frontend/* explorviz-frontend  
  
# startup script  
COPY startup.sh ./  
RUN chmod +x ./startup.sh  
CMD ./startup.sh && catalina.sh run

