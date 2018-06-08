FROM jetty  
RUN cd /var/lib/jetty/webapps && wget
https://dl.bintray.com/manorrock/maven/com/manorrock/git/repos/15/repos-15.war  
ENV GIT_REPOS_DIRECTORY /mnt  
EXPOSE 8080  

