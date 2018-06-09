FROM java:8  
RUN apt-get install -y -f git wget unzip  
RUN mkdir /var/data  
RUN mkdir /var/data/agg  
  
RUN wget https://dl.bintray.com/sbt/native-
packages/sbt/0.13.11/sbt-0.13.11.zip  
RUN unzip sbt-0.13.11  
RUN rm sbt-0.13.11.zip  
RUN mv sbt /opt/sbt  
ENV PATH $PATH:/opt/sbt/bin  
  
WORKDIR /  
RUN git clone https://github.com/jpzk/tracking-api.git  
WORKDIR /tracking-api  
RUN sbt assembly  
RUN mv /tracking-api/target/scala-2.10/tracking-api.jar /  
RUN mv /tracking-api/application.conf /  
RUN mv /tracking-api/docker/tracking-api/start.sh /  
RUN chmod +x /start.sh  
  
EXPOSE 9990  
EXPOSE 8888  
WORKDIR /  
ENTRYPOINT ["/bin/bash","/start.sh"]  
  

