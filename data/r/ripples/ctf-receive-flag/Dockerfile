FROM python:2  
# set timezone  
ENV TZ=Asia/Shanghai  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ >/etc/timezone  
  
RUN pip install requests  
  
# add user  
RUN groupadd -r pwn && useradd -r -g pwn pwn  
USER pwn  
  
WORKDIR /var/pwn/pwning  
EXPOSE 8888  
CMD ["python", "-u", "receive_flag.py"]  

