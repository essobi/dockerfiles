FROM node:4.1.2-slim  
  
COPY Dockerfile /  
  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="Visualizer" \  
org.label-schema.description="Visualizer with path /visualizer" \  
org.label-schema.url="http://andradaprieto.es" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/jandradap/visualizer" \  
org.label-schema.vendor="Jorge Andrada Prieto" \  
org.label-schema.version=$VERSION \  
org.label-schema.schema-version="1.0" \  
maintainer="Jorge Andrada Prieto <jandradap@gmail.com>" \  
org.label-schema.docker.cmd=""  
  
WORKDIR /app/visualizer  
  
# Only run npm install if these files change.  
COPY ./package.json /app/visualizer/package.json  
  
# Install dependencies  
RUN npm install --unsafe-perm=true  
  
# Add the rest of the sources  
COPY . /app/visualizer  
  
# Build the app  
RUN npm run dist  
  
# Number of milliseconds between polling requests. Default is 1000.  
ENV MS 1000  
EXPOSE 8090  
CMD ["npm","start"]  

