FROM python:3.4  
# Set PYTHONUNBUFFERED so output is displayed in the Docker log  
ENV PYTHONUNBUFFERED=1  
EXPOSE 8000  
WORKDIR /usr/src/app  
  
# Install dependencies  
COPY requirements.txt requirements.txt  
RUN pip install -r requirements.txt  
  
# Copy the rest of the application's code  
COPY . /usr/src/app  
  
# Run the app  
CMD ["./run_app.sh"]  

