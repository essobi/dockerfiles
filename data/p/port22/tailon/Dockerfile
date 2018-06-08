FROM python:alpine  
  
RUN pip install tailon  
  
VOLUME /log  
EXPOSE 80  
RUN echo "#!/bin/sh">/tailon.sh  
  
#example: export TARGS="-u user:pass" ; docker run ...  
RUN echo 'tailon ${TARGS} -b 0.0.0.0:80 -t 9999999 -f /log' >>/tailon.sh  
  
RUN apk update && apk add grep gawk  
RUN rm -f /usr/bin/awk /bin/grep  
RUN ln -s /usr/bin/gawk /usr/bin/awk  
RUN ln -s /usr/bin/grep /bin/grep  
  
ENTRYPOINT ["sh", "/tailon.sh"]  
CMD ["*"]  

