FROM ubuntu  
  
# Install Tools  
RUN apt-get update  
RUN apt-get -y install sudo  
RUN apt-get -y install apt-transport-https  
RUN apt-get -y install tzdata  
  
# Install NuGet, Mono, Mono-XBuild  
RUN apt-get -y install nuget  
RUN apt-get -y install mono-devel  
RUN apt-get -y install mono-xbuild  
  
# Install Gauge  
RUN apt-key adv --keyserver hkp://pool.sks-keyservers.net --recv-keys 023EDB0B  
RUN echo deb https://dl.bintray.com/gauge/gauge-deb stable main | sudo tee -a
/etc/apt/sources.list  
RUN apt-get update  
RUN apt-get install gauge  
  
# Install Gauge Language Runner  
RUN gauge install csharp  
  
# Install Gauge Plugins  
RUN gauge install html-report  
RUN gauge install xml-report  
RUN gauge install spectacle  
RUN gauge install flash  
  
# Install WebDrivers  
RUN apt-get -y install chromium-chromedriver  
RUN ln -s /usr/lib/chromium-browser/chromedriver /usr/bin/chromedriver  
  
ENV PATH=$HOME/.gauge:$PATH  

