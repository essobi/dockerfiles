FROM centos:7  
RUN yum install -y wget git gcc pcre-devel openssl openssl-devel libxslt-devel  
  
WORKDIR /  
  
RUN curl --silent --location https://rpm.nodesource.com/setup_4.x | bash -  
  
RUN yum install -y nodejs  
  
COPY . /root/web  
  
WORKDIR /root/web  
  
RUN npm install  
  
RUN npm install -g supervisor  
  
RUN echo -n "ldwcnmlgb.pw" > conf/DBIp  
  
WORKDIR /  
  
RUN wget https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-64bit-
static.tar.xz -O ffmpeg.tar.xz  
  
RUN xz -d ffmpeg.tar.xz  
  
RUN mkdir ffmpeg  
  
RUN tar xvf ffmpeg.tar -C ffmpeg --strip-components 1  
  
RUN git clone git://github.com/arut/nginx-rtmp-module.git  
  
RUN wget http://nginx.org/download/nginx-1.2.4.tar.gz  
  
RUN tar xzf nginx-1.2.4.tar.gz  
  
WORKDIR /nginx-1.2.4  
  
RUN ./configure --add-module=/nginx-rtmp-module --with-http_xslt_module  
  
RUN make  
  
RUN make install  
  
COPY nginx.conf /nginx-1.2.4/conf/nginx.conf  
  
COPY nclients.xsl /usr/local/nginx/html/  
  
RUN chmod 777 /usr/local/nginx/html  
  
EXPOSE 8099  
EXPOSE 1935  
WORKDIR /root/web  
  
RUN chmod +x start.sh  
  
CMD ./start.sh  

