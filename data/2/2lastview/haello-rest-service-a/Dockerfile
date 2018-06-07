# base image  
FROM ubuntu:14.04  
# dependencies  
RUN apt-get update  
RUN apt-get install -y autoconf automake libtool  
RUN apt-get install -y libpng12-dev  
RUN apt-get install -y libjpeg62-dev  
RUN apt-get install -y g++  
RUN apt-get install -y libtiff4-dev  
RUN apt-get install -y libopencv-dev libtesseract-dev  
RUN apt-get install -y git  
RUN apt-get install -y cmake  
RUN apt-get install -y build-essential  
RUN apt-get install -y libleptonica-dev  
RUN apt-get install -y liblog4cplus-dev  
RUN apt-get install -y libcurl3-dev  
RUN apt-get install -y python2.7-dev  
RUN apt-get install -y tk8.5 tcl8.5 tk8.5-dev tcl8.5-dev  
RUN apt-get build-dep -y python-imaging --fix-missing  
RUN apt-get install -y imagemagick  
RUN apt-get install -y wget  
RUN apt-get install -y python python-pip  
WORKDIR /  
RUN ls  
  
# build leptonica  
RUN wget http://www.leptonica.org/source/leptonica-1.70.tar.gz  
RUN tar -zxvf leptonica-1.70.tar.gz  
WORKDIR leptonica-1.70/  
RUN ./autobuild  
RUN ./configure  
RUN make  
RUN make install  
RUN ldconfig  
WORKDIR /  
RUN ls  
  
# build tesseract  
RUN wget https://tesseract-ocr.googlecode.com/files/tesseract-
ocr-3.02.02.tar.gz  
RUN tar -zxvf tesseract-ocr-3.02.02.tar.gz  
WORKDIR tesseract-ocr/  
RUN ./autogen.sh  
RUN ./configure  
RUN make  
RUN make install  
RUN ldconfig  
WORKDIR /  
RUN ls  
  
# language english  
RUN wget https://tesseract-ocr.googlecode.com/files/tesseract-
ocr-3.02.eng.tar.gz  
RUN tar -xf tesseract-ocr-3.02.eng.tar.gz  
RUN sudo cp -r tesseract-ocr/tessdata /usr/local/share/  
WORKDIR /  
RUN ls  
  
# language german  
RUN wget https://tesseract-ocr.googlecode.com/files/tesseract-
ocr-3.02.deu.tar.gz  
RUN tar -xf tesseract-ocr-3.02.deu.tar.gz  
RUN sudo cp -r tesseract-ocr/tessdata /usr/local/share/  
WORKDIR /  
RUN ls  
  
# language italian  
RUN wget https://tesseract-ocr.googlecode.com/files/tesseract-
ocr-3.02.ita.tar.gz  
RUN tar -xf tesseract-ocr-3.02.ita.tar.gz  
RUN sudo cp -r tesseract-ocr/tessdata /usr/local/share/  
WORKDIR /  
RUN ls  
  
# language french  
RUN wget https://tesseract-ocr.googlecode.com/files/tesseract-
ocr-3.02.fra.tar.gz  
RUN tar -xf tesseract-ocr-3.02.fra.tar.gz  
RUN sudo cp -r tesseract-ocr/tessdata /usr/local/share/  
WORKDIR /  
RUN ls  
  
# language spanish  
RUN wget https://tesseract-ocr.googlecode.com/files/tesseract-
ocr-3.02.spa.tar.gz  
RUN tar -xf tesseract-ocr-3.02.spa.tar.gz  
RUN sudo cp -r tesseract-ocr/tessdata /usr/local/share/  
WORKDIR /  
RUN ls  
  
# language swedish  
RUN wget https://tesseract-ocr.googlecode.com/files/tesseract-
ocr-3.02.swe.tar.gz  
RUN tar -xf tesseract-ocr-3.02.swe.tar.gz  
RUN sudo cp -r tesseract-ocr/tessdata /usr/local/share/  
WORKDIR /  
RUN ls  
  
# requirements  
ADD requirements.txt /  
RUN pip install -r requirements.txt  
  
# Work environments  
ADD ./src /src  
WORKDIR /src  
RUN ls  
  
# Run Server  
EXPOSE 8080  
CMD ["python", "rest.py"]

