FROM alpine  
MAINTAINER Olivier Filangi "olivier.filangi@inra.fr"  
# Environment variables  
ENV ASKOMICS="https://github.com/askomics/askomics.git" \  
ASKOMICS_DIR="/usr/local/askomics" \  
ASKOMICS_VERSION="federation"  
# Install prerequisites, clone repository and install  
RUN apk add --update bash make gcc g++ zlib-dev libzip-dev bzip2-dev xz-dev
git linux-headers python3 python3-dev nodejs nodejs-npm linux-headers && \  
git clone ${ASKOMICS} ${ASKOMICS_DIR} && \  
cd ${ASKOMICS_DIR} && \  
git checkout ${ASKOMICS_VERSION} && \  
npm install gulp -g && \  
npm install --production && \  
chmod +x startAskomics.sh && \  
rm -rf /usr/local/askomics/venv && \  
bash ./startAskomics.sh -b && \  
rm -rf /var/cache/apk/*  
  
WORKDIR /usr/local/askomics/  
  
EXPOSE 6543  
CMD ["bash", "./startAskomics.sh", "-r"]  

