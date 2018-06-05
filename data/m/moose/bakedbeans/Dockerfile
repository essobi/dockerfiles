FROM python:3.6-alpine  
  
# Create the directory layout and virtual environment  
RUN mkdir /venv /app /contents && python3.6 -m venv /venv  
  
COPY . /app  
RUN /venv/bin/pip install /app/  
  
EXPOSE 3000  
CMD /venv/bin/baked --host=0.0.0.0 /contents  

