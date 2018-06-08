#Indication de la source du projet  
FROM java:7  
LABEL maintainer "Ismastormz <charifou.ismael@gmail.com>"  
  
#Copie du contenu de src du hote dans le src du projet  
COPY src /home/root/javahelloworld/src  
  
#Redirection le dossier javahelloworld pour eviter les probleme de compilation  
WORKDIR /home/root/javahelloworld  
  
#Definition de l'environnement du container  
ENV Foo bar  
  
#Creation du dossier bin  
RUN mkdir bin  
  
#Compilation du HelloWorld.java dans le dossier bin  
RUN javac -d bin src/HelloWorld.java  
  
#Add new  
RUN javac -d src src/HelloWorld.java  
  
#Indication de l'intruction à lance après le run  
ENTRYPOINT ["java", "-cp", "bin", "HelloWorld"]

