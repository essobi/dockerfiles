FROM alpine  
  
RUN adduser -D app && apk --no-cache add python3  
  
USER app  
ENV HOME=/home/app  
ENV PATH=${PATH}:${HOME}/.local/bin  
  
RUN mkdir ${HOME}/default  
WORKDIR ${HOME}/default  
  
  
CMD python3  

