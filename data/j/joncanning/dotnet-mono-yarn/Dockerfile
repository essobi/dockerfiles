FROM microsoft/dotnet  
  
RUN apt update \  
&& apt upgrade -y \  
&& apt install -y apt-transport-https \  
&& apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 \--recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF \  
&& echo "deb https://download.mono-project.com/repo/debian stable-stretch
main" | tee /etc/apt/sources.list.d/mono-official-stable.list \  
&& curl -sL https://deb.nodesource.com/setup_10.x | bash - \  
&& curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add \- \  
&& echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list \  
&& apt update \  
&& apt install -y mono-complete nodejs yarn

