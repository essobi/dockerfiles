FROM eschoute/python3-qiskit:0.0.3  
RUN apk --no-cache --update-cache add --virtual lint-build \  
build-base linux-headers  
RUN pip install --no-cache-dir pylint mypy  
RUN apk del lint-build  

