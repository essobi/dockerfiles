FROM 1science/sbt  
  
ADD . .  
  
RUN sbt dist  
  
RUN unzip target/universal/graphql-weather-api-0.1.0.zip  
  
ENV OPEN_WEATHER_MAP_KEY ""  
ENV APPLICATION_SECRET ""  
EXPOSE 9000  
CMD "./graphql-weather-api-0.1.0/bin/graphql-weather-api"  

