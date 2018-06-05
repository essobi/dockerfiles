FROM luisli88/centos6-python2.7  
MAINTAINER Luis Ricardo Ruiz <luislicardo1307@gmail.com>  
  
#Install developer dependencies  
RUN yum install -y \  
freetype-devel \  
mysql-devel \  
postgresql-devel \  
libjpeg-devel \  
libpng-devel \  
blas-devel \  
lapack-devel  
  
#Install environment  
RUN pip install \  
akismet==0.2.0 \  
altgraph==0.10.2 \  
backports.ssl-match-hostname==3.4.0.2 \  
bdist-mpkg==0.5.0 \  
certifi==2015.4.28 \  
cmsplugin-contact==1.0.0 \  
cmsplugin-filer==0.9.5 \  
dj-database-url==0.2.2 \  
dj-static==0.0.5 \  
Django==1.5.5 \  
django-appconf==0.6 \  
django-bootstrap-form==3.1 \  
django-bower==5.0.4 \  
django-calendarium==0.4.6 \  
django-classy-tags==0.4 \  
django-clear-cache==0.3 \  
django-cms==2.4.3 \  
django-colorful==0.1.3 \  
django-debug-toolbar==1.0.1 \  
django-easy-pdf==0.1.0 \  
django-filer==0.9.5 \  
django-filter==0.9.1 \  
django-filters==0.1.0 \  
django-floppyforms==1.1.1 \  
django-imagekit==3.0.4 \  
django-mptt==0.5.2 \  
django-p3p==1.0.1 \  
django-password-reset==0.6 \  
django-polymorphic==0.5.3 \  
django-reversion==1.7 \  
django-sekizai==0.7 \  
django-subdomains==2.0.4 \  
django-swingtime==0.4 \  
django-toolbelt==0.0.1 \  
djangorestframework==2.3.12  
RUN pip install \  
easy-thumbnails==1.4 \  
feedparser==5.1.3 \  
gunicorn==18.0 \  
html2text==2015.2.18 \  
html5lib==0.99 \  
images2gif==1.0.1 \  
macholib==1.5.1 \  
matplotlib==1.3.1 \  
modulegraph==0.10.4 \  
MySQL-python==1.2.5 \  
nose==1.3.7 \  
numpy==1.8.1 \  
oauthlib==0.6.3 \  
pdfkit==0.5.0 \  
pilkit==1.1.6 \  
Pillow==2.4.0 \  
psycopg2==2.5.1 \  
py2app==0.7.3 \  
pyparsing==2.0.1 \  
PyPDF2==1.25.1 \  
python-dateutil==2.2 \  
python-memcached==1.53  
RUN pip install \  
python-openid==2.2.5 \  
python-social-auth==0.1.26 \  
pytz==2013.7 \  
reportlab==3.2.0 \  
requests==2.3.0 \  
requests-oauthlib==0.4.1 \  
scipy==0.13.3 \  
six==1.4.1 \  
South==1.0.2 \  
sqlparse==0.1.11 \  
static==0.4 \  
suds==0.4 \  
tornado==4.2.1 \  
Twisted==13.2.0 \  
urllib3==1.8.2 \  
virtualenv==1.11.6 \  
wheel==0.24.0 \  
wkhtmltopdf==0.2 \  
xattr==0.6.4 \  
xhtml2pdf==0.0.6 \  
zope.interface==4.1.1  
#install NodeJS  
RUN yum install -y \  
screen  
  
WORKDIR /opt/sources  
RUN wget http://nodejs.org/dist/v0.12.9/node-v0.12.9.tar.gz  
RUN tar -xf node-v0.12.9.tar.gz  
RUN cd node-v0.12.9 \  
&& ./configure --prefix=/usr/local \  
&& make \  
&& make install  
  
#install phantomjs  
RUN yum -y install \  
gcc \  
gcc-c++ \  
make \  
flex \  
bison \  
gperf \  
ruby \  
openssl-devel \  
freetype-devel \  
fontconfig-devel \  
libicu-devel \  
sqlite-devel \  
libpng-devel \  
libjpeg-devel  
RUN git clone --recursive git://github.com/ariya/phantomjs.git  
RUN pip install \  
argparse  
RUN cd phantomjs && python2.7 build.py  
RUN cp phantomjs/bin/phantomjs /usr/local/bin/  
#Clean the repository  
WORKDIR /opt  
RUN rm -rf /opt/sources  
  
#install latest dependencies for network tasks  
RUN yum -y install \  
nc \  
openssh-server  
RUN mkdir /var/run/sshd  
RUN echo 'root:arquibogota' | chpasswd  
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config  
RUN sed -ri 's/#UsePAM no/UsePAM no/g' /etc/ssh/sshd_config  
  
# SSH login fix. Otherwise user is kicked off after login  
RUN echo "export VISIBLE=now" >> /etc/profile  
  
#COnfigurar las fuentes nativas  
RUN yum -y install \  
epel-release  
RUN yum -y install \  
wine-fonts  
  
RUN pip install django-codemirror-widget  
  
#COnfigure Static files  
WORKDIR /opt/project  
  
#Expose the needed ports  
EXPOSE 22  
EXPOSE 8000  
#Configure Starting services  
CMD ["/etc/init.d/sshd", "start"]  

