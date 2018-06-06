FROM tomcat:9  
# There are different ENV vars to consider when running Fedora Commons.  
# An explanation of running Tomcat from
https://stackoverflow.com/a/29398713/1154882  
# "  
# In many circumstances, it is desirable to have a single copy of a Tomcat
binary distribution shared among multiple users on the same server. To make
this possible, you can set the CATALINA_BASE environment variable to the
directory that contains the files for your 'personal' Tomcat instance.  
# When running with a separate CATALINA_HOME and CATALINA_BASE, the files and
directories are split as following:  
# In CATALINA_BASE:  
# bin - Only: setenv.sh (*nix) or setenv.bat (Windows), tomcat-juli.jar  
# conf - Server configuration files (including server.xml)  
# lib - Libraries and classes, as explained below  
# logs - Log and output files  
# webapps - Automatically loaded web applications  
# work - Temporary working directories for web applications  
# temp - Directory used by the JVM for temporary files>  
# In CATALINA_HOME:  
# bin - Startup and shutdown scripts  
# lib - Libraries and classes, as explained below  
# endorsed - Libraries that override standard "Endorsed Standards". By default
it's absent.  
# "  
# For Willow purposes:  
# CATALINA_HOME is set by the Tomcat Docker image. There should be no need to
change it.  
# CATALINA_BASE is the directory where settings specific to the Fedora Commons
app need to be held.  
# As per the description above, certain directories in CATALINA_BASE are
static assets (bin, conf, lib)  
# while certain directories change during runtime (logs, webapps, work, temp).  
# The static directories should be baked into the image. The writeable
directories should be mounted as volumes.  
# In this case this would result in 3 extra volumes, none of which are
particularly useful.  
# For Willow, it is easier to make the entire CATALINA_BASE a volume. That
means that when the volume is mounted at container  
# start-up, everything done inside CATALINA_BASE in this Dockerfile is going
to disappear (unless it's being run on a  
# local developer workstation). All actions that need to be taken inside
CATALINA_BASE should be taken in the docker-entrypoint.sh,  
# not here.  
# What we do here is to add all static assets to a static directory,
WILLOW_FEDORA_STATIC_DIR. Those will be symlinked  
# into CATALINA_BASE by docker-entrypoint.sh on each container start-up.  
# The final result after the container starts is something like this:  
# ls -l $CATALINA_BASE  
# bin -> $WILLOW_FEDORA_STATIC_DIR/bin  
# conf -> $WILLOW_FEDORA_STATIC_DIR/conf  
# lib -> $WILLOW_FEDORA_STATIC_DIR/lib  
# logs  
# webapps  
# ROOT.war -> $WILLOW_FEDORA_STATIC_DIR/webapps/ROOT.war  
# work  
# temp  
ENV WILLOW_FEDORA_STATIC_DIR=/willow_fedora_static \  
FCREPO4_HOME=/fcrepo4_home \  
FCREPO4_DATA=/fcrepo4_data \  
CATALINA_BASE=/fcrepo4_home  
  
RUN mkdir -p $WILLOW_FEDORA_STATIC_DIR $WILLOW_FEDORA_STATIC_DIR/bin
$WILLOW_FEDORA_STATIC_DIR/webapps /tmp  
  
# Tip: downloading large files with "curl -L <URL> -o <file>" (rather than
with DOCKER ADD) allows for the files to be fully cached  
RUN curl -L
https://github.com/fcrepo4/fcrepo4/releases/download/fcrepo-4.7.2/fcrepo-
webapp-4.7.2.war -o $WILLOW_FEDORA_STATIC_DIR/webapps/ROOT.war  
  
COPY conf $WILLOW_FEDORA_STATIC_DIR/conf  
COPY setenv.sh $WILLOW_FEDORA_STATIC_DIR/bin/setenv.sh  
COPY docker-healthcheck.sh /usr/local/bin/  
COPY wait-for-it.sh /usr/local/bin/  
COPY docker-entrypoint.sh /  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
HEALTHCHECK CMD ["docker-healthcheck.sh"]  

