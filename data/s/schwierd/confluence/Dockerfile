FROM schwierd/atlassian-base:latest  
MAINTAINER Daniel Schwierzeck <daniel.schwierzeck@gmail.com>  
  
ENV CONFLUENCE_VERSION 5.9.5  
ENV CONFLUENCE_ROOT /opt/confluence  
  
# Create system user  
RUN groupadd -r confluence -g 666 && \  
useradd -r -g confluence -u 666 -m -d $CONFLUENCE_ROOT -s /sbin/nologin
confluence && \  
mkdir -p $CONFLUENCE_ROOT/install $CONFLUENCE_ROOT/data  
  
# Install Confluence  
RUN curl -sSL
http://www.atlassian.com/software/confluence/downloads/binary/atlassian-
confluence-$CONFLUENCE_VERSION.tar.gz \  
| tar -xz --strip=1 -C $CONFLUENCE_ROOT/install/  
  
# Configure Confluence home directory  
RUN echo "confluence.home = $CONFLUENCE_ROOT/data" >
$CONFLUENCE_ROOT/install/confluence/WEB-INF/classes/confluence-init.properties  
  
# Increase MaxMetaspaceSize  
RUN sed -i \  
-e 's,-XX:MaxMetaspaceSize=256m,-XX:MaxMetaspaceSize=512m,g' \  
$CONFLUENCE_ROOT/install/bin/setenv.sh  
  
# Fix permissions  
RUN chown -R confluence:confluence $CONFLUENCE_ROOT  
  
EXPOSE 8090  
VOLUME $CONFLUENCE_ROOT/data  
  
COPY docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
WORKDIR $CONFLUENCE_ROOT/install/bin  
USER confluence  
CMD [ "run" ]  

