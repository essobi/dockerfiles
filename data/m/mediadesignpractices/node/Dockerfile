FROM mediadesignpractices/debian:latest  
LABEL organization "Media Design Practices"  
LABEL maintainer "mediadesignpractices"  
LABEL contributor "unsalted"  
LABEL test "test"  
  
ENV NPM_CONFIG_LOGLEVEL info  
ENV NODE_VERSION 6.10.2  
ENV YARN_VERSION 0.21.3  
# add node group to user  
USER root  
RUN groupadd --gid 9000 node \  
&& usermod -a -G node mdp  
  
RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.xz" \  
&& curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt" \  
&& grep "node-v$NODE_VERSION-linux-x64.tar.xz\$" SHASUMS256.txt | sha256sum -c
- \  
&& tar -xJf "node-v$NODE_VERSION-linux-x64.tar.xz" -C /usr/local \--strip-
components=1 \  
&& rm "node-v$NODE_VERSION-linux-x64.tar.xz" SHASUMS256.txt \  
&& ln -s /usr/local/bin/node /usr/local/bin/nodejs  
  
# include yarn for future proofing  
RUN set -ex \  
&& for key in \  
6A010C5166006599AA17F08146C2130DFD2497F5 \  
; do \  
gpg --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys "$key"; \  
done \  
&& curl -fSL -o yarn.js "https://yarnpkg.com/downloads/$YARN_VERSION/yarn-
legacy-$YARN_VERSION.js" \  
&& curl -fSL -o yarn.js.asc "https://yarnpkg.com/downloads/$YARN_VERSION/yarn-
legacy-$YARN_VERSION.js.asc" \  
&& gpg --batch --verify yarn.js.asc yarn.js \  
&& rm yarn.js.asc \  
&& mv yarn.js /usr/local/bin/yarn \  
&& chmod +x /usr/local/bin/yarn  
  
USER $NB_USER  
WORKDIR $WORK_DIR  
  
CMD [ "node" ]

