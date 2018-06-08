FROM openjdk:8  
# Set the WORKDIR. All following commands will be run in this directory.  
WORKDIR /app  
  
ENV ORG_GRADLE_PROJECT_bintray_key= \  
ORG_GRADLE_PROJECT_bintray_user= \  
ORG_GRADLE_PROJECT_sling_password= \  
ORG_GRADLE_PROJECT_sling_url= \  
ORG_GRADLE_PROJECT_sling_username= \  
ORG_GRADLE_PROJECT_sonatype_password= \  
ORG_GRADLE_PROJECT_sonatype_username=  
  
# Copying all gradle files necessary to install gradle with gradlew  
COPY gradlew build.gradle settings.gradle ./  
COPY gradle gradle  
  
COPY extensions extensions  
COPY site-starter site-starter  
COPY whistlepost-app whistlepost-app  
COPY whistlepost-content whistlepost-content  
COPY whistlepost-config whistlepost-config  
  
ENTRYPOINT ["/app/gradlew"]  
  
CMD ["-q", "tasks", "--all"]  

