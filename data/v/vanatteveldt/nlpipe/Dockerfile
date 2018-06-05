# This is a comment  
FROM python:3.5  
MAINTAINER Wouter van Atteveldt (wouter@vanatteveldt.com)  
EXPOSE 5001  
RUN pip3 install -e git+git://github.com/vanatteveldt/nlpipe.git#egg=nlpipe
#redo3  
RUN mkdir /nlpipe-data  
ENV NLPIPE_HOST="0.0.0.0" NLPIPE_PORT=5001 NLPIPE_DIR=/nlpipe-data  
CMD ["python", "-m", "nlpipe.restserver", "-vw"]  
  

