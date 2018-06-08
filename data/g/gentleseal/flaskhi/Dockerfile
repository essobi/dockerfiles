# Use python 2 image as base ("inherit" from it)  
FROM python:2  
# Set working directory (used by 2nd argument of COPY)  
WORKDIR /usr/src/app  
# Install dependencies  
RUN pip install --no-cache-dir flask  
# Copy our code in (will go to /usr/src/app [workdir])  
COPY example_app.py .  
# CMD is ran when container is started (so on start we run example_app.py)  
CMD [ "python", "./example_app.py" ]  

