FROM progrium/cedarish:cedar14  
MAINTAINER Jaigouk Kim <ping@jaigouk.kim>  
  
ADD ./stack/configs/etc-profile /etc/profile  
  
ADD ./builder/ /build  
RUN xargs -L 1 /build/install-buildpack /tmp/buildpacks <
/build/config/buildpacks.txt  

