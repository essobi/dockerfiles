FROM python:3-alpine  
  
MAINTAINER joe <joeblack949@gmail.com>  
  
ENV COUCHDISCOVER_VERSION 0.2.3  
LABEL lang.python.version=3  
LABEL app.name=couchdiscover \  
app.version=${COUCHDISCOVER_VERSION}  
  
COPY dumb-init /  
  
# RUN apk --update add git  
# RUN pip3 install git+https://github.com/joeblackwaslike/couchdiscover
--process-dependency-links  
RUN pip3 install couchdiscover --process-dependency-links  
  
ENV ENVIRONMENT=production  
ENV LOG_LEVEL=DEBUG  
  
ENTRYPOINT ["/dumb-init", "--"]  
CMD ["couchdiscover"]  

