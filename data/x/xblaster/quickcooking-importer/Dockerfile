FROM xblaster/generic_node  
  
RUN apt-get install -y imagemagick tesseract-ocr-fra tesseract-ocr ghostscript  
  
RUN git clone https://github.com/xblaster/quickCooking3-importer  
WORKDIR quickCooking3-importer  
  
RUN npm config set registry http://registry.npmjs.org/  
  
RUN git pull && git pull  
  
RUN npm install  
RUN npm install -g gulp  
  
RUN git pull  
  
#CMD gulp  

