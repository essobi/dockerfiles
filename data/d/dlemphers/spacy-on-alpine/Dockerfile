FROM python:3-alpine  
  
LABEL maintainer="dlemphers@gmail.com"  
  
RUN apk add -U wget bash tzdata build-base libffi-dev openssl-dev  
  
RUN echo "http://dl-8.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories  
  
RUN apk --no-cache --update-cache add gcc gfortran python python-dev py-pip
build-base wget freetype-dev libpng-dev openblas-dev  
  
ENV TZ=America/Chicago  
  
# Clean APK cache  
RUN rm -rf /var/cache/apk/*  
  
# Install large deps here so they are cached  
RUN pip install pandas  
RUN pip install matplotlib  
RUN pip install scipy  
RUN pip install scikit-learn  
RUN pip install beautifulsoup4  
RUN pip install spacy  
  
RUN python -m spacy download en_core_web_sm

