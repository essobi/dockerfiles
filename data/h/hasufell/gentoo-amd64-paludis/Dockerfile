FROM busybox  
MAINTAINER Julian Ospald <hasufell@posteo.de>  
  
# This one should be present by running the build.sh script  
COPY build.sh bootstrap.sh /  
  
# one step, to make the layer as thin as possible  
# bootstrap.h calls build.sh  
RUN /bootstrap.sh amd64 x86_64  
  
# update etc files... hope this doesn't screw up  
RUN etc-update --automode -5  
  
# don't allow regular sync, because we want to make sure  
# all images deriving from this one have the same state  
RUN sed -i -e 's|^sync|#sync|' /etc/paludis/repositories/*.conf  
  
# copy hooks  
COPY ./config/paludis /etc/paludis  
  

