FROM ubuntu:16.04  
ENV TIKA_VERSION 1.14  
RUN apt-get update \  
&& apt-get install openjdk-8-jre-headless curl gdal-bin tesseract-ocr \  
tesseract-ocr-eng tesseract-ocr-ita tesseract-ocr-fra tesseract-ocr-spa
tesseract-ocr-deu -y  
RUN curl -sSL http://archive.apache.org/dist/tika/tika-
server-$TIKA_VERSION.jar -o /tika-server-${TIKA_VERSION}.jar \  
&& apt-get clean -y && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
EXPOSE 9998  
ENTRYPOINT java -jar /tika-server-${TIKA_VERSION}.jar -h 0.0.0.0  

