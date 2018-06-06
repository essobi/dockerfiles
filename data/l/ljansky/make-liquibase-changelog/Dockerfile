FROM ljansky/alpine-mysql-liquibase:latest  
  
COPY make_changelog.sh /tmp/make_changelog.sh  
COPY liquibase.properties /tmp/liquibase.properties  
COPY changelog.xml /tmp/changelog.xml  
  
RUN chmod 777 /tmp/make_changelog.sh  
  
RUN mkdir /tmp/db && mkdir /tmp/db/changelogs  
  
ENTRYPOINT [ "/tmp/make_changelog.sh" ]

