FROM mhart/alpine-node:6.8  
ARG HACKMD_VERSION=0.4.5  
ENV HACKMD_REPO_URL https://github.com/hackmdio/hackmd.git  
ENV HACKMD_DIR /opt/hackmd  
  
ENV POSTGRES_USER hackmd  
ENV POSTGRES_PASSWORD hackmdpass  
ENV POSTGRES_DB hackmd  
ENV POSTGRES_HOST database  
ENV POSTGRES_PORT 5432  
ENV CFG_URLADDPORT true  
ENV CFG_DIALECT postgres  
ENV CFG_DOMAIN "hackmd.io"  
ENV CFG_URL_PATH "hackmd"  
ENV CFG_DEBUG false  
ENV CFG_GOOGLE_API_KEY ""  
ENV CFG_GOOGLE_CLIENT_ID ""  
ENV CFG_DROPBOX_APP_KEY ""  
ENV NODE_ENV production  
  
RUN apk add --update \  
git \  
python \  
alpine-sdk && \  
git clone ${HACKMD_REPO_URL} ${HACKMD_DIR} && \  
cd /opt/hackmd && \  
git checkout tags/${HACKMD_VERSION} -b release-${HACKMD_VERSION} && \  
npm install && \  
npm install -g bower && \  
bower install --allow-root  
  
COPY assets/* ${HACKMD_DIR}/  
  
WORKDIR ${HACKMD_DIR}  
  
ENTRYPOINT [ "/opt/hackmd/docker-entrypoint.sh" ]  
  
EXPOSE 3000  

