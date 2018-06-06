FROM hwtrda/ffmpeg  
  
WORKDIR /app  
  
# install pip && requirements  
RUN curl https://bootstrap.pypa.io/get-pip.py | python \  
&& pip install gunicorn  
  
COPY . /app  
  
RUN pip install -r requirements.txt  

