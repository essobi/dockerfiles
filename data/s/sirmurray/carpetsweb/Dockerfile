FROM python:3.6.1  
ENV PYTHONUNBUFFERED 1  
RUN apt-get update \  
&& apt-get install -y libmagickwand-dev imagemagick \  
&& apt-get autoremove -y --purge \  
&& rm -rf /var/lib/apt/lists/*  
RUN mkdir /config  
ADD /config/pip/ /config/  
RUN pip install -r /config/requirements.txt  
WORKDIR /src  

