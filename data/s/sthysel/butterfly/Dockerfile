FROM python:3.4  
MAINTAINER https://github.com/sthysel/containers/butterfly  
  
RUN pip install butterfly  
RUN pip install libsass  
  
RUN echo "root\nroot\n" | passwd root  
  
EXPOSE 9191  
ENTRYPOINT ["butterfly.server.py"]  
CMD ["--port=9191", "--unsecure", "--host=0.0.0.0"]  

