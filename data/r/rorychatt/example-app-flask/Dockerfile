FROM alpine  
  
MAINTAINER Rory Chatterton "rorychatt@gmail.com"  
# Get PIP, Python & Build Essentials  
RUN apk add --no-cache bash git python3 python3-dev py3-psycopg2 \  
&& python3 -m ensurepip \  
&& rm -r /usr/lib/python*/ensurepip \  
&& pip3 install --upgrade pip \  
&& pip3 install flask \  
&& rm -r /root/.cache  
  
# Copy over requirements first to leverage Docker caching feature  
COPY ./requirements.txt /app/requirements.txt  
  
# Install Python dependancies  
WORKDIR /app  
RUN pip install -r requirements.txt  
  
# Copy the rest over  
COPY . /app  
WORKDIR /app  
  
# Start gunicorn server on :8000  
CMD ["/usr/bin/gunicorn", "demoapp:app", "-b 0.0.0.0:8000"]  

