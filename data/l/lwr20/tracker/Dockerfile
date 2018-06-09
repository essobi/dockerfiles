FROM ubuntu:14.04  
# Update  
RUN apt-get update  
RUN apt-get install -y python python-pip xvfb wget chromium-browser chromium-
chromedriver  
  
# Setup a chrome user  
RUN groupadd chrome && useradd -g chrome chrome  
  
# Install app dependencies  
COPY requirements.txt /home/chrome/requirements.txt  
RUN pip install -r /home/chrome/requirements.txt  
  
# Bundle app source  
COPY *.py /home/chrome/  
  
RUN chown -R chrome:chrome /home/chrome  
  
USER chrome  
WORKDIR /home/chrome  
  
ENV PATH=/usr/lib/chromium-browser:$PATH  
  
CMD [ "python", "tracker.py"]  

