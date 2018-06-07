FROM ubuntu:16.04  
MAINTAINER Matias Gerard <mgerard@sinc.unl.edu.ar>  
  
# Web Demo Builder - Base Docker image for Python 3.5  
ENV python_env="/python_env"  
# Install base packages  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get update && apt-get install -y --no-install-recommends \  
build-essential \  
pkg-config \  
gfortran \  
libatlas-base-dev \  
libssl-dev \  
libffi-dev \  
fonts-lyx \  
libfreetype6-dev \  
libpng-dev \  
python3 \  
python3-dev \  
python3-pip \  
python3-tk \  
git \  
tk-dev \  
libyaml-dev \  
wkhtmltopdf \  
imagemagick && \  
rm -rf /var/lib/apt/lists/*  
  
# python packages  
RUN pip3 install -U virtualenv==15.2.0  
RUN virtualenv ${python_env}  
  
COPY install_python_module /usr/local/bin/  
  
RUN install_python_module setuptools==39.0.1  
RUN install_python_module pip==9.0.3  
RUN install_python_module numpy==1.14.2  
RUN install_python_module scipy==1.0.1  
RUN install_python_module scikit-learn==0.19.0  
RUN install_python_module sklearn_extensions==0.0.2  
RUN install_python_module pandas==0.22.0  
RUN install_python_module pdfkit==0.6.1  
RUN install_python_module scikit-image==0.13.1  
RUN install_python_module opencv-python==3.4.0.12  
RUN install_python_module matplotlib==2.1.0  
RUN install_python_module theano==1.0.1  
RUN install_python_module
https://github.com/Lasagne/Lasagne/archive/master.zip  
RUN install_python_module
git+https://github.com/dnouri/nolearn.git@master\#egg=nolearn==0.7.git  
  
RUN ln -s ${python_env}/bin/python /usr/local/bin/python  
  
# Create a new user "developer".  
# It will get access to the X11 session in the host computer  
ENV uid=1000  
ENV gid=${uid}  
  
COPY init.sh /  
COPY create_user.sh /  
COPY matplotlibrc_tkagg /  
COPY matplotlibrc_agg /  
  
ENTRYPOINT ["/init.sh"]  
CMD ["/create_user.sh"]  

