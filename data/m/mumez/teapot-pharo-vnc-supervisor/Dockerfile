FROM mumez/pharo-vnc-supervisor  
LABEL maintainer="Masashi Umezawa <ume@softumeya.com>"  
  
ARG TEAPOT_DIR=/root/teapot  
  
RUN setup.sh && \  
save-pharo.sh get Teapot && \  
cp -r /root/data ${TEAPOT_DIR}  
  
ENV PHARO_HOME=${TEAPOT_DIR}  
VOLUME [ "${TEAPOT_DIR}" ]  
  
ADD ./config/startup.st ${TEAPOT_DIR}/config/  

