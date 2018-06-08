FROM mono:4.6  
MAINTAINER Edijs Timosenko  
  
RUN mkdir -p /usr/src/app/source /usr/src/app/build  
WORKDIR /usr/src/app/source  
COPY . /usr/src/app/source  
RUN xbuild /property:Configuration=Release
/property:OutDir=/usr/src/app/build/  
WORKDIR /usr/src/app/build  
  
ENTRYPOINT [ "mono", "./Lighthouse.exe" ]

