FROM progrium/cedarish:cedar14  
MAINTAINER Jeff Lindsay <progrium@gmail.com>  
  
ADD ./stack/configs/etc-profile /etc/profile  
  
ADD ./builder/ /build  
RUN xargs -L 1 /build/install-buildpack /tmp/buildpacks <
/build/config/buildpacks.txt  
  
RUN gem install foreman  
  
ENV PORT 5000  
EXPOSE 5000  

