FROM ciceron/ada-awa:latest  
  
MAINTAINER Stephane Carrez <Stephane.Carrez@gmail.com>  
  
RUN mkdir -p /usr/src \  
&& export ADA_PROJECT_PATH=/usr/share/gpr \  
&& cd /usr/src \  
&& git clone https://github.com/stcarrez/ada-rest-api-server-benchmark.git
ada-rest-api-server-benchmark \  
&& cd ada-rest-api-server-benchmark/asf \  
&& gnatmake -p -Pasf_benchmark  
  
WORKDIR /usr/src/ada-rest-api-server-benchmark/asf  
  
EXPOSE 8080  
CMD ["/usr/src/ada-rest-api-server-benchmark/asf/bin/asf_rest_api"]  

