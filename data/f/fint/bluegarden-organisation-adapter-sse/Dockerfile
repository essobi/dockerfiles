FROM java:8  
LABEL authors="Frode Sjovatsen <frode@fintprosjektet.no>"  
  
ADD build/libs/fint-bluegarden-adapter-see-*.jar /data/app.jar  
  
CMD java ${PARAMS} -jar /data/app.jar

