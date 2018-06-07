FROM ubuntu:16.04  
MAINTAINER Leandro Souza <leandrocsfrb@gmail.com>  
  
RUN apt-get update  
  
#git  
RUN apt-get install -y git  
  
#ebook-convert  
RUN apt-get install -y wget python xz-utils libglu1-mesa  
RUN wget -nv -O-
https://raw.githubusercontent.com/kovidgoyal/calibre/master/setup/linux-
installer.py | python -c "import sys; main=lambda:sys.stderr.write('Download
failed\n'); exec(sys.stdin.read()); main()"  
  
#add nodejs  
RUN wget --output-document nodesource.sh https://deb.nodesource.com/setup_4.x  
RUN chmod +x nodesource.sh  
RUN ./nodesource.sh  
  
RUN apt-get install -y nodejs  
  
#gitbook  
RUN npm install gitbook-cli -g  
RUN mkdir tempBook  
RUN cd tempBook  
RUN gitbook init  
RUN cd ..  
RUN rm -r tempBook  
  
#libs gitbook-editor  
RUN apt-get install -q -y libgtk2.0-0 libnotify4 libgconf-2-4 libnss3
libasound2  
  
#gitbook-editor  
RUN wget --output-document gitbook-editor-5.0.5-linux-x64.deb
http://downloads.editor.gitbook.com/download/linux-64-bit  
  
RUN dpkg -i gitbook-editor-5.0.5-linux-x64.deb  
  
CMD gitbook-editor  

