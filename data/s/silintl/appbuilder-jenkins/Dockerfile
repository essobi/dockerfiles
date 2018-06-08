FROM jenkins:1.651.2  
MAINTAINER <Chris Hubbard> "chris_hubbard@sil.org"  
USER root  
RUN apt-get update && apt-get install -y \  
s3cmd vim  
  
RUN curl
https://raw.githubusercontent.com/silinternational/s3-expand/master/s3-expand
> /usr/local/bin/s3-expand  
RUN chmod a+x /usr/local/bin/s3-expand  
  
#To Debug the execution of the init.groovy.d scripts:  
# 1) uncomment the following lines  
# 2) switch the entrypoints  
# 3) run docker-compose build  
# 4) run docker-compose up  
# 5) run docker exec -it vagrant_appbuilder_1 bash  
# 6) in container, run /usr/local/bin/jenkins.sh  
#COPY build/debug.sh /usr/local/bin/  
#RUN chmod a+x /usr/local/bin/debug.sh  
COPY build/init.groovy.d/ /usr/share/jenkins/ref/init.groovy.d/  
  
COPY build/plugins.txt /usr/share/jenkins/ref/  
RUN /usr/local/bin/plugins.sh /usr/share/jenkins/ref/plugins.txt  
  
ENTRYPOINT
["/usr/local/bin/s3-expand","/bin/tini","--","/usr/local/bin/jenkins.sh"]  
#ENTRYPOINT
["/usr/local/bin/s3-expand","/bin/tini","--","/usr/local/bin/debug.sh"]  

