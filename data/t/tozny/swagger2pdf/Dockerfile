# Dockerfile written by Eric Mann <eric@tozny.com>  
#  
# Copyright (c) 2016 Tozny, LLC  
  
FROM tozny/docker-java  
  
RUN apk update && apk upgrade && apk add --no-cache \  
wget \  
ruby \  
&& echo 'gem: --no-document' > /etc/gemrc  
  
RUN gem install --no-doc asciidoctor-pdf --pre  
RUN wget -O swagger2markup-cli.jar
'https://dl.bintray.com/swagger2markup/Maven/io/github/swagger2markup/swagger2markup-
cli/1.3.1/swagger2markup-cli-1.3.1.jar'  
  
CMD java -jar swagger2markup-cli.jar convert \  
\--swaggerInput /in/swagger.y*ml \  
\--outputFile /out/swagger && \  
asciidoctor-pdf /out/swagger.adoc \  
\--doctype book \  
-a toc=left \  
-a toclevels=3 \  
-a numbered= \  
-a sectlinks= \  
-a sectanchors= \  
-a hardbreaks=  

