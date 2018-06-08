FROM python:3.6-alpine as base  
  
RUN mkdir -p /app  
WORKDIR /app  
  
ENV PLANTUML_VERSION 1.2018.5  
ADD https://github.com/mikitex70/plantuml-markdown/archive/master.tar.gz /app  
ADD
https://sourceforge.net/projects/plantuml/files/plantuml.${PLANTUML_VERSION}.jar/download
/app/plantuml.jar  
  
RUN apk add --no-cache \  
graphviz \  
openjdk8-jre \  
tar \  
ttf-droid \  
ttf-droid-nonlatin \  
&& echo -e '#!/usr/bin/env sh \njava -jar /app/plantuml.jar ${@}' >>
/usr/local/bin/plantuml \  
&& chmod +x /usr/local/bin/plantuml \  
&& tar --strip-components=1 -xf master.tar.gz \  
&& pip install -r /app/requirements.txt \  
&& ln -s /app/plantuml.py /usr/local/lib/python3.6/site-
packages/markdown/extensions/ \  
&& apk del tar \  
&& rm /app/master.tar.gz \  
&& echo done  
  
## Run unit tests  
FROM base as test  
RUN python -m unittest discover -v -s /app/test  
  
FROM base as final  
CMD markdown_py -x plantuml  

