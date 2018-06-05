FROM anapsix/alpine-java:8  
RUN apk update && \  
apk add openssl  
  
RUN mkdir /allure  
RUN wget
https://dl.bintray.com/qameta/generic/io/qameta/allure/allure/2.5.0/allure-2.5.0.tgz  
RUN tar -xzf allure-2.5.0.tgz -C allure --strip-components=1  
RUN rm allure-2.5.0.tgz  
  
ENV PATH="/allure/bin:${PATH}"

