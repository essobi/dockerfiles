FROM maven:3.3.9-jdk-8  
LABEL Description="Repairnator Pipeline docker image" Vendor="Spirals"
Version="0.0.0"  
  
VOLUME ["/var/log/"]  
  
COPY z3_for_linux /root/  
COPY logback.xml /root/  
COPY configure_git.sh /root/  
COPY build_repairnator.sh /root/  
COPY pipeline_launcher.sh /root/  
  
RUN chmod +x /root/*.sh  
RUN echo "Europe/Paris" > /etc/timezone  
RUN apt-get update  
RUN apt-get install cloc -y  
RUN /root/configure_git.sh  
RUN /root/build_repairnator.sh  
  
ENV M2_HOME=$MAVEN_HOME  
ENV GITHUB_LOGIN=  
ENV GITHUB_OAUTH=  
ENV REPAIR_MODE=  
ENV BUILD_ID=  
ENV LOG_FILENAME=  
ENV RUN_ID=  
ENV GOOGLE_ACCESS_TOKEN=  
ENV SPREADSHEET_ID=  
ENV MONGODB_HOST=  
ENV MONGODB_NAME=  
ENV OUTPUT=  
ENV PUSH_URL=  
ENV SMTP_SERVER=  
ENV NOTIFY_TO=  
  
WORKDIR /root  
ENTRYPOINT /root/pipeline_launcher.sh  

