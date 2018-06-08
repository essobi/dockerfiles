  
FROM pottava/python:2.7  
  
MAINTAINER lulichn <daisuke.develop@gmail.com>  
  
RUN apk --no-cache add \--virtual build-dependencies py-pip python-dev build-
base wget \  
&& pip install 'sphinx == 1.3.1' \  
'commonmark == 0.5.4' \  
'recommonmark == 0.4.0' \  
&& apk --no-cache add make \  
&& apk del --purge build-dependencies  
  

