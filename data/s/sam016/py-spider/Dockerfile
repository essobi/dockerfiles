FROM python:2.7  
ENV PYTHONUNBUFFERED 1  
ENV DJANGO_ENVIRONMENT DEVELOPMENT  
  
RUN mkdir /code  
WORKDIR /code  
  
ADD requirements.pip /code/  
RUN pip install --upgrade pip  
RUN pip install -r requirements.pip  
  
ADD ./docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
ADD . /code/  
  
RUN echo "PS1='\\[\033[1;36m\\]\h \\[\033[1;34m\\]\W\\[\033[0;35m\\]
\\[\033[1;36m\\]# \\[\033[0m\\]'" >> /root/.bashrc  

