FROM ubuntu  
  
RUN apt-get update -q \  
&& apt-get install -q -y --fix-missing \  
ca-certificates \  
libasound2 \  
libcanberra-gtk-module \  
libgconf-2-4 \  
libgtk2.0-0 \  
libpci3 \  
libsecret-1-0 \  
libnotify4 \  
libnspr4 \  
libnss3 \  
libnss3-nssdb \  
libxext-dev \  
libxrender-dev \  
libxslt1.1 \  
libxtst6 \  
libxtst-dev \  
libxss1 \  
libxkbfile1\  
git \  
curl \  
vim  
RUN curl -o vscode.deb -J -L 'https://go.microsoft.com/fwlink/?LinkID=760868'
\  
&& dpkg -i vscode.deb \  
&& apt-get install -f \  
&& rm -f vscode.deb \  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR /work  
# CMD ["code"]  
  
CMD code -w --user-data-dir=/root/.config/Code . && while true; do echo
"[$$(date)] Hit CTRL+C"; sleep 3600; done  

