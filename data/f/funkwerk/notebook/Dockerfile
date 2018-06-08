FROM think/notebook:0.0.2  
MAINTAINER info@funkwerk-itk.com  
  
COPY resources/img/logo.png /usr/lib/python3.5/site-
packages/notebook/static/base/images/  
COPY resources/css/funkstyle.css /usr/lib/python3.5/site-
packages/notebook/static/custom/custom.css  
  
RUN cat /usr/lib/python3.5/site-packages/notebook/static/custom/custom.css >>
/usr/lib/python3.5/site-packages/notebook/static/style/style.min.css  

