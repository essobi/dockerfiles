FROM nginx  
MAINTAINER Indexyz <r18@iinde.xyz>  
RUN apt-get update && apt-get install python3 python3-setuptools build-
essential git unzip wget -y && \  
easy_install3 pip && \  
curl -sL https://deb.nodesource.com/setup_6.x | bash && \  
apt-get update && \  
apt-get install nodejs npm -y  
  
RUN git clone https://github.com/SpongePowered/SpongeDocs.git docs && \  
cd docs && pip3 install -r requirements.txt && \  
npm install && \  
wget https://crowdin.com/download/project/sponge-docs/zh-CN.zip && \  
unzip zh-CN.zip && \  
sphinx-build -D language='zh_CN' -d build/doctrees source build/html && \  
rm -rf /usr/share/nginx/html && \  
mv build/html /usr/share/nginx/html  
  
  
EXPOSE 80/tcp  

