FROM node:5.12.0  
# FROM meteorhacks/meteord:devbuild  
  
LABEL net.quadric.vendor="Quadric ApS" maintainer="Ahmed Magdy
<ahmed.magdy@quadric.net>"  
# ENV DEBIAN_FRONTEND noninteractive  
# RUN apt-get update && \  
# apt-get install -y curl && \  
# curl -sL https://deb.nodesource.com/setup_4.x | bash - && \  
# apt-get install -y nodejs --no-install-recommends && \  
# rm -rf /var/lib/apt/lists/*  
# RUN apt-get update -qq && apt-get install -y locales -qq && locale-gen
en_US.UTF-8 en_us && dpkg-reconfigure locales && locale-gen C.UTF-8 &&
/usr/sbin/update-locale LANG=C.UTF-8  
# ENV LANG C.UTF-8  
# ENV LANGUAGE C.UTF-8  
# ENV LC_ALL C.UTF-8  
  
RUN npm i -g yarn  
  
#RUN ln -s /usr/local/bin/node /usr/local/bin/nodejs  
RUN curl -sL https://install.meteor.com/?release=1.4.2.7 | sed s/--progress-
bar/-sL/g | /bin/sh  

