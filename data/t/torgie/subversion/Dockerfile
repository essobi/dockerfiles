FROM alpine:3.4  
MAINTAINER "torgie <torgie@gmail.com>"  
# Create the subversion folders  
RUN mkdir -p /opt/svn \  
&& touch /var/log/svn.log  
  
# Install our necessary software  
RUN apk update \  
&& apk add subversion  
  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
  
# The port needed by svnserve  
EXPOSE 3690  
WORKDIR /opt/svn  
ENTRYPOINT ["/docker-entrypoint.sh"]  

