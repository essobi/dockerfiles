FROM askomics/virtuoso  
MAINTAINER Xavier Garnier 'xavier.garnier@irisa.fr'  
# Environment variables  
ENV ASKOMICS="https://github.com/askomics/askomics.git" \  
ASKOMICS_DIR="/usr/local/askomics" \  
ASKOMICS_VERSION="17.12" \  
SPARQL_UPDATE=true  
  
# Copy files  
COPY monitor_traffic.sh /monitor_traffic.sh  
COPY start.sh /start.sh  
COPY dump.template.nq /dump.template.nq  
  
# Install prerequisites, clone repository and install  
RUN apk add --update bash make gcc g++ zlib-dev libzip-dev bzip2-dev xz-dev
git python3 python3-dev nodejs nodejs-npm wget && \  
git clone ${ASKOMICS} ${ASKOMICS_DIR} && \  
cd ${ASKOMICS_DIR} && \  
git checkout -b ${ASKOMICS_VERSION} origin/${ASKOMICS_VERSION} && \  
npm install gulp -g && \  
npm install --production && \  
chmod +x startAskomics.sh && \  
rm -rf /usr/local/askomics/venv && \  
bash ./startAskomics.sh -b && \  
rm -rf /var/cache/apk/* && \  
chmod +x /start.sh  
  
WORKDIR /usr/local/askomics/  
  
EXPOSE 6543  
CMD ["/start.sh"]  

