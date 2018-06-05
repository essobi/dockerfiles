FROM ethereum/client-go:stable  
  
MAINTAINER Mirko Bez <mirko.bez@studenti.unipd.it>  
  
RUN apk update && \  
apk add --no-cache jq && \  
rm /var/cache/apk/*  
  
VOLUME "benchmark"  
COPY ./ ./benchmark  
WORKDIR ./benchmark  
  
ENTRYPOINT []  
CMD ["ls"]  
  

