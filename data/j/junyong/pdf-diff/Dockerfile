FROM alpine  
  
COPY pdf-diff-master/setup.py /  
COPY pdf-diff-master/pdf_diff /pdf_diff  
  
RUN apk add --update alpine-sdk python3 python3-dev py3-lxml poppler-utils
zlib-dev jpeg-dev ttf-ubuntu-font-family && \  
pip3 install Pillow && pip3 install diff_match_patch_python && \  
apk del alpine-sdk python3-dev zlib-dev jpeg-dev && rm -rf /var/cache/apk/* &&
\  
python3 setup.py install && \  
rm -rf setup.py /pdf_diff /pdf_diff.egg-info  

