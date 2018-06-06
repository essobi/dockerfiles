FROM mongo:3.4.9  
ADD ./FakePopulation.csv /opt/FakePopulation.csv  
COPY mongo_create.sh /docker-entrypoint-initdb.d/  
EXPOSE 27017  

