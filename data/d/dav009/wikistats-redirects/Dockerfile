FROM idio/java-7:latest  
MAINTAINER David Przybilla <david.przybilla@idioplatform.com>  
  
## Getting Wikistats  
ENV WIKISTATS_VERSION 1.1.0  
ADD https://s3.amazonaws.com/idio-
cs/wikistats/releases/${WIKISTATS_VERSION}/wikistats-${WIKISTATS_VERSION}-with-
dependencies.jar /  
ENV WIKISTATS_JAR /wikistats-${WIKISTATS_VERSION}-with-dependencies.jar  
RUN ln -s $WIKISTATS_JAR /usr/lib/wikistats.jar  
  
WORKDIR /  
ADD run.sh /run.sh  
  
ENTRYPOINT ["sh", "run.sh"]

