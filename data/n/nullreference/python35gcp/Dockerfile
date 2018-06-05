FROM gcr.io/google_appengine/python  
LABEL python_version=python3.5  
RUN virtualenv --no-download -p python3.5 /env  
  
ENV VIRTUAL_ENV /env  
ENV PATH /env/bin:$PATH  
ADD . /_base/  
RUN pip install -r /_base/requirements.txt

