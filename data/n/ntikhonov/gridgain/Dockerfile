#  
# Copyright (C) GridGain Systems. All Rights Reserved.  
# _________ _____ __________________ _____  
# __ ____/___________(_)______ /__ ____/______ ____(_)_______  
# _ / __ __ ___/__ / _ __ / _ / __ _ __ `/__ / __ __ \  
# / /_/ / _ / _ / / /_/ / / /_/ / / /_/ / _ / _ / / /  
# \\____/ /_/ /_/ \\_,__/ \\____/ \\__,_/ /_/ /_/ /_/  
#  
FROM java:7  
ENV GRIDGAIN_VERSION 7.4.1  
ENV GRIDGAIN_HOME /opt/gridgain  
  
RUN mkdir -p $GRIDGAIN_HOME  
  
WORKDIR $GRIDGAIN_HOME  
  
ADD http://www.gridgain.com/media/gridgain-enterprise-
fabric-$GRIDGAIN_VERSION.zip $GRIDGAIN_HOME/gridgain.zip  
  
RUN unzip gridgain.zip  
  
RUN rm gridgain.zip  
  
# Copy sh files and set permission  
ADD ./run.sh $GRIDGAIN_HOME/  
  
RUN chmod +x $GRIDGAIN_HOME/run.sh  
  
CMD $GRIDGAIN_HOME/run.sh  

