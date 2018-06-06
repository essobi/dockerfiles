FROM python:2.7  
COPY requirements.txt /requirements.txt  
COPY text_vis.py /text_vis.py  
RUN pip install -r /requirements.txt  
RUN apt-get update  
RUN apt-get install unzip -y  
ADD https://github.com/amueller/word_cloud/archive/master.zip master.zip  
RUN unzip master.zip  
WORKDIR word_cloud-master  
RUN python ./setup.py install  
VOLUME [ "/input", "/output" ]  
WORKDIR /  
CMD python text_vis.py /input /output  

