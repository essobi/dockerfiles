FROM microsoft/dotnet  
  
ENV APP_HOME /root  
ENV MONO_VERSION 5.0.1.1  
WORKDIR $APP_HOME  
  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF  
  
RUN echo "deb http://download.mono-project.com/repo/debian
jessie/snapshots/$MONO_VERSION main" > /etc/apt/sources.list.d/mono-
official.list \  
&& apt-get update \  
&& apt-get install -y binutils mono-devel ca-certificates-mono fsharp mono-
vbnc nuget referenceassemblies-pcl sudo \  
&& rm -rf /var/lib/apt/lists/* /tmp/*  
  
# Install nodejs and npm  
RUN curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -  
RUN apt-get install -y nodejs  
  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -  
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee
/etc/apt/sources.list.d/yarn.list  
  
RUN sudo apt-get update && sudo apt-get -y install yarn  
  
# Install Fable compiler  
RUN npm -g i fable-compiler  
  
CMD ["bash"]  

