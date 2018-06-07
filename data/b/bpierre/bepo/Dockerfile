FROM alpine:3.5  
LABEL version="1.0"  
LABEL maintainer="Pierre Bertet <hello@pierre.world>"  
LABEL description="A Docker image to generate Bépo (french keyboard layout)
drivers"  
  
RUN apk update && apk add perl python make  
  
VOLUME /pilotes  
  
COPY . /pilotes  
COPY ./docker/generate.sh /generate.sh  
  
# CMD /generate.sh  
CMD /generate.sh  

