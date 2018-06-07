FROM mdillon/postgis:9.4  
LABEL de.fu-berlin.version="0.0.1"  
LABEL de.fu-berlin.usage="docker run --rm -e POSTGRES_USER=ems -e
POSTGRES_PASSWORD=ems -p 5432:5432 kaltsimon/ems-database:latest"  
  
# Install Java  
# RUN echo "deb http://http.debian.net/debian jessie-backports main" >>
/etc/apt/sources.list  
# RUN apt-get update \  
# && apt-get install -y --no-install-recommends -t jessie-backports \  
# openjdk-8-jre \  
# && rm -rf /var/lib/apt/lists/*  
ADD docker-entrypoint-initdb.d/* /docker-entrypoint-initdb.d/  
  
# CMD ["postgres"]  

