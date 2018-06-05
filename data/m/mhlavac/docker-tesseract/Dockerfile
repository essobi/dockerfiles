# Tesseract OCR Runtime Environment - Docker Container  
# with deu, ces and helpful aliases  
FROM tesseractshadow/tesseract4re  
  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y tesseract-ocr tesseract-ocr-deu tesseract-ocr-ces
imagemagick  
  
COPY ocr /bin/ocr  
COPY ocr-ces /bin/ocr-ces  
COPY ocr-deu /bin/ocr-deu  
COPY ocr-eng /bin/ocr-eng  
COPY img2txt-ces /bin/img2txt-ces  
COPY img2txt-deu /bin/img2txt-deu  
COPY img2txt-eng /bin/img2txt-eng  
  
WORKDIR /home/work  

