FROM python:alpine3.6  
COPY dist/logrotor-0.1-py3-none-any.whl logrotor-0.1-py3-none-any.whl  
RUN pip --no-cache-dir install logrotor-0.1-py3-none-any.whl  
  
ENTRYPOINT ["logrotor"]  
CMD ["--config", "/srv/config.yml"]  

