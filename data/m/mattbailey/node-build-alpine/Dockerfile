FROM node:8-alpine  
  
RUN set -ex; \  
mkdir -p /usr/src/app; \  
apk --no-cache add tini  
  
WORKDIR /usr/src/app  
  
ONBUILD ARG NPM_CONFIG_REGISTRY=https://registry.npmjs.org  
ONBUILD ENV NPM_CONFIG_REGISTRY $NPM_CONFIG_REGISTRY  
  
ONBUILD ARG ENVIRONMENT=production  
ONBUILD ENV ENVIRONMENT $ENVIRONMENT  
  
ONBUILD ARG NODE_ENV=production  
ONBUILD ENV NODE_ENV $NODE_ENV  
  
ONBUILD ARG BABEL_ENV=production  
ONBUILD ENV BABEL_ENV $NODE_ENV  
  
ONBUILD ARG GITHUB_TOKEN=''  
ONBUILD ENV GITHUB_TOKEN $GITHUB_TOKEN  
  
ONBUILD ENV npm_config_progress false  
ONBUILD ENV npm_config_loglevel error  
  
# Comments for labels are relative to using drone  
# Get rev SHA1: --build-arg LABEL_VCS_REF=${DRONE_COMMIT_SHA:-none}  
ONBUILD ARG LABEL_VCS_REF=none  
# Get git url: --build-arg LABEL_VCS_URL=${DRONE_REPO_LINK:-none}  
ONBUILD ARG LABEL_VCS_URL=none  
# Get name of this program: --build-arg LABEL_NAME=${DRONE_REPO_NAME:-none}  
ONBUILD ARG LABEL_NAME=none  
# Get version with: --build-arg LABEL_VERSION=${DRONE_TAG:-v0.0.0}  
ONBUILD ARG LABEL_VERSION=v0.0.0  
# Epoch 1 in RFC 3339  
# Get correct time with: --build-arg LABEL_BUILD_DATE=`date -u
+'%Y-%m-%dT%H:%M:%SZ'`  
ONBUILD ARG LABEL_BUILD_DATE="1969-12-31T16:00:00Z"  
ONBUILD LABEL \  
org.label-schema.vcs-ref=$LABEL_VCS_REF \  
org.label-schema.vcs-url=$LABEL_VCS_URL \  
org.label-schema.name=$LABEL_NAME \  
org.label-schema.version=$LABEL_VERSION \  
org.label-schema.schema-version=1.0 \  
org.label-schema.build-date=$LABEL_BUILD_DATE  
  
ONBUILD COPY package.json /usr/src/app  
ONBUILD COPY yarn.lock /usr/src/app  
ONBUILD RUN set -ex; \  
yarn config set registry $NPM_CONFIG_REGISTRY; \  
until yarn install --silent --skip-integrity-check --no-progress --no-emoji; \  
do echo "*** Yarn retrying ***"; \  
done; \  
yarn cache clean --force  
ONBUILD COPY . /usr/src/app  
ONBUILD WORKDIR /usr/src/app  
  
ONBUILD ENTRYPOINT ["/sbin/tini", "--"]  
ONBUILD CMD ["yarn", "start"]  

