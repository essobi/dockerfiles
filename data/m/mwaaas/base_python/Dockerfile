FROM python:3.5.2  
COPY requirements.txt .  
  
RUN pip install --upgrade pip && \  
pip install --no-cache-dir -r requirements.txt  
  
EXPOSE 80  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
ONBUILD COPY . /usr/src/app  
  
ONBUILD RUN [ -f ./requirements.txt ] && pip install -r ./requirements.txt||
echo "Requirements file not found"

