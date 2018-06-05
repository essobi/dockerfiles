FROM python:3.6.5-jessie  
  
ENV TZ=Asia/Shanghai  
ENV DEBIAN_FRONTEND noninteractive  
  
COPY requirement.txt /requirement.txt  
COPY cmd.sh /cmd.sh  
# COPY pip.conf /root/.pip/pip.conf mirror in China  
# COPY source.list /etc/apt/sources.list mirror in China  
  
RUN apt-get update \  
&& apt install software-properties-common libxml2-dev libxslt-dev dialog apt-
utils aptitude -yf \  
&& pip install -r /requirement.txt \  
&& pip install tushare \  
&& pip install pytdx \  
&& pip install pyecharts_snapshot \  
&& curl -sL https://deb.nodesource.com/setup_8.x | bash - \  
&& apt-get install -y nodejs \  
&& aptitude install npm -yf \  
&& npm install npm -g \  
&& npm install forever -g \  
&& npm install cnpm -g \  
&& cd / \  
&& git clone https://github.com/barretthugh/QUANTAXIS \  
&& chmod -R 777 /QUANTAXIS \  
&& cd /QUANTAXIS \  
&& pip install -e . \  
&& cd /QUANTAXIS/QUANTAXIS_Webkit/backend \  
&& npm install \  
&& cd /QUANTAXIS/QUANTAXIS_Webkit/web \  
&& npm install \  
&& apt-get clean -y \  
&& apt-get autoclean -y \  
&& apt-get autoremove -y \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& chmod +x /cmd.sh  
  
EXPOSE 8080  
EXPOSE 3000  
  
CMD ["/cmd.sh"]  

