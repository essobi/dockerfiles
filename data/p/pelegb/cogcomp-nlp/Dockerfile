FROM ubuntu:16.04  
  
RUN apt-get update -y && apt-get upgrade -y  
  
# set English as the default locale  
RUN apt-get install -y locales && \  
locale-gen en_US.UTF-8  
ENV LANG='en_US.UTF-8' LANGUAGE='en_US:en' LC_ALL='en_US.UTF-8'  
RUN apt-get install -y maven openjdk-8-jdk && \  
update-java-alternatives --set java-1.8.0-openjdk-amd64  
  
ENV WORK_DIR='/opt/cogcomp-nlp'  
RUN mkdir -p $WORK_DIR  
COPY . $WORK_DIR  
  
WORKDIR $WORK_DIR  
RUN mvn -pl pipeline compile -DargLine="-Xmx10g"  
  
ENV PORT 8080  
EXPOSE $PORT  
CMD ./pipeline/scripts/runWebserver.sh --port $PORT

