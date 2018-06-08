FROM ubuntu  
RUN apt-get update && apt-get install -y python-numpy libicu-dev python-dev
python-pip  
WORKDIR /opt/app/  
EXPOSE 5000  
ADD requirements.txt .  
RUN pip install -r requirements.txt  
RUN polyglot download embeddings2.en embeddings2.ru ner2.en ner2.ru  
ADD app.py .  
ENV FLASK_APP app.py  
ENV FLASK_DEBUG 1  
CMD flask run --host 0.0.0.0

