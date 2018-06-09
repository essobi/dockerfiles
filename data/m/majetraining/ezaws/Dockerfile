FROM python:3.6  
LABEL maintainer="jd@maje.biz"  
ARG target_dir=/appli  
ADD requirements.txt ${target_dir}/  
RUN pip install -r ${target_dir}/requirements.txt  
RUN cd ${target_dir} && git clone https://github.com/majeinfo/ezaws.git  
EXPOSE 8000  
WORKDIR ${target_dir}/ezaws  
CMD [ "/usr/local/bin/python", "manage.py", "runserver", "0.0.0.0:8000" ]  

