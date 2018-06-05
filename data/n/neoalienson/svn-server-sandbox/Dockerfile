FROM alpine:latest  
MAINTAINER neo [at] orz [dot] hk  
  
WORKDIR /var/opt/svn  
  
RUN apk update && \  
apk add subversion  
  
# create a sandbox repository with full access from anyone, with default
strcture  
RUN svnadmin create sandbox && \  
echo -e "[general]\nanon-access = write" > sandbox/conf/svnserve.conf && \  
svn mkdir file:///var/opt/svn/sandbox/tags
file:///var/opt/svn/sandbox/branches \  
file:///var/opt/svn/sandbox/trunk -m 'inital structure'  
  
VOLUME /var/opt/svn  
  
EXPOSE 3690  
CMD [ "/usr/bin/svnserve", "--daemon", "--foreground", "--root",
"/var/opt/svn" ]  

