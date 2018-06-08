FROM ubuntu:trusty  
  
#For Linode only  
#COPY sources.list /etc/apt/  
  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF  
RUN echo "deb http://download.mono-project.com/repo/debian wheezy main" | sudo
tee /etc/apt/sources.list.d/mono-xamarin.list \  
&& apt-get update \  
&& apt-get install -y mono-devel fsharp mono-vbnc nuget nodejs-legacy git
build-essential npm libpq-dev curl \  
&& apt-get clean  
RUN mozroots --machine --import --sync --quiet && npm install -g npm \  
&& curl -o /root/Npgsql.dll http://ftp1.s2konline.net/t/Npgsql.dll \  
&& rm -rf /usr/lib/mono/gac/Npgsql && gacutil -i /root/Npgsql.dll && rm
/root/Npgsql.dll \  
&& rm -rf /usr/lib/mono/gac/Microsoft.VisualBasic  

