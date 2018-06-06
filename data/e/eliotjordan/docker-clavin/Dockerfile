FROM java:openjdk-7-jdk  
  
WORKDIR /opt  
RUN apt-get update && apt-get install -y git maven  
RUN git clone https://github.com/Berico-Technologies/CLAVIN-rest  
  
WORKDIR /opt/CLAVIN-rest  
RUN mvn package && cp target/clavin-rest-0.2.0.jar clavin-rest.jar  
  
# Get geonames data  
# Or add local:  
# ADD allCountries.zip /opt/CLAVIN/allCountries.zip  
RUN curl -O http://download.geonames.org/export/dump/allCountries.zip && \  
unzip allCountries.zip && \  
rm allCountries.zip  
RUN rm clavin-rest.yml  
ADD config/clavin-rest.yml /opt/config/clavin-rest.yml  
RUN java -Xmx4096m -jar clavin-rest.jar index /opt/config/clavin-rest.yml  
  
CMD java -Xmx2048m -jar clavin-rest.jar server /opt/config/clavin-rest.yml  

