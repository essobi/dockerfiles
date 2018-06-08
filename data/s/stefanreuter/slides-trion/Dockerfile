FROM tgbyte/slides-base  
  
ADD . /home/slides  
  
ONBUILD ARG UID  
ONBUILD ENV RUN_AS=${UID:-www}  
ONBUILD USER root  
ONBUILD ADD . /home/slides  
ONBUILD RUN generate && \  
chown -R $RUN_AS /home/slides  
ONBUILD USER $RUN_AS  

