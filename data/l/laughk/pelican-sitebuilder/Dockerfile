FROM alpine:latest  
  
ENV ALPINE_PACKAGES="\  
python3 \  
rsync \  
openssh \  
git \  
bash \  
"  
ENV PY_PACKAGES="\  
pelican \  
markdown \  
"  
RUN echo && \  
apk add --no-cache $ALPINE_PACKAGES && \  
pip3 install -U pip && \  
pip3 install $PY_PACKAGES && \  
mkdir -pv /project-root /my-theme && \  
git clone \--recursive https://github.com/getpelican/pelican-plugins /pelican-
plugins && \  
git clone \--recursive https://github.com/getpelican/pelican-themes /pelican-
themes  
  
COPY builder /usr/local/bin/  
VOLUME ["/project-root", "/theme"]  
WORKDIR /project-root  
CMD ["builder"]  

