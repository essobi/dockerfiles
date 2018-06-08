FROM fedora:22  
MAINTAINER Patrice FERLET <metal3d@gmail.com>  
  
EXPOSE 8000  
RUN set -ex;\  
dnf install -v -y \  
python-pip \  
pandoc-pdf \  
texlive-sourcesanspro \  
texlive-framed texlive-ly1 texlive-collection-fontsrecommended \  
texlive-collection-langfrench; \  
rm -rf /var/cache/dnf/*; \  
pip install gunicorn  
  
COPY pandoc-server/main.py /opt/main.py  
WORKDIR /opt  
  
CMD ["gunicorn", "-w" ,"4","-b","0.0.0.0:8000", "main:app"]  
  

