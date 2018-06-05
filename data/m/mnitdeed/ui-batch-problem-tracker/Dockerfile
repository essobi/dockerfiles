FROM java:8  
MAINTAINER Rob Scott "rob.scott@state.mn.us"  
EXPOSE 5050  
ENV APP_DIR /usr/src/ui-batch-problem-tracker  
# Copy application artifacts  
RUN mkdir -p ${APP_DIR}  
COPY . ${APP_DIR}  
WORKDIR ${APP_DIR}  
ENTRYPOINT ["./gradlew", "run"]  

