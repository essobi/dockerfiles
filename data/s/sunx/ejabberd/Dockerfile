FROM alpine:3.4  
MAINTAINER Vladimir Goshev <sunx@sunx.name>  
  
# DATA_DIR:  
# Where we will store config and db.  
# Also it's user home directory.  
# Default: /home/ejabberd  
#  
# SW_VERSION:  
# Version of ejabberd  
# which we want to use for our Mozilla Syncserver  
# uUID - set UID of ffsync user, default: 2016  
# uGID - set GID of ffsync user, default: 2016  
ENV DATA_DIR="/home/ejabberd" \  
SW_VERSION="17.08"  
# All installation proccess is in build.sh  
# It is possible to do all work via RUN command(s)  
# But it looks much better with all work in script  
COPY build.sh /tmp/build.sh  
# Execute our build script and delete it because we won't need it anymore  
RUN /tmp/build.sh "$SW_VERSION" "$DATA_DIR" && rm /tmp/build.sh  
  
# Container initialization scripts  
COPY docker-run.sh /bin/docker-run  
  
EXPOSE 5222 5296  
VOLUME $DATA_DIR  
  
USER ejabberd  
  
# Container will execute /bin/docker-run with user access to configure (if
needed) and run  
# Ejabberd  
CMD ["/bin/docker-run"]  

