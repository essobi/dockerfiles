# Use latest Python runtime as parent image  
FROM python:3.6.5  
# Meta-data  
LABEL maintainer="Heath Robertson <CodeHappens@ToiletHill.io>" \  
description="Machine Learning Workflow #1: Self-Contained Container\  
Libraries, and code in one image"  
  
# Set the working directory to /app  
WORKDIR /app  
  
# This works also: pip --no-cache-dir install numpy scipy matplotlib ipython
jupyter pandas sympy nose  
COPY requirements.txt ./  
RUN pip install --no-cache-dir -r requirements.txt  
  
# Copy the current directory contents into the container at /app  
COPY . /app  
  
# Make port 8888 available to the world outside this container.  
EXPOSE 8888  
CMD ["jupyter", "notebook", "--ip=*", "--port=8888", "--allow-root"]  

