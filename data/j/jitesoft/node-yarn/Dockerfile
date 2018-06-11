FROM jitesoft/node-base:9  
LABEL maintainer="Johannes Tegnér <johannes@jitesoft.com>"  
  
ENV YARN_VERSION="1.3.2" \  
PATH="$PATH:/yarn/bin"  
RUN apk add --no-cache git \  
&& apk add \--no-cache --virtual trash gnupg \  
&& wget -qO- https://dl.yarnpkg.com/debian/pubkey.gpg | gpg --import \  
&& wget
https://github.com/yarnpkg/yarn/releases/download/v${YARN_VERSION}/yarn-v${YARN_VERSION}.tar.gz
\  
&& wget -O keys.asc
https://github.com/yarnpkg/yarn/releases/download/v${YARN_VERSION}/yarn-v${YARN_VERSION}.tar.gz.asc
\  
&& gpg --verify keys.asc yarn-v${YARN_VERSION}.tar.gz \  
&& mkdir /yarn \  
&& tar -xzvf yarn-v${YARN_VERSION}.tar.gz -C /yarn --strip-components=1 \  
&& rm -r yarn-v${YARN_VERSION}.tar.gz keys.asc \  
&& apk del trash  
  
ENTRYPOINT [ "yarn" ]

