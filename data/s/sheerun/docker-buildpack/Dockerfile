FROM heroku/cedar:14  
ENV HOME /app  
ENV APP_DIR /app  
ENV REQUEST_ID build-0  
ENV STACK cedar-14  
ENV CURL_TIMEOUT 30  
ENV CURL_CONNECT_TIMEOUT 180  
WORKDIR $HOME  
  
RUN rm -rf $HOME && mkdir -p $HOME/.profile.d && touch
$HOME/.profile.d/empty.sh && echo "for script in \$HOME/.profile.d/*.sh ; do .
\$script; done" > /$HOME/.profile  
  
RUN printf "#!/bin/bash -l\nexec \"\$@\"" > /bin/env-exec && chmod a+x
/bin/env-exec  
  
RUN printf "#!/bin/bash -l\nexec /bin/sh -c \"\$@\"" > /bin/env-shell && chmod
a+x /bin/env-shell  
  
SHELL ["/bin/env-shell"]  
  
ENTRYPOINT ["/bin/env-exec"]  
  
ADD buildpack /usr/bin/buildpack  
  
ADD start /usr/bin/start  

