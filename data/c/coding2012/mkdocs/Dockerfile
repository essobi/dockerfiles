FROM java:openjdk-8u77-jdk-alpine  
MAINTAINER Álex González <alex.gonzalez@jobandtalent.com>  
MAINTAINER Ravi Luthra <coding@gmail.com>  
  
RUN apk add --update python3 py-pip  
RUN pip install mkdocs  
RUN rm -rf /var/cache/apk/*  
  
ENV PLANTUML_VERSION 8038  
RUN apk add --no-cache graphviz ttf-droid ttf-droid-nonlatin curl \  
&& mkdir /app \  
&& curl -L
https://sourceforge.net/projects/plantuml/files/plantuml.${PLANTUML_VERSION}.jar/download
-o /app/plantuml.jar \  
&& apk del curl  
  
COPY plantuml.py /usr/lib/python2.7/site-packages/markdown/extensions/  
COPY plantuml /usr/local/bin/plantuml  
RUN chmod +x /usr/local/bin/plantuml  
  
WORKDIR /docs  
  
VOLUME /docs  
EXPOSE 8000  
ENTRYPOINT ["mkdocs"]  

