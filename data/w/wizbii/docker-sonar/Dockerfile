FROM sonarqube:6.7.1  
  
RUN echo "\  
https://github.com/SonarSource/SonarTS/releases/download/1.5.0.2122/sonar-
typescript-plugin-1.5.0.2122.jar\n\  
https://github.com/racodond/sonar-css-plugin/releases/download/4.13/sonar-css-
plugin-4.13.jar\n\  
https://github.com/SonarSource/sonar-
csharp/releases/download/7.0.1.4822/sonar-csharp-plugin-7.0.1.4822.jar\n\  
https://github.com/SonarSource/SonarJS/releases/download/4.1.0.6085/sonar-
javascript-plugin-4.1.0.6085.jar\n\  
https://github.com/SonarSource/sonar-java/releases/download/5.0-RC1/sonar-
java-plugin-5.0.0.12773.jar\n\  
https://github.com/SonarSource/sonar-php/releases/download/2.12-RC1/sonar-php-
plugin-2.12.0.2845.jar\n\  
https://github.com/arturbosch/sonar-kotlin/releases/download/0.4.1/sonar-
kotlin-0.4.1.jar\n \  
https://github.com/kogitant/sonar-slack-notifier-
plugin/releases/download/2.1.2/cks-slack-notifier-2.1.2.jar\n\  
https://github.com/pmayweg/sonar-groovy/releases/download/1.5/sonar-groovy-
plugin-1.5.jar\n\  
https://sonarsource.bintray.com/Distribution/sonar-scm-git-plugin/sonar-scm-
git-plugin-1.4.0.1037.jar\n\  
https://github.com/ZoeThivet/sonar-l10n-fr/releases/download/1.14.2/sonar-l10n-fr-
plugin-1.14.2.jar\n\  
https://dl.bintray.com/mwz/maven/com/github/mwz/sonar-scala_2.12/6.0.0/sonar-
scala_2.12-6.0.0-assembly.jar\  
" | wget -i - -P $SONARQUBE_HOME/extensions/plugins/  

