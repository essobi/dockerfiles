FROM ubuntu  
MAINTAINER Xavier Garnier "xavier.garnier@inria.fr"  
# Prerequisites  
RUN apt-get update && apt-get install -y \  
git \  
build-essential \  
python3 \  
python3-pip \  
python3-venv \  
vim \  
ruby \  
npm \  
nodejs-legacy \  
# Additional packages for dev  
vim htop curl  
  
ENV ASKOMICS=https://github.com/xgaia/askomics.git  
ENV ASKOMICS_COMMIT=ff0a21d465f172715cbcbd71d3e87f2016bb4a01  
  
RUN git clone $ASKOMICS /usr/local/askomics/  
  
WORKDIR /usr/local/askomics/  
  
RUN git checkout $ASKOMICS_COMMIT  
  
RUN npm install gulp -g  
RUN npm install  
RUN chmod +x startAskomics.sh  
  
# Delete the local venv if exist and build the new one  
RUN rm -rf /usr/local/askomics/venv && \  
./startAskomics.sh -b  
  
EXPOSE 6543  
CMD ["./startAskomics.sh", "-r"]  

