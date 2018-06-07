FROM ubuntu:latest  
  
# configuration  
ENV PDFOCR_CONFIG /etc/pypdfocr.conf  
ENV PDFOCR_BASEPATH /srv  
ENV T_LANG deu  
  
# install software  
RUN sh -c "set -x \  
&& apt-get update && apt-get install -y locales curl python python-setuptools
python-watchdog python-reportlab python-pil python-pypdf2 tesseract-ocr
tesseract-ocr-${T_LANG} ghostscript imagemagick poppler-utils\  
&& apt-get purge -y --auto-remove"  
# setup locales  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
  
# copy orientation data  
RUN cp /usr/share/tesseract-ocr/tessdata/${T_LANG}.traineddata
/usr/share/tesseract-ocr/tessdata/osd.traineddata  
  
# copy default configuration file  
WORKDIR /  
COPY pypdfocr.conf ${PDFOCR_CONFIG}  
# Patch for _text files  
#COPY watcher_ignore_textpdf.patch .  
#RUN patch -l /usr/local/lib/python2.7/dist-
packages/pypdfocr/pypdfocr_watcher.py -i watcher_ignore_textpdf.patch  
# Patch for regex  
#COPY regex.patch .  
#RUN patch -l /usr/local/lib/python2.7/dist-
packages/pypdfocr/pypdfocr_pdffiler.py -i regex.patch  
# download pypdfocr from own repository (with modifications and patches)  
RUN mkdir /tmp/pypdfocr  
WORKDIR /tmp/pypdfocr  
RUN sh -c "curl -L https://github.com/thelexus/pypdfocr/tarball/master | tar
xz --strip=1"  
RUN sh -c "python setup.py install"  
# define volumes  
VOLUME ${PDFOCR_BASEPATH}/documents ${PDFOCR_BASEPATH}/pdfinput  
  
WORKDIR /  
CMD ["sh","-c","/usr/local/bin/pypdfocr -l ${T_LANG} \--remove -w
${PDFOCR_BASEPATH}/pdfinput --splitting -f -c ${PDFOCR_CONFIG} -n"]  
#CMD ["/bin/bash"]  

