FROM python:3.6-alpine3.7  
WORKDIR /app  
COPY rancher_tools.py setup.py ./  
  
RUN pip install . ipython  
  
CMD ["ipython", "-i", "-c", "import rancher_tools as rt"]  

