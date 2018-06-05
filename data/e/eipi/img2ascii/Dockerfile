FROM python:2.7  
MAINTAINER eipi-1 <eipiminusone@gmail.com>  
  
WORKDIR /code  
  
RUN apt update &&\  
apt install -y git &&\  
git clone https://github.com/wahtak/ascii-net &&\  
pip install -r ascii-net/requirements.txt  
  
VOLUME /images  
WORKDIR /code/ascii-net  
  
# Run code once to init model  
RUN python test_ocr.py  
  
ENV THRESHOLD=50  
CMD for i in `ls /images`; do convert /images/"$i" -resize 720x630 -threshold
$THRESHOLD% -negate -background black -gravity center -extent 720x630
/code/ascii-net/test/test_image_w_inv.png && python test_ocr.py; done  

