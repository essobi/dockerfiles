FROM improving/java  
  
VOLUME "/opt/app/run"  
WORKDIR /opt/app  
COPY src/spring.sh spring.sh  
  
ARG user=spring  
RUN addgroup -g 1000 ${user} \  
&& adduser -h "/opt/app" -u 1000 -G ${user} -s /bin/bash -D ${user} \  
&& chown -R ${user}:${user} /opt/app/  
USER ${user}  
  
# docker build --force-rm -t improving-spring .  
# docker tag improving-spring improving/spring  
# docker run --rm -e JAVA_TIMEZONE=America/Sao_Paulo -v
~/tmp/improving/app/target/docker:/opt/app/run improving-spring  
ENV APPNAME "app"  
#Java  
ENV JAVA_OPTS ""  
#Spring  
ENV SPRING_PROFILE ""  
#BD  
ENV PG_URL "<<localhost>>"  
ENV PG_USER "postgres"  
ENV PG_PASS "postgres"  
#Apenas Dev  
ENV AWS_ACCESS_KEY ""  
ENV AWS_SECRET_KEY ""  
EXPOSE 8080  
CMD /opt/app/spring.sh

