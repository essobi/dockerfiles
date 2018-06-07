FROM node:9.3.0-alpine  
  
CMD ["ng"]  
  
ENTRYPOINT ["ng"]  
  
RUN npm i -g @angular/cli  
  
ARG SCHEMA=org.label-schema  
ARG SITE=site.gruen  
ARG BUILD_DATE  
ARG GIT_SHA  
  
LABEL ${SCHEMA}.build-date=${BUILD_DATE} \  
${SCHEMA}.vcs-ref=${GIT_SHA} \  
${SCHEMA}.vendor="gruen" \  
${SCHEMA}.name="angular-cli" \  
${SCHEMA}.vcs-url="https://github.com/darrengruen/docker-angular-cli" \  
${SCHEMA}.schema-version="1.0" \  
${SCHEMA}.docker.cmd.help="docker run $CONTAINER help" \  
${SITE}.author="Darren Green <darren@gruen.site>" \  
${SITE}.version="0.0.1"  
  

