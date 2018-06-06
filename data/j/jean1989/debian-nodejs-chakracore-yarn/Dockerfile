FROM jean1989/debian-nodejs-chakracore  
  
MAINTAINER Jean1989  
  
RUN apt-get update \  
&& apt-get install -y \--no-install-recommends ca-certificates apt-transport-
https \  
&& wget -O - https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add \- \  
&& echo "deb https://dl.yarnpkg.com/debian/ stable main" >>
/etc/apt/sources.list.d/yarn.list \  
&& apt-get update \  
&& apt-get install -y \--no-install-recommends yarn $(apt-mark showauto) \  
&& apt-get clean -y \  
&& apt-get autoclean -y \  
&& apt-get autoremove -y \  
&& rm -rf /usr/share/man /tmp/* /var/cache/apk/* /var/lib/apt/lists/*  
  
CMD ["/bin/bash"]  

