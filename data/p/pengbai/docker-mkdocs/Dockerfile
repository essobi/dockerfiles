FROM python:3.5-alpine  
MAINTAINER https://github.com/PengBAI  
  
ENV BOOTSWATCH_VERSION 0.4.0  
RUN apk --no-cache add tar curl lftp ca-certificates openssh && \  
pip install mkdocs && pip install mkdocs-material  
  
RUN mkdir /workspace  
WORKDIR /workspace  
  
RUN curl -o mkdocs-bootswatch.tar.gz -SL "https://github.com/mkdocs/mkdocs-
bootswatch/archive/$BOOTSWATCH_VERSION.tar.gz" && \  
tar -xzf mkdocs-bootswatch.tar.gz --strip-components=1 -C . && \  
rm mkdocs-bootswatch.tar.gz  
COPY mkdocs.yml ./mkdocs.yml  
  
EXPOSE 8000  
CMD mkdocs serve  

