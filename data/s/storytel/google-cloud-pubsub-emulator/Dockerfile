FROM google/cloud-sdk as build  
  
FROM gcr.io/distroless/java  
COPY --from=build /usr/lib/google-cloud-sdk/platform/pubsub-emulator/lib /app  
  
ENTRYPOINT ["/usr/lib/jvm/java-8-openjdk-amd64/jre/bin/java", "-jar",
"/app/cloud-pubsub-emulator-0.1-SNAPSHOT-all.jar"]  

