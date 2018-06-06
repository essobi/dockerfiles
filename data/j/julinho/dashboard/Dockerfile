FROM node:8  
  
ARG BUILD_DATE  
ARG VCS_REF  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="Julinho IFSC: dashboard" \  
org.label-schema.description="Painel administrativo" \  
org.label-schema.license="MIT" \  
org.label-schema.url="https://marvietech.com.br/blog/" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/julinho-ifsc/dashboard" \  
org.label-schema.vendor="Marvi•E Technologies" \  
org.label-schema.version="8.0" \  
org.label-schema.schema-version="1.0" \  
maintainer="Thiago Santos <thia.mdossantos@gmail.com>"  
  
ENV NPM_CONFIG_LOGLEVEL warn  
ENV HOME=/home/app  
WORKDIR $HOME/dashboard  
  
COPY package.json package-lock.json $HOME/dashboard/  
COPY . $HOME/dashboard  
COPY ./docker-entrypoint.sh /  
RUN chmod 0755 /docker-entrypoint.sh && \  
npm install --silent --progress=false && \  
chown -R node $HOME  
  
RUN npm run build  
  
USER node  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["node", "index.js"]  

