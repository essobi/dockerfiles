FROM compulsivecoder/ubuntu-base  
  
RUN apt-get update && apt-get -y upgrade  
  
RUN apt-get install -y curl python  
  
RUN python -c "$(curl -fsSL
https://raw.githubusercontent.com/platformio/platformio/develop/scripts/get-
platformio.py)"  

