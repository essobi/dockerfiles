FROM anapsix/alpine-java:8_jdk  
  
ENV CONFLUENCE_VER 5.10.3  
ENV CONFLUENCE_DATA /var/lib/atlassian/application-data/confluence  
  
RUN apk --update add curl \  
&& curl -LO
https://www.atlassian.com/software/confluence/downloads/binary/atlassian-
confluence-${CONFLUENCE_VER}.tar.gz \  
&& tar -xzf atlassian-confluence-${CONFLUENCE_VER}.tar.gz -C /usr/local \  
&& ln -s /usr/local/atlassian-confluence-${CONFLUENCE_VER}
/usr/local/confluence \  
&& rm atlassian-confluence-${CONFLUENCE_VER}.tar.gz \  
&& apk --purge del curl  
  
RUN sed -i 's|# confluence.home=.*|confluence.home='"${CONFLUENCE_DATA}"'|g'
/usr/local/confluence/confluence/WEB-INF/classes/confluence-init.properties  
  
VOLUME /var/lib/atlassian/application-data  
EXPOSE 8090  
CMD '/usr/local/confluence/bin/start-confluence.sh' '-fg'  

