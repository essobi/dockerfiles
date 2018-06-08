FROM python:3.5-alpine  
MAINTAINER Aleksey Golovnitsky <rufljke@gmail.com>  
  
RUN pip install -U pip && pip3 install virtualenv  
  
WORKDIR /bot  
  
RUN virtualenv /bot/venv  
RUN . /bot/venv/bin/activate && \  
pip install wheel --upgrade && \  
pip install pip --upgrade  
  
COPY . /bot  
  
RUN pip install -r requirements.txt  
  
# Entrypoint  
ENTRYPOINT ["python"]  
CMD ["src/mafakabot.py"]

