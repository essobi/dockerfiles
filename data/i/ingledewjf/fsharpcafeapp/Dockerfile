FROM mono:4.8.0.495  
RUN curl -sL https://deb.nodesource.com/setup_5.x | bash - \  
&& apt-get install -y nodejs  
  
WORKDIR /app  
  
COPY . /app  
  
RUN ls  
  
RUN mono paket/paket.bootstrapper.exe  
RUN mono paket/paket.exe restore  
  
RUN chmod +x ./monobuild.sh  
  
RUN sh ./monobuild.sh  
  
RUN export NPM_FILE_PATH=$(which npm)  
  
RUN ls  
  
RUN mono packages/FAKE/tools/FAKE.exe $@ \--fsiargs -d:MONO build.fsx  
  
EXPOSE 8083  
CMD ["mono", "/app/build/CafeApp.Web.exe"]  

