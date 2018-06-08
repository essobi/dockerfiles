from continuumio/anaconda  
RUN conda install opencv  
RUN pip install pytesseract  
RUN apt-get -y install tesseract-ocr  
ADD * /  
WORKDIR /home/  
  
# alias pancard='docker run -i --rm -v "$(pwd)":/home/ -w "/home/"
shantanuo/mypancard python /scan.py "$@"'  
# pancard pan8.jpg  

