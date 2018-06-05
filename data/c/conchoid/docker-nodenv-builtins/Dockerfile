FROM conchoid/docker-nodenv-builtins:v1.1.2-node0.10.48-1-6.9.5-alpine3.6 AS
node0.10-conchoid  
FROM conchoid/docker-nodenv-builtins:v1.1.2-node0.12.18-1-6.9.5-alpine3.6 AS
node0.12-conchoid  
FROM node:4.8.7-alpine AS node4  
FROM conchoid/docker-nodenv-builtins:v1.1.2-node5.12.0-1-6.9.5-alpine3.6 AS
node5-conchoid  
FROM node:6.9.5-alpine AS node6  
FROM node:7.10.1-alpine AS node7  
FROM node:9.4.0-alpine AS node9  
FROM node:10.3.0-alpine AS node10  
  
FROM conchoid/docker-nodenv:v1.1.2-4-8.9.4-alpine3.6  
ENV NODE010 "0.10.48"  
ENV NODE012 "0.12.18"  
ENV NODE4 "4.8.7"  
ENV NODE5 "5.12.0"  
ENV NODE6 "6.9.5"  
ENV NODE7 "7.10.1"  
ENV NODE8 "8.9.4"  
ENV NODE9 "9.4.0"  
ENV NODE10 "10.3.0"  
ENV PREINSTALLED_VERSIONS "\  
${NODE010}\n\  
${NODE012}\n\  
${NODE4}\n\  
${NODE5}\n\  
${NODE6}\n\  
${NODE7}\n\  
${NODE8}\n\  
${NODE9}\n\  
${NODE10}"  
COPY \--from=node0.10-conchoid "${NODENV_ROOT}/versions/${NODE010}"
"${NODENV_ROOT}/versions/${NODE010}"  
COPY \--from=node0.12-conchoid "${NODENV_ROOT}/versions/${NODE012}"
"${NODENV_ROOT}/versions/${NODE012}"  
COPY \--from=node4 "/usr/local/bin/node"
"${NODENV_ROOT}/versions/${NODE4}/bin/"  
COPY \--from=node5-conchoid "${NODENV_ROOT}/versions/${NODE5}"
"${NODENV_ROOT}/versions/${NODE5}"  
COPY \--from=node6 "/usr/local/bin/node"
"${NODENV_ROOT}/versions/${NODE6}/bin/"  
COPY \--from=node7 "/usr/local/bin/node"
"${NODENV_ROOT}/versions/${NODE7}/bin/"  
COPY \--from=node9 "/usr/local/bin/node"
"${NODENV_ROOT}/versions/${NODE9}/bin/"  
COPY \--from=node10 "/usr/local/bin/node"
"${NODENV_ROOT}/versions/${NODE10}/bin/"  
COPY \--from=node4 "/usr/local/lib/node_modules"
"${NODENV_ROOT}/versions/${NODE4}/lib/node_modules"  
COPY \--from=node6 "/usr/local/lib/node_modules"
"${NODENV_ROOT}/versions/${NODE6}/lib/node_modules"  
COPY \--from=node7 "/usr/local/lib/node_modules"
"${NODENV_ROOT}/versions/${NODE7}/lib/node_modules"  
COPY \--from=node9 "/usr/local/lib/node_modules"
"${NODENV_ROOT}/versions/${NODE9}/lib/node_modules"  
COPY \--from=node10 "/usr/local/lib/node_modules"
"${NODENV_ROOT}/versions/${NODE10}/lib/node_modules"  
  
RUN set -x \  
&& mkdir -p "${NODENV_ROOT}/versions/${NODE8}/bin/"
"${NODENV_ROOT}/versions/${NODE8}/lib/" \  
&& cp "$(nodenv which node)" "${NODENV_ROOT}/versions/${NODE8}/bin/" \  
&& cp -R "/usr/local/lib/node_modules" "${NODENV_ROOT}/versions/${NODE8}/lib/"
\  
&& echo -e ${PREINSTALLED_VERSIONS} | while read version;do \  
NPM_SRC="${NODENV_ROOT}/versions/${version}/lib/node_modules/npm/bin/npm-
cli.js" \  
&& NPM_DST="${NODENV_ROOT}/versions/${version}/bin/npm" \  
# Override the shebang line of npm-cli.js to use the "node" path dynamically.  
&& sed -i -E "1s/#.+/#!\/usr\/bin\/env node/" "${NPM_SRC}" \  
&& ln -s -f "${NPM_SRC}" "${NPM_DST}";done \  
&& nodenv rehash \  
&& npm set progress false --global --quiet  

