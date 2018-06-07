##################################################################################  
# /$$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$ /$$ /$$$$$$$ #  
# | $$__ $$|_ $$_/ /$$__ $$ /$$__ $$ /$$__ $$ /$$__ $$| $$ | $$| $$__ $$ #  
# | $$ \ $$ | $$ | $$ \\__/| $$ \\__/| $$ \ $$| $$ \\__/| $$ | $$| $$ \ $$ #  
# | $$ | $$ | $$ | $$$$$$ | $$ | $$ | $$| $$$$$$ | $$ | $$| $$$$$$$ #  
# | $$ | $$ | $$ \\____ $$| $$ | $$ | $$ \\____ $$| $$ | $$| $$__ $$ #  
# | $$ | $$ | $$ /$$ \ $$| $$ /$$| $$ | $$ /$$ \ $$| $$ | $$| $$ \ $$ #  
# | $$$$$$$/ /$$$$$$| $$$$$$/| $$$$$$/| $$$$$$/| $$$$$$/| $$$$$$/| $$$$$$$/ #  
# |_______/ |______/ \\______/ \\______/ \\______/ \\______/ \\______/
|_______/ #  
# #  
# discosub 0.3.0 #  
# author: 4383 (Hervé Beraud) #  
# url: https://github.com/4383/discosub #  
##################################################################################  
FROM ubuntu:latest  
  
RUN apt-get update  
RUN apt-get -y install tor && \  
apt-get -y install proxychains  
  
RUN apt-get -y install python-pip  
  
  
COPY . /usr/src/discosub  
WORKDIR /usr/src/discosub  
  
RUN pip install -r requirements.txt  
  
ENV TARGET=google.com  
WORKDIR /usr/src/discosub/discosub  
ENV PYTHONPATH="${PYTHONPATH}:/usr/src/discosub"  
  
CMD service tor start && \  
service tor status && \  
proxychains python main.py run $TARGET  

