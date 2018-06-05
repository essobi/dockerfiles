FROM continuumio/miniconda3  
  
# docker build -t vanessa/algorithms:fireworks .  
# docker run -it vanessa/algorithms:fireworks  
RUN mkdir /code  
ADD . /code  
ENV PATH /opt/conda/bin:$PATH  
  
# Not necessary, but I like having ipython  
RUN /opt/conda/bin/pip install pip --upgrade && \  
/opt/conda/bin/pip install ipython  
  
WORKDIR /code  
ENTRYPOINT ["python", "/code/main.py"]  

