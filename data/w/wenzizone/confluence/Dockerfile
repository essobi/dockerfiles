# Basics  
#  
FROM wenzizone/atlassian-base  
MAINTAINER wenzizone <wenzizone@126.com>  
  
# Install Confluence  
ENV CONFLUENCE_VERSION 6.1.2  
ENV CONTEXT_PATH wiki  
#ENV DATABASE_URL mysql://wikiuser:wIkiUser@mysql:3306/confluencedb  
#ENV DB_TYPE mysql  
ADD launch.bash /launch  
ADD provision.bash /provision  
  
RUN ["/provision"]  
  
# Launching Confluence  
WORKDIR /opt/confluence  
VOLUME ["/opt/atlassian-home"]  
EXPOSE 8090  
USER confluence  
CMD ["/launch"]  

