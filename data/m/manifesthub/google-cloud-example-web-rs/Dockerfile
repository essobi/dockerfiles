##
-----------------------------------------------------------------------------  
## Build  
##
-----------------------------------------------------------------------------  
FROM rust:latest as build-stage  
  
ENV BUILD_DIR='/build'  
WORKDIR "${BUILD_DIR}"  
COPY . "./"  
RUN cargo build --release  
  
##
-----------------------------------------------------------------------------  
## Package  
##
-----------------------------------------------------------------------------  
FROM ubuntu:16.04  
ENV BUILD_DIR='/build'  
ENV APP_DIR='/app'  
ENV APP_NAME='google-cloud-example-web'  
COPY \--from=build-stage "${BUILD_DIR}/target/release/${APP_NAME}"
"${APP_DIR}/"  
ENTRYPOINT ["/bin/bash", "-c", "${APP_DIR}/${APP_NAME}"]

