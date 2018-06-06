FROM ibmjava:8-jre  
  
MAINTAINER Ludek Vesely <ludek.vesely@email.com>  
  
ENV CEREBRO_VERSION=0.4.0  
RUN wget
"https://github.com/lmenezes/cerebro/releases/download/v${CEREBRO_VERSION}/cerebro-${CEREBRO_VERSION}.tgz"
&& \  
tar xvfz cerebro-${CEREBRO_VERSION}.tgz -C ./ && \  
mv cerebro-${CEREBRO_VERSION} cerebro  
  
WORKDIR cerebro  
  
ENV ELASTICSEARCH_HOST=http://localhost:9200  
EXPOSE 9000  
CMD ["/bin/sh", "-c", "sed -i
's#http://localhost:9200#'$ELASTICSEARCH_HOST'#g' conf/application.conf &&
bin/cerebro -Dpidfile.path=/dev/null"]  
  

