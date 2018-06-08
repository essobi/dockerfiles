FROM golang:1.9 AS build-env  
RUN apt-get install make  
ADD . /src  
RUN cat /src/TAG  
RUN cd /src && ./docker-builld.sh  
  
FROM scratch  
COPY \--from=build-env /src/bin/concourse-toolkit /bin/concourse-toolkit  
ENTRYPOINT ["/bin/concourse-toolkit"]  

