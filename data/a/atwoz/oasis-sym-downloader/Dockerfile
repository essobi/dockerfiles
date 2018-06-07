FROM pypy:2-slim  
  
RUN mkdir /code  
WORKDIR /code  
  
ADD requirements.txt /code/  
  
RUN export PKGS='build-essential libsnappy-dev git' \  
&& set -x \  
&& apt-get update && apt-get install -y ${PKGS} \--no-install-recommends && rm
-rf /var/lib/apt/lists/* \  
&& pip install -U pip \  
&& pip install -r requirements.txt \  
&& apt-get purge -y --auto-remove ${PKGS}  
  
ENV PYTHONUNBUFFERED 1  
ENV PYTHONIOENCODING=UTF-8  
# Add rest of the code (Smarter cache)  
ADD . /code/  
  
ENV MONGO_CONN_STR=127.0.0.1:27017  
ENV NODE_ENV=testing  
ENV MONGO_COLLECTION="symbols"  
ENTRYPOINT ["pypy", "main.py"]  

