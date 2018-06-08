FROM cybe/ps-base:alpine36  
  
ENV GITEA_PATH=/gitea GITEA_CUSTOM=/gitea/custom USER=git TZ=Europe/Berlin  
  
COPY start_with_secret.sh ${GITEA_PATH}/  
COPY app.ini ${GITEA_CUSTOM}/conf/  
  
RUN apk --no-cache add --virtual .build-deps go build-base git grep \  
# Prepare build environment  
&& export GOPATH=/tmp/go \  
&& mkdir -p ${GOPATH} \  
&& export PATH=${PATH}:${GOPATH}/bin \  
&& export APP_PATH=${GITEA_PATH}/app \  
# Fetch gitea  
&& mkdir -p ${GOPATH}/src/code.gitea.io \  
&& git clone -b release/v1.1 \--single-branch https://github.com/go-
gitea/gitea.git ${GOPATH}/src/code.gitea.io/gitea \  
&& cd ${GOPATH}/src/code.gitea.io/gitea \  
# Cherry pick two fixes  
&& git remote add fork https://github.com/cybe/gitea.git \  
&& git fetch fork \  
&& git config --local user.email "none@example.org" \  
&& git cherry-pick fork/api_bare_repos fork/ssh_parse_env \  
# Vendor custom git module  
&& go get -u github.com/kardianos/govendor \  
&& govendor fetch github.com/cybe/git@handle_bare_repos \  
&& govendor remove code.gitea.io/git \  
&& grep -r -l --null "\"code.gitea.io/git\"" . | xargs -0 sed -i
's|"code.gitea.io/git"|"github.com/cybe/git"|g' \  
# Build gitea  
&& make build TAGS="sqlite" \  
# Install gitea  
&& mkdir -p ${APP_PATH} \  
&& cp -r gitea options templates public scripts ${APP_PATH} \  
&& rm -rf ${APP_PATH}/public/config.codekit ${APP_PATH}/public/less \  
&& cd / \  
# Setup user and environment for gitea  
&& adduser -H -D -h ${GITEA_PATH}/data/home -s /bin/sh -g "Gitea Git User"
${USER} \  
&& mkdir -p ${GITEA_PATH}/logs ${GITEA_PATH}/tmp \  
&& chown -R ${USER}: ${GITEA_PATH} \  
# Cleanup  
&& rm -rf ${GOPATH} \  
&& apk --no-cache add git tzdata openssh-client \  
&& apk del --purge .build-deps  
  
USER git  
  
CMD ["di", "--", "/gitea/start_with_secret.sh", "/gitea/app/gitea", "web"]  

