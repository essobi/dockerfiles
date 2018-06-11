FROM node:0.10.35  
RUN \  
groupadd -r yomypopcorn && \  
useradd -r -g yomypopcorn yomypopcorn  
  
RUN mkdir /src  
  
COPY docker-run.sh /run.sh  
RUN chmod +x /run.sh  
  
COPY . /src/  
  
RUN \  
chown -R yomypopcorn:yomypopcorn /src && \  
cd /src/ && \  
npm install -g  
  
WORKDIR /src  
  
CMD [ "/run.sh" ]  

