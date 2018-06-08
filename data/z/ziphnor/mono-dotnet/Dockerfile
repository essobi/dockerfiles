FROM ubuntu:14.04  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF  
RUN echo "deb http://download.mono-project.com/repo/debian wheezy main" | sudo
tee /etc/apt/sources.list.d/mono-xamarin.list  
RUN echo "deb http://download.mono-project.com/repo/debian wheezy-
apache24-compat main" | sudo tee -a /etc/apt/sources.list.d/mono-xamarin.list  
RUN apt-get update  
RUN apt-get install curl libunwind8 gettext mono-complete fsharp dos2unix -y  
RUN curl -sSL -o dotnet.tar.gz https://go.microsoft.com/fwlink/?LinkID=835021  
RUN mkdir -p /opt/dotnet && tar zxf dotnet.tar.gz -C /opt/dotnet  
RUN ln -s /opt/dotnet/dotnet /usr/local/bin  
# Move to bin to so that cake ends up in /bin/tools  
ADD ./cakeinstall.sh /bin/cakeinstall.sh  
RUN cd bin  
# Ensure line endings dont mess things up  
RUN dos2unix -q /bin/cakeinstall.sh  
RUN chmod +rwx /bin/cakeinstall.sh  
RUN /bin/cakeinstall.sh

