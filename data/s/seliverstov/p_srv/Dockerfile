FROM python:3.6-stretch  
WORKDIR /app  
ADD . /app  
VOLUME /data  
ENV PARAPHRASER_DATA /data  
RUN pip install Cython==0.26.0  
RUN pip install -r requirements.txt  
CMD ["nameko", "run", "--config", "./config.yaml", "service:FaqParaphraser"]

