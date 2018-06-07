FROM debian:jessie  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN dpkg --add-architecture i386  
RUN sed -i "s/main/main contrib non-free/" etc/apt/sources.list  
RUN apt-get update && apt-get install -yq wine curl unrar unzip  
  
# innosetup  
RUN mkdir innosetup && \  
cd innosetup && \  
curl -fsSL -o innounp045.rar
"https://downloads.sourceforge.net/project/innounp/innounp/innounp%200.45/innounp045.rar?r=&ts=1439566551&use_mirror=skylineservers"
&& \  
unrar e innounp045.rar  
  
RUN cd innosetup && \  
curl -fsSL -o is-unicode.exe
http://files.jrsoftware.org/is/5/isetup-5.5.8-unicode.exe && \  
wine "./innounp.exe" -e "is-unicode.exe"  

