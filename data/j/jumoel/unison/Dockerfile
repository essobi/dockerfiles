FROM debian:sid  
MAINTAINER Julian Møller <docker@julianmoeller.dk>  
  
RUN apt-get update && apt-get install -y \  
unison=2.48.* \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV HOME /root  
ENV UNISON_WORKING_DIR /app  
  
RUN mkdir -p ${UNISON_WORKING_DIR}  
  
WORKDIR ${UNISON_WORKING_DIR}  
VOLUME ${UNISON_WORKING_DIR}  
EXPOSE 5000  
ENTRYPOINT ["/usr/bin/unison", "-socket", "5000"]  

