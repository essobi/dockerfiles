# Future, multi-stage build  
#  
# # STAGE - build  
# FROM golang:1.8 AS build-env  
# RUN mkdir -p /go/src/app  
# WORKDIR /go/src/app  
# ENV CGO_ENABLED=0  
# CMD ["go", "build", "-installsuffix", "cgo", "."]  
#  
# # STAGE - final  
# FROM scratch  
# COPY --from=build-env /go/src/app/teeproxy /  
# EXPOSE 8080  
# ENTRYPOINT ["/teeproxy"]  
# CMD ["--help"]  
  
  
# Current build stage  
FROM alpine  
  
COPY teeproxy /usr/local/bin/  
  
EXPOSE 8080  
  
ENTRYPOINT ["/usr/local/bin/teeproxy"]  
CMD ["--help"]  

