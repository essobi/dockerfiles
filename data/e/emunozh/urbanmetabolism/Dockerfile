FROM dock0/arch  
MAINTAINER emunozh <emunozh@gmail.com>  
RUN pacman -S --needed --noconfirm base  
  
WORKDIR /usr/src/app  
  
COPY requirements.txt ./  
RUN pacman -Syu --noconfirm  
RUN pacman -S --needed --noconfirm python python-setuptools  
RUN pacman -S --needed --noconfirm python python-pip  
RUN pacman -S --needed --noconfirm gcc  
RUN pacman -S --needed --noconfirm tk  
RUN pacman -S --needed --noconfirm gcc-fortran  
RUN pacman -S --needed --noconfirm r  
RUN pacman -S --needed --noconfirm python-rpy2  
RUN pacman -S --needed --noconfirm python-ipykernel  
RUN pacman -S --needed --noconfirm jupyter-notebook  
RUN pacman -S --needed --noconfirm npm  
RUN pacman -S --needed --noconfirm mathjax  
RUN pacman -S --needed --noconfirm wget  
RUN pacman -S --needed --noconfirm pandoc  
RUN pip install --no-cache-dir -r requirements.txt  
RUN pip install --no-cache-dir rpy2  
RUN npm install -g configurable-http-proxy  
RUN jupyter-nbextension install rise --py --sys-prefix  
RUN jupyter-nbextension enable rise --py --sys-prefix  
  
COPY . .  
  
COPY hub/ /usr/share/jupyter/hub  
COPY hub/static/favicon.ico /usr/lib/python3.6/site-
packages/notebook/static/base/images/favicon.ico  
COPY hub/static/favicon.ico /usr/lib/python3.6/site-
packages/notebook/static/base/images/favicon-busy.ico  
COPY .jupyter/custom/logo.png /usr/lib/python3.6/site-
packages/notebook/static/base/images/logo.png  
  
RUN R CMD INSTALL GREGWT_0.7.5.tar.gz  
RUN python setup.py install  
  
COPY makenewuser /usr/bin/makenewuser  
RUN chmod +x /usr/bin/makenewuser  
RUN makenewuser esteban  
RUN makenewuser test  

