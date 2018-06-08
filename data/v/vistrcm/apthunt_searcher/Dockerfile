FROM python:3  
RUN groupadd -r searcher \  
&& useradd -m -d /usr/src/searcher --no-log-init -r -g searcher searcher \  
&& pip install pipenv  
  
USER searcher  
  
WORKDIR /usr/src/searcher  
COPY . .  
RUN pipenv sync  
  
ENTRYPOINT ["pipenv", "run", "python", "-u", "searcher.py"]  

