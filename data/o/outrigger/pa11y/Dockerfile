FROM alekzonder/puppeteer:1  
  
# @see http://label-schema.org/rc1/  
LABEL maintainer="Phase2 <outrigger@phase2technology.com>" \  
org.label-schema.vendor="Phase2 <outrigger@phase2technology.com>" \  
org.label-schema.name="Outrigger pa11y" \  
org.label-schema.description="Docker image for pa11y, the CLI-based
accessibility testing tool." \  
org.label-schema.vcs-url="https://github.com/phase2/docker-pa11y" \  
org.label-schema.docker.cmd="docker run -it --rm --cap-add=SYS_ADMIN
outrigger/pa11y http://example.com" \  
org.label-schema.docker.cmd.help="docker run --rm outrigger/pa11y" \  
org.label-schema.docker.debug="docker exec -it $CONTAINER bash" \  
org.label-schema.schema-version="1.0"  
  
USER root  
  
# Let's get pa11y v5 in here.  
RUN yarn global add pa11y@5 && \  
yarn cache clean && \  
chown -R pptruser:pptruser /usr/local/share/.config/yarn/global/node_modules  
  
ENV PATH "/usr/local/share/.config/yarn/global/node_modules/.bin/:${PATH}"  
  
USER pptruser  
  
ENTRYPOINT ["dumb-init", "--", "pa11y"]  
  
CMD ["-h"]  

