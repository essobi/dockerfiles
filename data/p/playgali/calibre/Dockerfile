FROM debian  
MAINTAINER Galileo Martinez "playgali@gmail.com"  
ENV REFRESHED_AT 2017-Sep-22  
RUN apt-get update && apt-get install -y wget python xdg-utils && apt-get
clean \  
&& wget -nv -O- https://download.calibre-ebook.com/linux-installer.py \  
| python -c "import sys; main=lambda:sys.stderr.write('Download failed\n'); \  
exec(sys.stdin.read()); main(install_dir='/opt', isolated=True)"  
  
EXPOSE 8080  
ENTRYPOINT ["/opt/calibre/calibre-server"]  
CMD ["/calibre"]  

