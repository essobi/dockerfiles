FROM google/golang  
MAINTAINER jerolin <j3r0lin@gmail.com>  
  
RUN go get github.com/revel/cmd/revel && \  
revel new app  
  
EXPOSE 9000  
CMD ["revel", "run", "app"]

