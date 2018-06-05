FROM ubuntu:trusty  
  
MAINTAINER tuna7@fsoft.com.vn  
  
RUN /bin/bash -c 'echo "deb http://cran.rstudio.com/bin/linux/ubuntu trusty/"
>> /etc/apt/sources.list' && \  
gpg --keyserver keyserver.ubuntu.com --recv-key E084DAB9 && \  
gpg -a --export E084DAB9 | apt-key add -  
  
RUN apt-get update && apt-get install -y curl git  
  
# Install nodejs  
RUN curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash - && apt-get
install -y nodejs  
  
#Install R-base  
RUN apt-get -y install r-base r-base-core r-recommended r-base-html r-base-dev  
  
#Install R libraries  
RUN apt-get -y install libcurl4-gnutls-dev libxml2-dev libssl-dev  
  
RUN Rscript -e "install.packages('devtools', repos='http://cran.rstudio.com/',
dependencies = TRUE)" && \  
Rscript -e "devtools::install_github('twitter/AnomalyDetection')" && \  
Rscript -e "install.packages('RSQLite', repos='http://cran.rstudio.com/',
dependencies = TRUE)" && \  
Rscript -e "install.packages('httr', repos='http://cran.rstudio.com/',
dependencies = TRUE)" && \  
Rscript -e "install.packages('jsonlite', repos='http://cran.rstudio.com/',
dependencies = TRUE)"  
  
RUN mkdir /installation  
WORKDIR /installation  
COPY . /installation  
  
RUN npm install && npm update && npm install pm2 -g  
RUN npm install -g --unsafe-perm node-red  
ADD flows/settings.js /root/.node-red/settings.js  
ADD flows/flows.json /root/.node-red/flows.json  
  
RUN cd /root/.node-red/ && \  
npm install node-red-contrib-http-auth0 && \  
npm install node-red-contrib-aws-sdk && \  
npm install node-red-contrib-job-queue && \  
npm uninstall -g node-red-node-serialport && \  
npm rebuild  
  
EXPOSE 1880  
ENTRYPOINT ["pm2"]  
CMD ["start", "node-red", "--no-daemon"]  
  

