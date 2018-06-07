FROM mono:4.2.3.4  
# Install unzip  
RUN apt-get update \  
&& apt-get install -y unzip \  
&& rm -rf /var/lib/apt/lists/*  
  
ADD http://aka.ms/bfemulator /tmp/bfemulator.zip  
RUN unzip /tmp/bfemulator.zip -d /tmp/  
CMD mono /tmp/BFEmulator.exe  

