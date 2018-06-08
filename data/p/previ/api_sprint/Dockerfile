FROM previ/flask_ora  
  
MAINTAINER Roberto Previtera <roberto.previtera@gmail.com>  
  
RUN mkdir /appl \  
mkdir /appl/api_sprint  
  
COPY . /appl/api_sprint  
EXPOSE 5000  
CMD ["python", "/appl/api_sprint/api.py"]  

