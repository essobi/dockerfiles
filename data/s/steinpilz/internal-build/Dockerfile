FROM microsoft/dotnet:2.0.5-sdk-2.1.4-stretch  
  
# mono_start  
  
ENV MONO_VERSION 5.8.0.108  
  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF  
  
RUN echo "deb http://download.mono-project.com/repo/debian
jessie/snapshots/$MONO_VERSION main" > /etc/apt/sources.list.d/mono-
official.list \  
&& apt-get update \  
&& apt-get install -y mono-runtime \  
&& rm -rf /var/lib/apt/lists/* /tmp/*  
  
RUN apt-get update \  
&& apt-get install -y binutils curl mono-devel ca-certificates-mono fsharp
mono-vbnc nuget referenceassemblies-pcl \  
&& rm -rf /var/lib/apt/lists/* /tmp/*  
# mono_end  
# locale_fix_start  
# locale fix based on the https://serverfault.com/a/689947  
  
RUN apt-get update \  
&& apt-get install -y locales \  
&& rm -rf /var/lib/apt/lists/* /tmp/*  
  
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \  
echo 'LANG="en_US.UTF-8"' > /etc/default/locale && \  
dpkg-reconfigure --frontend=noninteractive locales && \  
update-locale LANG=en_US.UTF-8  
  
# locale_fix_end  

