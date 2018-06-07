FROM fuwanguo/ubuntu:14.04  
ENV SPRING_OUTPUT_ANSI_ENABLED=ALWAYS \  
JHIPSTER_SLEEP=0  
# add source  
ADD . /src/  
  
RUN cd /src/ && \  
./gradlew bootRepackage&& \  
mv /src/build/libs/*.war /app.war  
  
RUN sh -c 'touch /app.war'  
  
VOLUME /tmp  
EXPOSE 8080  
CMD echo "The application will start in ${JHIPSTER_SLEEP}s..." && \  
sleep ${JHIPSTER_SLEEP} && \  
java -Djava.security.egd=file:/dev/./urandom -jar /app.war  

