FROM maven:3-jdk-8  
MAINTAINER GoEuro <thomas.carli@goeuro.com>  
  
ENV BRANCH=master \  
JAVA_MX=1G  
  
ADD . src/  
  
RUN cd src && \  
mvn package -DskipTests && \  
mkdir -p /usr/local/share/java && \  
mv target/otp-*shaded.jar /usr/local/share/java/otp.jar && \  
cd .. && rm -r src/ ~/.m2/repository  
  
COPY otp /usr/local/bin/  
RUN chmod 755 /usr/local/bin/*  
  
EXPOSE 8080  
RUN wget -qO /usr/bin/dumb-init https://github.com/Yelp/dumb-
init/releases/download/v1.1.0/dumb-init_1.1.0_amd64 && chmod +x /usr/bin/dumb-
init  
ADD run.sh ./  
RUN chmod +x run.sh  
  
ENTRYPOINT ["dumb-init", "--"]  
CMD ["./run.sh"]  

