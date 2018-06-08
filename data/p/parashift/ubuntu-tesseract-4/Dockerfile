FROM ubuntu:xenial  
  
LABEL author="seo.cahill@parashift.io"  
  
ENV LANG C.UTF-8  
ENV LC_ALL C.UTF-8  
ENV PYTHONIOENCODING utf-8  
ENV PYTHON_VERSION=3.5.2  
ENV PYTHON_MAJOR=3.5  
RUN \  
apt-get update -y \  
&& apt-get install -y \  
build-essential \  
git \  
ghostscript \  
imagemagick \  
libfile-mimeinfo-perl \  
libglib2.0.0 \  
mime-support \  
openssh-client \  
poppler-utils \  
python3 \  
python3-dev \  
python3-pip  
  
RUN \  
apt-get install -y software-properties-common \  
&& add-apt-repository -y ppa:alex-p/tesseract-ocr \  
&& apt-get update \  
&& apt-get install -y \  
libtesseract-dev \  
libleptonica-dev \  
tesseract-ocr \  
tesseract-ocr-deu \  
tesseract-ocr-eng \  
&& pip3 install pip --upgrade \  
&& git clone https://github.com/sirfz/tesserocr.git \  
&& cd tesserocr \  
&& pip install . \  
&& cd .. \  
&& rm -rf tesserocr  
  
ADD https://github.com/tesseract-ocr/tessdata_best/raw/master/eng.traineddata
/usr/share/tesseract-ocr/4.00/tessdata/eng.traineddata  
ADD https://github.com/tesseract-ocr/tessdata_best/raw/master/deu.traineddata
/usr/share/tesseract-ocr/4.00/tessdata/deu.traineddata  
ADD https://github.com/tesseract-ocr/tessdata_best/raw/master/frk.traineddata
/usr/share/tesseract-ocr/4.00/tessdata/frk.traineddata  
  
RUN \  
apt-get install -y curl \  
git \  
&& curl -L https://codeclimate.com/downloads/test-reporter/test-reporter-
latest-linux-amd64 \  
> "/usr/local/bin/cc-test-reporter" \  
&& chmod +x "/usr/local/bin/cc-test-reporter"  
  
CMD ["python3"]  
  

