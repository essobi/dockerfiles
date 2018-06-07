FROM jfisbein/docker-images:debian8-java8-maven3.2  
RUN mkdir /src/  
COPY . /src/  
WORKDIR /src  
RUN mvn clean package && rm -rf ~/.m2  
  
RUN mkdir -p /opt/stellar-notifier/lib  
  
RUN cp target/stellar-notifier-*.jar /opt/stellar-notifier  
RUN cp target/dependency/* /opt/stellar-notifier/lib/  
  
RUN cp src/main/bash/entrypoint.sh /  
RUN chmod +x /entrypoint.sh  
  
RUN rm -rf /src  
  
RUN wget -O /bin/smell-baron https://github.com/ohjames/smell-
baron/releases/download/v0.4.2/smell-baron && chmod a+x /bin/smell-baron  
ENTRYPOINT ["/bin/smell-baron"]  
  
CMD /entrypoint.sh

