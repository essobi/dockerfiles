FROM alpine:3.4  
RUN apk update  
RUN apk add gcc python3 python3-dev freetds-dev freetds git linux-headers
musl-dev  
RUN pip3 install cython  
RUN pip3 install
git+https://github.com/pymssql/pymssql.git@3bc299936fe2d35196dd4c9ebc8a22777f0c97e6  
RUN pip3 install gunicorn python-dotenv pymysql  

