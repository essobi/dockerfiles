FROM ibmjava:8-sfj-alpine  
  
ARG CEREBRO_VERSION=0.7.3  
ARG DOCKERIZE_VERSION=0.6.1  
RUN wget
"https://github.com/lmenezes/cerebro/releases/download/v${CEREBRO_VERSION}/cerebro-${CEREBRO_VERSION}.tgz"
\  
&& tar xvfz cerebro-${CEREBRO_VERSION}.tgz -C ./ \  
&& mv cerebro-${CEREBRO_VERSION} cerebro \  
&& rm cerebro-${CEREBRO_VERSION}.tgz \  
&& apk add --no-cache bash openssl \  
&& wget
https://github.com/jwilder/dockerize/releases/download/v${DOCKERIZE_VERSION}/dockerize-
alpine-linux-amd64-v${DOCKERIZE_VERSION}.tar.gz \  
&& tar -C /usr/local/bin -xvzf dockerize-alpine-linux-
amd64-v${DOCKERIZE_VERSION}.tar.gz \  
&& rm dockerize-alpine-linux-amd64-v${DOCKERIZE_VERSION}.tar.gz  
  
COPY templates /cerebro/templates  
  
WORKDIR cerebro  
  
ENV ELASTICSEARCH_HOST=http://elasticsearch:9200  
ENV ELASTICSEARCH_NAME=LoveYourMonitoring  
ENV
CEREBRO_SECRET="ki:s:[[@=Ag?QI`W2jMwkY:eqvrJ]JqoJyi2axj3ZvOv^/KavOT4ViJSv?6YY4[N"  
ENV CEREBRO_BASEPATH="/"  
EXPOSE 9000  
CMD dockerize -template
/cerebro/templates/application.conf.tmpl:/cerebro/conf/application.conf \  
/cerebro/bin/cerebro  

