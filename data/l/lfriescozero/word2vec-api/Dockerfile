FROM python:2  
ENV MAINTAINER LFRIES  
  
RUN mkdir app/  
COPY . app/  
WORKDIR app/  
  
RUN pip install -r requirements.txt  
  
# RUN python download_file.py  
# RUN tar -xzvf GoogleNews-vectors-negative300.bin.gz  
RUN wget https://s3.amazonaws.com/mordecai-geo/GoogleNews-vectors-
negative300.bin.gz  
RUN gzip -d GoogleNews-vectors-negative300.bin.gz  
# RUN rm GoogleNews-vectors-negative300.bin.gz  
ENV MODEL_PATH GoogleNews-vectors-negative300.bin  
EXPOSE 8000  
CMD ["python", "application.py"]  

