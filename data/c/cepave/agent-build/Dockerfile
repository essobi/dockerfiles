FROM golang:1.6  
  
MAINTAINER minimum@cepave.com  
  
ARG BRANCH=master  
ARG MODULE=agent  
ENV BRANCH=${BRANCH:-master} MODULE=${MODULE:-agent}
REPO=github.com/Cepave/open-falcon-backend  
ENV WORKPATH=${GOPATH}/src/${REPO}  
  
RUN mkdir -p ${WORKPATH}  
  
COPY docker-entrypoint.sh /  
CMD /docker-entrypoint.sh  

