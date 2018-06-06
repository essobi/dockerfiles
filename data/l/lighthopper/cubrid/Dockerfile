FROM centos:6.6  
# The same environment variables exported by  
# /etc/profile.d/cubrid.  
ENV CUBRID_USER=cubrid  
ENV CUBRID=/opt/$CUBRID_USER  
ENV CUBRID_DATABASES=$CUBRID/databases  
ENV CUBRID_LOGS=$CUBRID/log  
ENV CUBRID_CHARSET=en_US  
ENV CUBRID_VERSION=10.0.0  
ENV CUBRID_PATCH_NUMBER=1376  
ENV LD_LIBRARY_PATH=$CUBRID/lib  
ENV PATH=$CUBRID/bin:$PATH  
  
RUN rpm -ivh
http://ftp.cubrid.org/CUBRID_Engine/$CUBRID_VERSION/cubrid-$CUBRID_VERSION.$CUBRID_PATCH_NUMBER-
el5.x86_64.rpm  
  
# Switch to `cubrid` user.  
USER $CUBRID_USER  
  
# Switch to `cubrid` home directory.  
WORKDIR $CUBRID  
  
# Add a script to create and start "demodb" database.  
ADD create-start-demodb.sh $CUBRID  
  
EXPOSE 33000 30000 8001 8002 1523  
# `tail -f /dev/null` trick is to keep the foreground process always ON.  
# Otherwise, the `cubrid` command quits as soon as it successfully  
# starts up all the necessary services.  
CMD cubrid service start && tail -f $CUBRID_LOGS/**/* $CUBRID_LOGS/**/**/*  

