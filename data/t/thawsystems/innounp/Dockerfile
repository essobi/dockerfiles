FROM thawsystems/wine-stable  
MAINTAINER David Manouchehri  
  
USER root  
RUN apt-get -y update && \  
DEBIAN_FRONTEND=noninteractive apt-get -y install p7zip-full p7zip-rar wget  
  
RUN printf '#!/usr/bin/env bash\nWINEDEBUG=-all exec wine
"/home/innounp/innounp.exe" "$@"\n' > /usr/local/bin/innounp && chmod +x
/usr/local/bin/innounp  
  
RUN useradd -m innounp  
USER innounp  
WORKDIR /home/innounp  
ENV HOME /home/innounp  
  
RUN wget -O innounp.rar
"https://sourceforge.net/projects/innounp/files/latest/download?source=files"
&& \  
7z x innounp.rar && rm innounp.rar && \  
(wine innounp.exe || true)  

