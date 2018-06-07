FROM learninglayers/base  
MAINTAINER Yordan Manolov <manolov@dbis.rwth-aachen.de>  
  
ENV PWMCONF /opt/conf  
ENV PWMACC /opt/account  
RUN mkdir -p $PWMCONF $PWMACC  
ADD conf/ $PWMCONF  
ADD account/ $PWMACC  
  
VOLUME ["$PWMCONF","$PWMACC"]  

