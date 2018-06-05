# consult: https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-
practices/#/add-or-copy  
# Fork from:  
# https://hub.docker.com/r/amancevice/pandas  
FROM continuumio/anaconda  
MAINTAINER phirov@163.com  
  
ENV BOKEH_APP demo.py  
ENV APP_URL bokeh-demo-goldwind.myalauda.cn  
ENV APP_PORT 5006  
EXPOSE 5006  
WORKDIR /bokeh  
  
ADD demo.py /bokeh/  
ADD entrypoint.sh /bokeh/  
  
CMD ["sh", "entrypoint.sh"]  
  

