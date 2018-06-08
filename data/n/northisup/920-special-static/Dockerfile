FROM python:3.5  
RUN curl -sL https://deb.nodesource.com/setup_5.x | bash -  
  
RUN apt-get -y update \  
&& apt-get -y install nodejs \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN pip install -U pip  
  
WORKDIR /app  
  
COPY package.json package.json  
RUN npm install  
  
COPY requirements.txt requirements.txt  
RUN pip install -r requirements.txt  
  
COPY . /app  
  
ENV DEBUG 1  
EXPOSE 8000  
CMD [ "python", "manage.py", "runserver" ]  

