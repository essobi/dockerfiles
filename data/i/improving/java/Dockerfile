FROM frolvlad/alpine-oraclejdk8:slim  
RUN apk add --no-cache bc coreutils  
  
COPY src/define-java-opts.sh /opt/define-java-opts.sh  
COPY src/improving-entrypoint.sh /opt/improving-entrypoint.sh  
  
# docker build --force-rm -t improving-java .  
# docker tag improving-java improving/java  
# docker run --rm -e JAVA_TIMEZONE=America/Sao_Paulo improving-java  
ENV JAVA_OPTS=""  
ENV JAVA_TIMEZONE=""  
ENTRYPOINT ["/opt/improving-entrypoint.sh"]  
CMD echo $JAVA_OPTS && java -version  

