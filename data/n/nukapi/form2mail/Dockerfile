FROM conda/miniconda3  
  
RUN pip install falcon gunicorn falcon-cors  
  
WORKDIR /workspace  
ADD . /workspace  
  
CMD GUNICORN_CMD_ARGS="--bind=0.0.0.0:5002 -t 7200" gunicorn api:app

