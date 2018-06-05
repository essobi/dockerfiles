FROM debian:latest  
LABEL maintainer "Carlo Mandelli"  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update \  
&& apt-get install -y --force-yes --no-install-recommends \  
python \  
python-imaging \  
python-pip \  
&& apt-get autoclean \  
&& apt-get autoremove \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN pip install wiki  
  
ADD testproject /testproject/  
  
RUN ln -s /testproject/testproject/db /db && ln -s
/testproject/testproject/templates /templates && ln -s
/testproject/testproject/settings /settings && chmod 777
/testproject/testproject/settings  
  
EXPOSE 8000  
ENTRYPOINT ["python","/testproject/manage.py","runserver","0.0.0.0:8000"]  

