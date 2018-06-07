FROM openjdk:8-jdk  
  
LABEL maintainer="hilmar.lapp@duke.edu"  
# For which target within the repository to build? If empty, uses the latest  
# release. Otherwise, the branch, or tag, for which to build the container.  
ARG TARGET  
  
# name and Github repository  
ARG APPNAME=phenoscape-kb-services  
ARG REPO=phenoscape/phenoscape-kb-services  
  
# create designated non-root system user and group  
ARG APP_USER=phenoscape  
ARG APP_GROUP=phenoscape  
  
# where to install within the container  
ARG APP_PREFIX=/usr/share/phenoscape  
  
# Prevent error messages from debconf about non-interactive frontend  
ARG TERM=linux  
ARG DEBIAN_FRONTEND=noninteractive  
  
ADD create-user.sh /usr/local/bin/create-service-user  
RUN chmod ug+x /usr/local/bin/create-service-user  
RUN create-service-user $APP_USER $APP_GROUP  
  
# Install dependencies of sbt  
RUN apt-get update -y && \  
apt-get install -y apt-utils && \  
apt-get install -y \  
apt-transport-https \  
fakeroot  
  
# Install sbt (Scala Build Tool) through its Debian package directory.  
RUN echo "deb https://dl.bintray.com/sbt/debian /" > \  
/etc/apt/sources.list.d/sbt.list && \  
apt-key adv \--keyserver hkp://keyserver.ubuntu.com:80 \  
\--recv 2EE0EA64E40A89B84B2DF73499E82A75642AC823  
  
RUN apt-get update -y && \  
apt-get install -y \  
sbt  
  
# Download and unpack application from the requested tag or branch on Github  
ADD get-tarball-url.sh /tmp/get-tarball-url.sh  
RUN echo \  
"Building $APPNAME from "$(sh /tmp/get-tarball-url.sh $REPO $TARGET) && \  
curl -L -o /tmp/$APPNAME.tar.gz \  
$(sh /tmp/get-tarball-url.sh $REPO $TARGET) && \  
mkdir /tmp/$APPNAME && \  
tar -z -x -v \--strip-components 1 -C /tmp/$APPNAME -f /tmp/$APPNAME.tar.gz  
  
# Build application (using sbt)  
RUN cd /tmp/$APPNAME && \  
sbt stage  
  
# then install to /usr/share, adding a symlink to /usr/local/bin, and  
# end by cleaning up  
RUN cd /tmp/$APPNAME && \  
mv target/universal/stage $APP_PREFIX && \  
chmod a+x $APP_PREFIX/bin/$APPNAME && \  
ln -s $APP_PREFIX/bin/$APPNAME /usr/local/bin/$APPNAME && \  
rm -rf /tmp/$APPNAME* /tmp/get-tarball-url*  
# create the mount point for configuration files  
RUN mkdir /srv/conf  
  
# application may need a significant amount of memory  
# (use --env on the docker run command line to override)  
ENV JAVA_OPTS="-Xmx8G"  
# the port on which application will be listening within the container  
EXPOSE 8082  
  
# run the service under a designated user rather than root  
USER $APP_USER  
  
# by default, the application config file is expected at this location  
# (override on the docker run commandline by providing a trailing argument)  
CMD ["-Dconfig.file=/srv/conf/application.conf"]  
  
# this will have to run on the exposed port and bind to 0.0.0.0 to work, so we  
# override here on the command line whatever the configuration file has  
ENTRYPOINT ["/usr/share/phenoscape/bin/phenoscape-kb-services", "-Dkb-
services.port=8082", "-Dkb-services.host=0.0.0.0"]

