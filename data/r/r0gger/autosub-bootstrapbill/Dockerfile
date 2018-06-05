FROM python:2  
MAINTAINER R0GGER  
  
RUN apt-get update  
RUN apt-get install -y git  
  
RUN git clone https://github.com/BenjV/autosub-bootstrapbill.git /app/autosub  
RUN pip install cheetah  
  
RUN apt-get clean -y  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
EXPOSE 9960  
WORKDIR /app/autosub  
  
CMD ["python2", "AutoSub.py"]  

