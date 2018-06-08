FROM ubuntu  
  
#FFMPEG.  
RUN apt-get update  
RUN apt-get install -y libffi-dev libssl-dev  
RUN apt-get install -y python3 python3-pip python3-setuptools python3-dev
build-essential  
RUN apt-get install -y ffmpeg  
  
#Update pip  
RUN pip3 install --upgrade pip  
  
# Pre-install requirements  
ADD requirements.txt /SassyBot/requirements.txt  
  
# Install packages via pip  
RUN pip3 install -r /SassyBot/requirements.txt  
  
# Add project fully.  
ADD ./ /SassyBot/  
  
# Run project  
WORKDIR /SassyBot/  
CMD python3 sassybot.py  

