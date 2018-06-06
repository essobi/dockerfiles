# Using official python runtime base image  
FROM python:3.5.2  
# Environment Variables  
ENV AMQP_HOST myaccess  
ENV AMQP_PORT mysecret  
ENV AMQP_USER myendpoint.de  
ENV AMQP_PASS mybucket  
ENV AMQP_RECEIVE_QUEUE mysecret  
ENV AMQP_SEND_QUEUE myid  
  
# Set the application directory  
WORKDIR /app  
  
# Install our requirements.txt  
ADD requirements.txt /app/requirements.txt  
RUN pip install -r requirements.txt  
  
# Copy our code from the current folder to /app inside the container  
ADD . /app  
  
RUN pip install textacy[all]  
RUN python -m spacy download de  
  
RUN pip install numpy && \  
pip install --upgrade cython  
  
# Define our command to be run when launching the container  
CMD ["python", "app.py"]  

