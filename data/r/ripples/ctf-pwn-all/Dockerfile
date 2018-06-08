FROM pwntools/pwntools:stable  
  
USER root  
  
# set timezone  
ENV TZ=Asia/Shanghai  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ >/etc/timezone  
  
# add user  
RUN groupadd -r pwn && useradd -r -g pwn pwn  
USER pwn  
  
ENV TERM linux  
ENV PYTHONPATH /var/pwn/utils:$PYTHONPATH  
WORKDIR /var/pwn/pwning  
  
CMD ["python", "-u", "pwn_all.py"]  

