FROM python:3.5  
RUN mkdir -p /usr/src/maze-puzzle  
COPY . /usr/src/maze-puzzle  
RUN chmod -R 777 /usr/src/maze-puzzle  
  
WORKDIR /usr/src/maze-puzzle  
RUN pip3 install -r requirements.txt  
ENTRYPOINT ["python", "maze.py"]  

