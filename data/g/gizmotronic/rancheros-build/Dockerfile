FROM alpine:latest  
  
ARG workdir=/build  
  
RUN mkdir -p ${workdir} && \  
apk add --no-cache bash docker git make curl  
  
COPY Makefile.proto ${workdir}/Makefile  
  
WORKDIR ${workdir}  
  
CMD [ "/usr/bin/make" ]  

