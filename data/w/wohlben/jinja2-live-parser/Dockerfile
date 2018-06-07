FROM python:2.7  
RUN git clone https://github.com/sahilsk/jinja2-live-parser.git && \  
cd jinja2-live-parser && \  
pip install -r requirements.txt  
  
RUN sed -i 's/\\(.*\\)app.run()/\1app.run(host="0.0.0.0")/' /jinja2-live-
parser/parser.py  
  
EXPOSE 5000  
CMD ["python", "/jinja2-live-parser/parser.py"]  
  

