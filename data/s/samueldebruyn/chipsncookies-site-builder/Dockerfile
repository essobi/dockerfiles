FROM samueldebruyn/hugo-build:latest  
MAINTAINER Samuel Debruyn <s@muel.be>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# setup workdir  
RUN mkdir -p /root/work/  
WORKDIR /root/work/  
  
# install mono sources to get latest stable version of mono  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF  
RUN echo "deb http://download.mono-project.com/repo/debian wheezy main" | tee
/etc/apt/sources.list.d/mono-xamarin.list  
RUN echo "deb http://download.mono-project.com/repo/debian wheezy-
apache24-compat main" | tee -a /etc/apt/sources.list.d/mono-xamarin.list  
RUN echo "deb http://download.mono-project.com/repo/debian wheezy-
libjpeg62-compat main" | tee -a /etc/apt/sources.list.d/mono-xamarin.list  
  
# install node  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -  
  
# install mono  
RUN apt-get -y install mono-devel nuget nodejs  
  
# install browserify  
RUN npm install -g browserify  
  
# install uglify  
RUN npm install -g uglify-js  
  
# slim down image  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# echo mono version  
CMD echo mono --version  

