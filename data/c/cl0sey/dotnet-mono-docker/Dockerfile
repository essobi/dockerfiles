FROM microsoft/dotnet:1.0-runtime  
  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF \  
&& echo "deb http://download.mono-project.com/repo/debian wheezy-
libjpeg62-compat main" | tee -a /etc/apt/sources.list.d/mono-xamarin.list \  
&& echo "deb http://download.mono-project.com/repo/debian
wheezy/snapshots/4.4.2.11 main" | tee -a /etc/apt/sources.list.d/mono-
xamarin.list \  
&& apt-get update \  
&& apt-get install -y mono-devel \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN ln -s
/usr/share/dotnet/shared/Microsoft.NETCore.App/1.0.0/System.Native.so
/usr/lib/libSystem.Native.so  

