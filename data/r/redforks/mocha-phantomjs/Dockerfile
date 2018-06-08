FROM wernight/phantomjs  
  
MAINTAINER Red Forks <redforks@gmail.com>  
  
USER root  
  
RUN apt-get update && apt-get install -y curl && curl -sL
https://deb.nodesource.com/setup_6.x | bash - && apt-get install -y nodejs &&
npm install -g mocha-phantomjs && apt-get purge --auto-remove -y curl && apt-
get clean && rm -rf /var/lib/apt/lists/*  
  
# switch to uid/gid identical to host uid/gid (forks/users), if not doing
this, files that  
# clang-format written will change user and group all to root.  
USER 1000  
  
CMD ["/usr/bin/mocha-phantomjs"]  
  

