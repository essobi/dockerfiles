# FROM 3blades/core-server:build-119 AS core  
FROM illumidesk/core-server:build-5 AS core  
FROM rocker/rstudio:3.4.1  
# Install dependencies  
RUN apt-get update \  
&& apt-get -yq dist-upgrade \  
&& apt-get install -yq --no-install-recommends \  
liblapack-dev \  
libopenblas-dev \  
libopencv-dev \  
python \  
python-dev \  
python3-distutils \  
python-pip \  
rsync \  
software-properties-common \  
unzip \  
virtualenv \  
zlib1g-dev \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install R packages  
RUN su - -c "R -e \"install.packages('devtools')\""  
  
# Install h20  
RUN su - -c "R -e \"install.packages('h2o')\""  
  
ENV ROOT TRUE  
  
EXPOSE 8080  
RUN echo "www-port=8888" > /etc/rstudio/rserver.conf  
RUN echo "session-default-working-dir=/resources" > /etc/rstudio/rsession.conf  
WORKDIR /resources  
  
# Copy runner to end to avoid cache busting  
COPY \--from=core runner /runner  

