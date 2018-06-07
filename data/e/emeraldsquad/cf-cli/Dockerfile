FROM emeraldsquad/alpine-scripting  
  
ENV CF_CLI_VERSION=6.32.0  
RUN wget -q -O -
'https://cli.run.pivotal.io/stable?release=linux64-binary&source=github&version='${CF_CLI_VERSION}
\  
| tar -xzf - -C /usr/bin

