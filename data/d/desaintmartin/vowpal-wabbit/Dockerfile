FROM python:3-alpine  
MAINTAINER Cedric de Saint Martin, cdesaintmartin@wiremind.fr  
WORKDIR /app  
  
# Install vw  
RUN apk add --no-cache --virtual build-deps build-base git python3-dev boost-
dev zlib-dev && \  
git clone \--depth 1 --branch master --single-branch \  
git://github.com/JohnLangford/vowpal_wabbit.git /app/build && \  
cd /app/build && make && make install &&\  
cd / && \  
apk del build-deps && \  
rm -rf /var/cache/apk/* && rm -rf /app/build && \  
apk --no-cache add --virtual run-deps boost-program_options zlib libstdc++  
RUN mkdir ./saved-data  
EXPOSE 26542  
# Deploy flask minimal app that allows to trigger s3 upload  
COPY s3uploader/requirements.txt .  
RUN pip install -r requirements.txt  
COPY s3uploader .  
RUN pip install .  
  
COPY vw-wrapper.sh .  
ENTRYPOINT ["/app/vw-wrapper.sh"]  

