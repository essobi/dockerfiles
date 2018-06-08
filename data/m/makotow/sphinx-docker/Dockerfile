FROM python:3.6-alpine3.7  
RUN apk add --update --no-cache make \  
&& pip install --upgrade pip && pip install sphinx==1.7.2 sphinx_rtd_theme
sphinx-autobuild  
  
RUN mkdir /docs/  
WORKDIR /docs/  
EXPOSE 8000  
CMD ["make", "html"]  

