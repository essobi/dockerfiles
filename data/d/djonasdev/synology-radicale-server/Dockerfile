FROM alpine:3.7  
LABEL Dominic Jonas <info@dominic-jonas.de>  
  
###################################################  
# UserId and GroupId #  
# The ids of the user running the radicale server #  
# The mounted directory will get this permissions #  
###################################################  
ENV UID="1036"  
ENV GID="1036"  
####################################################  
# All installation proccess is in build.sh #  
# It is possible to do all work via RUN command(s) #  
# But it looks much better with all work in script #  
####################################################  
COPY build.sh /tmp/build.sh  
  
###########################################################################  
# Execute our build script and delete it because we won't need it anymore #  
###########################################################################  
RUN /tmp/build.sh && rm /tmp/build.sh  
  
####################  
# Copy config file #  
####################  
COPY radicale.ini /usr/local/share/radicale.ini  
  
####################################  
# Container initialization scripts #  
####################################  
COPY docker-run docker-run-root /bin/  
####################  
# Set network port #  
####################  
EXPOSE 5232  
######################################  
# Set mount point #  
# Where we will store config and db. #  
######################################  
VOLUME "/data"  
################################################################################################  
# Container will run some preparations with root access (create your user,
fixing permissions) #  
# and then execute /bin/docker-run with user access to configure (if needed)
and run #  
# radicale #  
################################################################################################  
CMD ["/bin/docker-run-root"]

