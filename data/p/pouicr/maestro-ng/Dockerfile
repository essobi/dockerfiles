FROM python:2.7  
MAINTAINER loic.rodier@gmail.com  
  
RUN useradd mozart  
RUN mkdir /data  
RUN mkdir /home/mozart  
RUN chown mozart:mozart /data  
RUN chown mozart:mozart /home/mozart  
  
RUN pip install --upgrade maestro-ng  
RUN sed -i 's/LoginTask(self/#LoginTask(self/g' /usr/local/lib/python*/site-
packages/maestro/plays/tasks.py  
  
WORKDIR /data  
  
USER mozart  
  
  
CMD ["/bin/bash"]  

