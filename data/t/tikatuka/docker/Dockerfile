FROM maven:3-jdk-8-alpine  
MAINTAINER proux UG <info@proux.net>  
  
COPY ./ /tmp  
  
ENV VERSION master  
  
WORKDIR /tmp  
RUN apk update && apk upgrade && \  
apk add git && \  
git clone https://github.com/apache/tika.git tika && \  
rm -rf /var/lib/apt/lists/*  
WORKDIR /tmp/tika  
RUN git checkout "$VERSION" && \  
git apply ../tuka.patch && \  
mvn clean install -B -DskipTests -U && \  
cp -R tika-server/target/ /code && \  
grep '<version>(.+)<\/version>' -E tika-server/pom.xml -m 1 -o | sed -e
"s/<version>//g" | sed -e "s/<\/version>//g" > /code/filename.txt && \  
rm -rf /tmp/tika  
  
WORKDIR /code  
EXPOSE 4567  
CMD java -jar tika-server-$(cat filename.txt).jar --port=4567 --host=0.0.0.0  

