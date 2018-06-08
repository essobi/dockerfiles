# Using official python runtime base image  
FROM python:3.5.2  
# Environment Variables  
ENV SQL_HOST myhost.com  
  
# Set the application directory  
WORKDIR /app  
  
# Install our requirements.txt  
ADD requirements.txt /app/requirements.txt  
RUN pip install -r requirements.txt  
  
# Copy our code from the current folder to /app inside the container  
ADD . /app  
  
RUN pip install textacy[all]  
RUN python -m spacy download en  
RUN python -m spacy download de  
  
RUN pip install numpy && \  
pip install --upgrade cython  
  
# Define our command to be run when launching the container  
# CMD ["python", "app.py"]  

