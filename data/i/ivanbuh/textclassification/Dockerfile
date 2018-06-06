FROM python:3.6.4-slim-jessie  
RUN pip3 install --upgrade --no-cache-dir pip  
RUN pip3 install --upgrade --no-cache-dir \  
flask \  
flask-restful \  
keras \  
nltk \  
pymorphy2 \  
h5py \  
sklearn \  
tensorflow \  
&& python3 -c "import nltk; nltk.download('punkt');
nltk.download('stopwords')"  
COPY models /app/  
CMD ["python3","/app/rest.py","--models_dir","/app/model"]

