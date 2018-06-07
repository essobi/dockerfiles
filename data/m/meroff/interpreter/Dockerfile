FROM frolvlad/alpine-oraclejdk8:full  
ADD . /code/  
RUN apk add --no-cache libstdc++ && \  
echo '{ "allow_root": true }' > /root/.bowerrc && \  
rm -Rf /code/target /code/node_modules && \  
cd /code/ && \  
./mvnw clean package -Pprod -DskipTests && \  
mv /code/target/*.war /app.war  
  
FROM frolvlad/alpine-oraclejdk8:full  
ENV SPRING_OUTPUT_ANSI_ENABLED=ALWAYS \  
JHIPSTER_SLEEP=0 \  
JAVA_OPTS=""  
EXPOSE 8081  
CMD echo "The application will start in ${JHIPSTER_SLEEP}s..." && \  
sleep ${JHIPSTER_SLEEP} && \  
java ${JAVA_OPTS} -Djava.security.egd=file:/dev/./urandom -jar /app.war  
COPY \--from=0 /app.war .  

