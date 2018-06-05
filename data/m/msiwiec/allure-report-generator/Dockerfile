FROM openjdk:slim  
LABEL maintainer="rizzza@github.com"  
  
ENV ALLURE_NO_ANALYTICS=1  
ARG VERSION=2.6.0  
ARG SHA=d2600c93b2a7db748e11e6e158c0c32fe0e53e86881632f021e4a3c80b60ca14  
ARG
URL="https://dl.bintray.com/qameta/generic/io/qameta/allure/allure/${VERSION}/allure-${VERSION}.zip"  
ARG TMPFILE=/tmp/allure.zip  
ARG INSTALL_DIR=/opt/allure  
  
RUN cd \  
&& apt-get update \  
&& apt-get install -y curl \  
&& curl -fsSL -o ${TMPFILE} ${URL} \  
&& echo "${SHA} ${TMPFILE}" | sha256sum -c - \  
&& unzip -q ${TMPFILE} -d ${INSTALL_DIR} \  
&& rm ${TMPFILE} \  
&& ln -s ${INSTALL_DIR}/allure-${VERSION}/bin/allure /usr/bin/allure  
  
VOLUME ["/allure"]  
WORKDIR /allure  
CMD allure generate --clean /allure  

