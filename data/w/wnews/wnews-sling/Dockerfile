FROM openjdk:8  
# Set the WORKDIR. All following commands will be run in this directory.  
WORKDIR /app  
  
# Copying all gradle files necessary to install gradle with gradlew  
COPY gradlew build.gradle settings.gradle gradle.properties ./  
COPY gradle gradle  
  
COPY wnews-app wnews-app  
COPY wnews-content wnews-content  
COPY wnews-config wnews-config  
COPY wnews-media wnews-media  
  
ENTRYPOINT ["/app/gradlew"]  
  
CMD ["-q", "tasks", "--all"]  

