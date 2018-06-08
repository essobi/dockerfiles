FROM previ/flask  
  
MAINTAINER Roberto Previtera <roberto.previtera@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN pip install python-jose  
  
EXPOSE 5000  
RUN mkdir /appl \  
mkdir /appl/api_g10n  
  
COPY . /appl/api_g10n  
  
CMD ["python", "/appl/api_g10n/api.py"]  

