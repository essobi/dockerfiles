# Usage:  
# docker run --rm --volumes-from=dockerredmine_redmine_1 starfox/redmine-
plugin-dashboard  
#  
FROM sameersbn/ubuntu  
MAINTAINER Sascha.Herrmann.Consulting@gmail.com  
  
RUN apt-get update  
RUN apt-get -y install wget git  
  
ADD install-plugin.sh /install-plugin.sh  
CMD ["/install-plugin.sh"]  

