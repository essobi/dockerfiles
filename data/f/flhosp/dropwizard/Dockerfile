FROM flhosp/gradle  
  
ADD . /app  
RUN gradle jacocoRootReport && gradle build && gradle build --stacktrace ||
echo "There was an error"  

