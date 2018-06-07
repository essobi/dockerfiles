FROM orchardup/python:2.7  
RUN pip install --install-option="--install-scripts=/usr/bin" -U pip && pip
install -U setuptools wheel  
RUN mkdir /wheelhouse  
VOLUME /wheelhouse  
WORKDIR /wheelhouse  
ADD build_wheel.sh /  
RUN chmod +x /build_wheel.sh  
ENTRYPOINT ["/build_wheel.sh"]  

