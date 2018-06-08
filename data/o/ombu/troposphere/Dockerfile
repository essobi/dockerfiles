FROM python:2.7-slim  
  
MAINTAINER OMBU  
  
WORKDIR /tmp  
  
RUN apt-get -qq update && apt-get install -y build-essential libssl-dev groff
\  
&& rm -rf /var/lib/apt/lists/*  
  
COPY requirements.txt .  
  
RUN pip install -r requirements.txt  
  
CMD ["pip", "freeze"]  
  

