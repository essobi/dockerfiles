FROM ourtownrentals/git-deploy  
  
ENV NODE_ENV production  
  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="hiera-deploy" \  
org.label-schema.description="Dockerized Triggered Git Deployment Server" \  
org.label-schema.url="http://andradaprieto.es" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/jandradap/LARP" \  
org.label-schema.vendor="Jorge Andrada Prieto" \  
org.label-schema.version=$VERSION \  
org.label-schema.schema-version="1.0" \  
maintainer="Jorge Andrada Prieto <jandradap@gmail.com>" \  
org.label-schema.docker.cmd="docker run -p 443:443 -v
$(pwd)/test/private:/etc/ssl/private jorgeandrada/hiera-deploy"  
  
EXPOSE 443  
  
RUN mkdir -p /etc/puppetlabs/hiera  
  
COPY index.js /usr/src/app/  
  
VOLUME /srv  
  
WORKDIR /usr/src/app  
  
ENTRYPOINT ["npm"]  
  
CMD ["start"]  

