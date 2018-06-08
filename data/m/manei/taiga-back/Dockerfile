FROM manei/taiga-back-base:latest  
MAINTAINER Mihai Anei <mihai.anei@gmail.com>  
LABEL Description="Taiga Backend Image"  
  
RUN cd / && git clone \--branch 2.1.0 https://github.com/taigaio/taiga-
back.git taiga-back \  
&& cd taiga-back \  
&& git checkout stable \  
&& pip install -r requirements.txt  
  
ADD local.py /taiga-back/settings/local.py  
ADD common.py /taiga-back/settings/common.py  
  
# RUN pip install circus  
# RUN mkdir /conf/  
# ADD circus.ini /conf/circus.ini  
# RUN circusctl reloadconfig  
WORKDIR /taiga-back  
CMD ["python", "manage.py", "runserver"]

