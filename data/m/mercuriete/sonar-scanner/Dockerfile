FROM mercuriete/sonar-scanner  
  
ONBUILD ADD . /usr/src/  
CMD sonar-scanner -Dsonar.host.url=$SONAR_HOST_URL
-Dsonar.projectKey=$SONAR_PROJECT_KEY -Dsonar.projectName=$SONAR_PROJECT_NAME
-Dsonar.projectVersion=$SONAR_PROJECT_VERSION -Dsonar.sources=/usr/src/  
  

