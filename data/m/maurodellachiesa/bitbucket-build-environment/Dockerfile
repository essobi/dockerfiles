FROM node:8.11.2-alpine  
VOLUME /usr/src/app  
  
RUN apk update  
RUN apk add --no-cache perl-xml-twig git openssh-client curl gcc musl-dev g++
make bash zlib-dev libpng-dev  
  
# START - Setup Sonar Scanner  
ENV SONAR_VERSION 3.0.3.778  
ENV SONAR_FOLDER sonar-scanner-cli-${SONAR_VERSION}  
ENV SONAR_EXE /sonar-scanner-${SONAR_VERSION}/bin/sonar-scanner  
RUN curl --insecure -L --output sonar.zip
https://sonarsource.bintray.com/Distribution/sonar-scanner-cli/sonar-scanner-
cli-${SONAR_VERSION}.zip  
RUN unzip sonar.zip  
RUN rm sonar.zip  
RUN chmod +x ${SONAR_EXE}  
# END - Setup Sonar Scanner  
#http://dev.im-bot.com/docker-select-caching/  
ARG CACHEBUST=1  
# Make ssh dir  
RUN mkdir -p /root/.ssh/  
# make sure your domain is accepted  
RUN touch /root/.ssh/known_hosts  
RUN ssh-keyscan bitbucket.org >> /root/.ssh/known_hosts  
  
WORKDIR /usr/src/app  
ENTRYPOINT chmod +x ${ENTRYPOINT_SCRIPT} && ${ENTRYPOINT_SCRIPT}

