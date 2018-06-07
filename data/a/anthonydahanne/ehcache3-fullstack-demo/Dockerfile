FROM jhipster/jhipster:latest  
COPY /fullstack /home/jhipster/fullstack  
USER root  
RUN \  
# fix jhipster user permissions  
chown -R jhipster:jhipster \  
/home/jhipster/fullstack  
  
USER jhipster  
WORKDIR /home/jhipster/fullstack  
  
RUN ./mvnw -Pprod -DskipTests clean package \  
&& mv /home/jhipster/fullstack/target/fullstack-1.0.0-SNAPSHOT.war
/home/jhipster/fullstack/fullstack-1.0.0-SNAPSHOT.war \  
&& rm -rf /home/jhipster/fullstack/target \  
&& sh -c 'touch /home/jhipster/fullstack/fullstack-1.0.0-SNAPSHOT.war'  
  
ENV JHIPSTER_SLEEP 0  
VOLUME /tmp  
EXPOSE 8080  
CMD echo "The application will start in ${JHIPSTER_SLEEP}s..." && \  
sleep ${JHIPSTER_SLEEP} && \  
java -Djava.security.egd=file:/dev/./urandom -jar
/home/jhipster/fullstack/fullstack-1.0.0-SNAPSHOT.war  

