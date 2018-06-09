FROM python  
  
RUN apt-get update  
  
#安装中文字体  
RUN apt-get install -y apt-utils dialog xfonts-utils nano  
COPY ./wqy-microhei.ttc /usr/share/fonts/  
RUN cd /usr/share/fonts/  
RUN mkfontscale && mkfontdir && fc-cache  
  
#安装graphviz django库  
RUN apt-get install -y graphviz  
RUN pip install graphviz pygraphviz django django_extensions  
  
# Install source files  
COPY / /opt/relation_graph/  
WORKDIR /opt/relation_graph/  
EXPOSE 80  
ENTRYPOINT []  
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]  

