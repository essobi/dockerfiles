FROM blang/latex  
MAINTAINER Sönke Liebau <soenke.liebau@opencore.com>  
  
RUN apt-get update -q  
RUN apt-get -qy install python python-pip  
RUN pip install jinja2  
ADD run.py /usr/local/bin/run.py  
  
# Install necessary fonts  
RUN mkdir /usr/share/fonts/truetype/helvetica  
COPY font/* /usr/share/fonts/truetype/helvetica/  
  
WORKDIR /documents  
VOLUME ["/documents"]  
CMD /usr/local/bin/run.py

