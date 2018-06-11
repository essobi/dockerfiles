FROM centos:7  
MAINTAINER Elvin Tan <elvin@elvin.net>  
RUN yum -y install epel-release && yum -y update  
RUN yum -y install subversion  
EXPOSE 3690/tcp  
VOLUME ["/svn"]  
ENTRYPOINT ["/usr/bin/svnserve","-d","--foreground","-r","/svn"]  
# docker run -d --name=svn --restart=always -v /home/svn:/svn -p 3690:3690
visago/svn  
#  
# On host machine, "cd /home/svn", "svnadmin create repo-name", then edit
/home/svn/repo-name/conf/* ! Disable anonymous !  
#  

