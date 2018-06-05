FROM python:alpine  
  
ARG BUILD_DATE  
ARG SOURCE_COMMIT  
ARG VERSION  
  
LABEL org.label-schema.schema-version="1.0" \  
org.label-schema.description="Reduce Arabic strings to their rasm, ie remove
vocalization and other diacritics." \  
org.label-schema.name="rasmify" \  
org.label-schema.version=$VERSION \  
org.label-schema.usage="/src/README.rst" \  
org.label-schema.url="https://github.com/telota/rasmipy" \  
org.label-schema.vcs-url="https://github.com/telota/rasmipy" \  
org.label-schema.docker.cmd="docker run --rm telota/rasmify" \  
org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.vcs-ref=$SOURCE_COMMIT  
  
ENV PORT=80  
EXPOSE 80  
ENTRYPOINT ["/sbin/tini", "--"]  
CMD ["rasmify-rest-service"]  
  
COPY . /src  
RUN cd /src \  
&& apk add --no-cache tini \  
&& pip install --no-cache-dir .[rest-service]  

