FROM ruby:2.5.0-alpine3.7  
WORKDIR /sass  
  
VOLUME ["/sass/src", "/sass/output"]  
  
CMD ["sass"]  
  
ENTRYPOINT ["sass"]  
  
RUN apk add --update alpine-sdk \  
&& gem install sass  
  
ARG SCHEMA=org.schema-label  
ARG SITE=site.gruen  
ARG BUILD_DATE  
ARG GIT_SHA  
  
LABEL ${SCHEMA}.build-date=${BUILD_DATE} \  
${SCHEMA}.vcs-ref=${GIT_SHA} \  
${SCHEMA}.vcs-url="https://github.com/darrengruen/docker-sass" \  
${SCHEMA}.name="sass" \  
${SCHEMA}.description="SASS in a Docker container" \  
${SITE}.author="Darren Green <darren@gruen.site>"  
  

