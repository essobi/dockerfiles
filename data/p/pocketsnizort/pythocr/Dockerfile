FROM ubuntu:latest  
  
ENV LANG=C.UTF-8 \  
REPO_URL=https://github.com/pocketsnizort/pythOCR \  
PYTHONPATH="/usr/share/vsscripts"  
VOLUME /input  
VOLUME /output  
VOLUME /vpys  
VOLUME /userconfig  
  
RUN apt-get update && \  
apt-get install -y software-properties-common && \  
add-apt-repository -y ppa:djcj/vapoursynth && \  
apt-get update -y --fix-missing && \  
apt-get install -y \  
enchant \  
git \  
myspell-fr \  
python3-pip \  
tesseract-ocr \  
vapoursynth \  
vapoursynth-extra-plugins && \  
pip3 install \  
colorama \  
configargparse \  
pyEnchant \  
numpy \  
opencv-python \  
tqdm && \  
mkdir /temp && \  
git clone $REPO_URL  
  
ADD https://github.com/tesseract-ocr/tessdata/raw/3.04.00/fra.traineddata
"/usr/share/tesseract-ocr/tessdata/."  
ADD https://github.com/tesseract-ocr/tessdata/raw/3.04.00/eng.traineddata
"/usr/share/tesseract-ocr/tessdata/."  
  
ENTRYPOINT ["python3", "/pythOCR/pythoCR.py", "-wd", "/tmp", "-o", "/output"]  
CMD ["--help"]  

