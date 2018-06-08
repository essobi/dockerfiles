FROM gcr.io/google-appengine/python  
LABEL python_version=python3.6  
# RUN apt-get update  
# RUN apt-get upgrade -y  
# RUN apt-get install -y libsm6 libxext6  
RUN virtualenv --no-download /env -p python3.6  
  
# Set virtualenv environment variables. This is equivalent to running  
# source /env/bin/activate  
ENV VIRTUAL_ENV /env  
ENV PATH /env/bin:$PATH  
  
# Various Python and C/build deps  
RUN apt-get update && apt-get install -y \  
wget \  
build-essential \  
cmake \  
git \  
unzip \  
pkg-config \  
python-dev \  
python-opencv \  
libopencv-dev \  
libav-tools \  
libjpeg-dev \  
libpng-dev \  
libtiff-dev \  
libjasper-dev \  
libgtk2.0-dev \  
python-numpy \  
python-pycurl \  
libatlas-base-dev \  
gfortran \  
webp \  
python-opencv \  
qt5-default \  
libvtk6-dev \  
zlib1g-dev  
  
RUN apt-get install -y tesseract-ocr  
ADD requirements.txt /app/  
RUN pip install -r requirements.txt  
# RUN pip install requests[security]  
RUN pip install opencv-python  
RUN pip install flask_api  
ADD . /app/  
CMD exec gunicorn -b :$PORT app:app  

