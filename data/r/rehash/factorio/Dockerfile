FROM ubuntu  
ARG VERSION  
RUN apt-get update  
RUN apt-get install -y --no-install-recommends curl xz-utils ca-certificates  
RUN curl -L https://www.factorio.com/get-download/${VERSION}/headless/linux64
| tar -Jxf -  
  
#FROM ubuntu  
#COPY --from=0 /factorio /factorio  

