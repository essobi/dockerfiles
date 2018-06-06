ARG MC_IMAGE_TAG=3.10  
FROM hazelcast/management-center:${MC_IMAGE_TAG}  
  
ENV USER_NAME=hazelcast  
ENV USER_UID=10001  
### Configure user  
RUN useradd -l -u $USER_UID -r -g 0 -d $MC_HOME -s /sbin/nologin -c
"${USER_UID} application user" $USER_NAME  
RUN chown -R $USER_UID:0 $HZ_HOME $MANCENTER_DATA  
RUN chmod +x $MC_HOME/*.sh  
  
USER $USER_UID  

