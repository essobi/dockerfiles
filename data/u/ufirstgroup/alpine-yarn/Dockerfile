FROM ufirstgroup/alpine-npm:7.10.0_4.5.0  
MAINTAINER Jean-Luc Geering <jeanluc.geering@ufirstgroup.com>  
MAINTAINER Michael Ruoss <michael.ruoss@ufirstgroup.com>  
  
# install packages (su-exec and various build dependencies)  
RUN apk update && apk upgrade && apk add \  
g++ \  
make \  
python \  
git  
  
# install yarn  
ENV YARN_VERSION 0.24.5  
RUN apk add --no-cache --virtual .yarn-deps curl gnupg tar && \  
mkdir -p /opt && \  
curl -sL
https://yarnpkg.com/downloads/${YARN_VERSION}/yarn-v${YARN_VERSION}.tar.gz |
tar xz -C /opt && \  
mv /opt/dist /opt/yarn && \  
ln -s /opt/yarn/bin/yarn /usr/local/bin && \  
apk del .yarn-deps  
  
# install node-gyp  
RUN /usr/local/bin/yarn global add node-gyp  
  
USER root  
  
WORKDIR "/workdir"  
  
ENV WORKDIR "/workdir"  
ENV HOMEDIR "/homedir"  
VOLUME ["/workdir", "/homedir"]  
  
COPY entrypoint.sh /  
  
ENTRYPOINT ["/sbin/tini", "--", "/entrypoint.sh"]  
CMD ["yarn"]  

