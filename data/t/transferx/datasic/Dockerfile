# 指定基于的基础镜像  
FROM ubuntu:latest  
  
# 维护者信息  
MAINTAINER transfer <448217518@qq.com>  
  
# 更新源  
RUN apt-get update  
  
# 安装python3  
RUN apt-get install -y python3  
  
# 安装科学计算相关的库  
RUN apt-get install -y python-numpy python-scipy python-matplotlib python-
pandas python-sympy python-nose  
  
# 安装pip  
RUN apt-get install -y python3-pip  
RUN pip3 install --upgrade pip  
  
# 安装jupyter  
RUN pip3 install jupyter  
  
# 安装tensorflow  
RUN pip3 install tensorflow  
  
# 端口  
EXPOSE 8888  
# 配置密码，只有这样才允许远程登录：密码“jupyter”  
ENV JUPYTER_CONFIG /root/.jupyter/jupyter_notebook_config.py  
RUN jupyter notebook --generate-config --allow-root  
RUN echo "c.NotebookApp.ip='*'" >> $JUPYTER_CONFIG  
RUN echo "c.NotebookApp.password =
'sha1:66acf0097398:0a0333384ee2c45a3dd6d9cb094ab98bff93184e'" >>
$JUPYTER_CONFIG  
RUN echo "c.NotebookApp.open_browser = False" >> $JUPYTER_CONFIG  
RUN echo "c.NotebookApp.port=8888" >> $JUPYTER_CONFIG  
  
# 指定工作路径  
VOLUME /src  
WORKDIR /src  
  
# 启动脚本  
CMD jupyter notebook --allow-root  

