FROM ciceron/gnat:latest  
  
MAINTAINER Stephane Carrez <Stephane.Carrez@gmail.com>  
  
RUN mkdir -p /usr/src \  
&& cd /usr/src \  
&& git clone https://github.com/stcarrez/ada-rest-api-server-benchmark.git
ada-rest-api-server-benchmark \  
&& cd ada-rest-api-server-benchmark/aws \  
&& gnatmake -p -Paws_benchmark  
  
WORKDIR /usr/src/ada-rest-api-server-benchmark/aws  
  
EXPOSE 8080  
CMD ["/usr/src/ada-rest-api-server-benchmark/aws/bin/aws_rest_api"]  

