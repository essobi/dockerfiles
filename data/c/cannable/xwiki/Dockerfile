FROM cannable/tomcat:9.0-micro  
ENV NAME XWIKI  
  
  
# Version and signature stuff  
# XWIKI_VERSION: Major & minor version of the platform  
ENV XWIKI_VERSION=9.11.4  
# XWIKI_WAR_KEY: PGP signature of the war file. The file is checked during the  
# build process and at first run of the container (before it's unpacked).  
ENV XWIKI_WAR_KEY=E5AFB784BEB276AB  
  
  
# Container configuration  
# LOCAL_APP_NAME: Directory under webapps where the app will live.  
# The default is 'xwiki'. If you want to use ROOT, you will have to make the  
# appropriate config alterations to xwiki.cfg and xwiki.properties required
for  
# the version of XWiki you're running. Please refer to the Admin Guide.  
ENV LOCAL_APP_NAME=xwiki  
  
# LOCAL_DB_DRIVER: Database you intend to use. NOTE: This only supports hsql
at  
# the moment. Other DBs may be added, which is why this is here. You can still  
# choose to use a proper DB (as is the recommendation for anything you intend  
# to run in a production environment), but you will have to configure  
# hibernate.xml and drop in a JDBC driver yourself.  
ENV LOCAL_DB_DRIVER=hsql  
  
  
# Download stuff  
# XWIKI_WARFILE: This is the file name of the war file.  
ENV XWIKI_WARFILE=xwiki-platform-distribution-war-${XWIKI_VERSION}.war  
  
# XWIKI_DL_SITE: This is the top-level directory hosting the war file.  
ENV XWIKI_DL_SITE=https://maven.xwiki.org/releases/org/xwiki/platform/xwiki-
platform-distribution-war/  
  
# XWIKI_DL_URL: Complete URL to the war file.  
ENV XWIKI_DL_URL=${XWIKI_DL_SITE}/${XWIKI_VERSION}/${XWIKI_WARFILE}  
  
# HSQL-Specific Stuff  
# Grabbing a database driver is done on first run of the container  
ENV HSQL_ZIPNAME=hsqldb-2.4.0.zip  
ENV HSQL_ZIPPATH=hsqldb-2.4.0/hsqldb/lib/hsqldb.jar  
ENV HSQL_JARNAME=hsqldb-2.4.0.jar  
ENV HSQL_SHA1=fbda3fc933dd79898c03bc65e6f3bcfa5c722a2d  
ENV
HSQL_DL_URL=https://iweb.dl.sourceforge.net/project/hsqldb/hsqldb/hsqldb_2_4/hsqldb-2.4.0.zip  
  
  
# More container junk  
WORKDIR /usr/local/tomcat  
COPY ["./data", "/data"]  
COPY ["./overrides", "/data/overrides"]  
RUN ["/bin/sh", "/data/build.sh"]  
EXPOSE 8080/tcp  
VOLUME ["/usr/local/tomcat/webapps"]  
VOLUME ["/usr/local/tomcat/work"]  
ENTRYPOINT ["/usr/bin/dumb-init", "--"]  
CMD ["/bin/sh", "/data/xwiki-init.sh"]  
  

