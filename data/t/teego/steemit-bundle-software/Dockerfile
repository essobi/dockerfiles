  
FROM teego/steemit-bundle-system:latest  
MAINTAINER Aleksandr Zykov <tiger@mano.email>  
  
RUN figlet 'Building'  
  
RUN ( \  
apt-get install -qy --no-install-recommends \  
git \  
build-essential \  
) && \  
apt-get clean -qy  
  
RUN ( \  
npm install --no-optional -g \  
babel-cli \  
sequelize-cli \  
node-gyp \  
)  
  
ENV NODE_ENV development  
  
ENV STEEMIT_REPOSITORY https://github.com/steemit/steemit.com  
ENV STEEMIT_COMMIT ab4be6a84ccd3f0e15ec2045db48172f30bbc0e8  
  
RUN figlet 'steemit.com '  
  
RUN ( \  
cd /root; \  
git clone $STEEMIT_REPOSITORY steemit \  
)  
  
RUN cd /root/steemit; \  
( \  
/usr/bin/test -n "$STEEMIT_COMMIT" && \  
git checkout $STEEMIT_COMMIT || \  
/bin/true \  
)  
  
ADD dev.config.js.diff /root/steemit/webpack/dev.config.js.diff  
  
RUN cd /root/steemit/webpack/; \  
( \  
cat dev.config.js.diff && \  
patch <dev.config.js.diff \  
)  
  
ADD server.js.diff /root/steemit/server/server.js.diff  
  
RUN cd /root/steemit/server/; \  
( \  
cat server.js.diff && \  
patch <server.js.diff \  
)  
  
ADD package.json.diff /root/steemit/  
  
RUN cd /root/steemit/; \  
( \  
cat package.json.diff && \  
patch <package.json.diff \  
)  
  
RUN cd /root/steemit/; \  
( \  
NODE_ENV=development npm install --no-optional --no-shrinkwrap \  
)  
  
ADD babelrc.diff /root/steemit/babelrc.diff  
  
RUN cd /root/steemit/; \  
( \  
cat babelrc.diff && \  
patch <babelrc.diff \  
)  
  
RUN cd /root/steemit/; \  
( \  
npm run build \  
)  
  
CMD ["/bin/bash"]  
  
RUN figlet 'Ready!'  

