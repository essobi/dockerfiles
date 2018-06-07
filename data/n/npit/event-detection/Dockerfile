# Pull base image.  
# FROM ubuntu:trusty  
FROM maven:3-jdk-8  
MAINTAINER George Giannakopoulos (ggianna@iit.demokritos.gr)  
  
ARG DAEMON_DIRECTORY="/daemon"  
ARG MOUNT_DIR="/mnt"  
ARG LOG_DIR="/var/log/bde"  
  
ARG CONNECTIONS_CONFIG_FOLDER="$MOUNT_DIR/connections"  
ARG SUPPLIED_NEWS_PROPS_FILE="$MOUNT_DIR/news.properties"  
ARG SUPPLIED_NEWS_URLS_FILE="$MOUNT_DIR/news.urls"  
ARG SUPPLIED_BLOG_PROPS_FILE="$MOUNT_DIR/blog.properties"  
ARG SUPPLIED_BLOG_URLS_FILE="$MOUNT_DIR/blog.urls"  
ARG SUPPLIED_CLUSTER_PROPS_FILE="$MOUNT_DIR/clustering.properties"  
ARG SUPPLIED_LOCATION_PROPS_FILE="$MOUNT_DIR/location.properties"  
ARG SUPPLIED_TWITTER_QUERIES_FILE="$MOUNT_DIR/twitter.queries"  
ARG SUPPLIED_TWITTER_PROPS_FILE="$MOUNT_DIR/twitter.properties"  
ARG SUPPLIED_TWITTER_ACCOUNTS_FILE="$MOUNT_DIR/twitter.accounts"  
ARG SUPPLIED_CRONTAB_FILE="$MOUNT_DIR/bdetab"  
  
ARG REST_SERVICES_DIR="/rest"  
  
LABEL multi.label1="BDE" \  
multi.label2="Event Detection"  
  
########################################  
## Get and build sources  
########################################  
# Install utils and tools  
RUN echo "Installing prerequisites"  
RUN apt-get -qq update  
RUN apt-get -qq install -y git curl cron  
  
# for debugging, TODO Remove  
RUN echo >&2 "*******************" && echo >&2 "Installing nano,netcat for
debugging, remove @ production version."  
RUN apt-get -qq install -y nano netcat  
  
  
# Make and define working directory.  
ENV BDE_ROOT_DIR "/bde"  
RUN mkdir -p "$BDE_ROOT_DIR"  
  
# Clone BDE components  
  
RUN echo 'Getting BDE source components.'  
RUN mkdir /build  
COPY build /build  
RUN build/getSourceCode.sh $BDE_ROOT_DIR/BDEEventDetection/  
  
RUN cd "$BDE_ROOT_DIR/BDEEventDetection"; BRANCH="$(cat /branchname)"; >&2
echo "Using branch [$BRANCH]"; git checkout $BRANCH;  
RUN echo 'Building.'  
# Build  
# make sure you copy maven settings and compile in a single run command. The
maven container will delete ~/.m2 contents  
# as each intermediate container for each command exits  
RUN cd $BDE_ROOT_DIR/BDEEventDetection; cp bde-mvn-settings.xml
/root/.m2/settings.xml; mvn -q package; cp -r /root/.m2/repository /maven-
repository  
RUN rm -rf /build /branchname  
  
########################################  
## Get and build miscellaneous sources  
########################################  
# rest services  
COPY rest $REST_SERVICES_DIR  
RUN $REST_SERVICES_DIR/getSourceCodeRest.sh $REST_SERVICES_DIR  
  
########################################  
## Add and configure interface  
########################################  
  
### Create environment variables from build args  
ENV MOUNT_DIR="$MOUNT_DIR"  
ENV LOG_DIR="$LOG_DIR"  
ENV CONNECTIONS_CONFIG_FOLDER="$CONNECTIONS_CONFIG_FOLDER"  
ENV SUPPLIED_NEWS_PROPS_FILE="$SUPPLIED_NEWS_PROPS_FILE"  
ENV SUPPLIED_NEWS_URLS_FILE="$SUPPLIED_NEWS_URLS_FILE"  
ENV SUPPLIED_BLOG_PROPS_FILE="$SUPPLIED_BLOG_PROPS_FILE"  
ENV SUPPLIED_BLOG_URLS_FILE="$SUPPLIED_BLOG_URLS_FILE"  
ENV SUPPLIED_CLUSTER_PROPS_FILE="$SUPPLIED_CLUSTER_PROPS_FILE"  
ENV SUPPLIED_LOCATION_PROPS_FILE="$SUPPLIED_LOCATION_PROPS_FILE"  
ENV SUPPLIED_TWITTER_QUERIES_FILE="$SUPPLIED_TWITTER_QUERIES_FILE"  
ENV SUPPLIED_TWITTER_PROPS_FILE="$SUPPLIED_TWITTER_PROPS_FILE"  
ENV SUPPLIED_TWITTER_ACCOUNTS_FILE="$SUPPLIED_TWITTER_ACCOUNTS_FILE"  
ENV SUPPLIED_CRONTAB_FILE="$SUPPLIED_CRONTAB_FILE"  
ENV DAEMON_DIRECTORY "$DAEMON_DIRECTORY"  
  
ENV REST_SERVICES_DIR "$REST_SERVICES_DIR"  
  
  
# create directories  
RUN mkdir -p $MOUNT_DIR  
RUN mkdir -p $LOG_DIR  
  
### Daemon interface  
  
RUN echo "Setting up the init-daemon interface."  
# declare and set environment variables required for interaction with the  
# init daemon to their default values. Stepname can/will be set at the  
# daemonInterface.sh (TBD)  
  
RUN echo >&2 "****************" && echo >&2 "Disabling the daemon interface
for testing".  
ENV ENABLE_INIT_DAEMON false  
ENV INIT_DAEMON_BASE_URI http://identifier/init-daemon  
ENV INIT_DAEMON_STEP default_step_name  
  
# make a dedicated directory for the daemon interface and a mount point  
# daemon scripts will be placed there. Is a build arg (default=/daemon).  
# also add the DAEMON_DIRECTORY name to /root keep track of the location in a  
# built image  
RUN echo "$DAEMON_DIRECTORY" > /root/daemonDirLoc  
RUN mkdir -p $DAEMON_DIRECTORY  
  
# copy the main script that will manage the interface with the remote daemon  
# and the query scripts the perform the querying at each stage  
# run your work right after the execute-step.sh call  
COPY daemon/* $DAEMON_DIRECTORY/  
  
# set the executable bit for the scripts  
RUN chmod +x $DAEMON_DIRECTORY/*.sh  
  
# set sleep times for wait - execute - finish daemon probe scripts  
ENV SLEEP_WAIT 1  
ENV SLEEP_EXEC 1  
ENV SLEEP_FINISH 1  
  
#### Testing:  
# To override the default daemon URI ( e.g. for testing purposes ),  
# you can add a override file with another address.  
# Mount as data volume to a mount point and write in it  
# the override daemon address.  
  
ENV DAEMON_INFO_FILE $DAEMON_DIRECTORY/daemoninfo  
RUN echo "init-daemon interface setup complete."  
### End of Daemon interface  
  
########################################  
### Execution  
########################################  
# copy the execution scripts for each module  
# set env. variables  
# bde execution scripts directory  
ENV EXEC_DIR="/bdex"  
# the classpath with all required jars  
ENV CLASSPATHFILE $EXEC_DIR/classpathfile  
# initialization flag file  
ENV INITIALIZATION_FILE="$EXEC_DIR/.initialized"  
# create folders, copy execution and auxilliary scripts  
RUN mkdir -p "$EXEC_DIR"  
COPY exec/* $EXEC_DIR/  
  
# copy the entrypoint driver script and utility scripts  
COPY driver.sh setprops.sh setsources.sh setauth.sh skel.sh /  
  
# set execution bit  
RUN chmod +x $EXEC_DIR/* /driver.sh  
  
# store the environment variables on a file to help with  
# cron-scheduled runs  
RUN printenv > ~/envvars  
  
  
  
  
# Define default command.  
CMD ["/driver.sh"]  
  
  
  
  
  

