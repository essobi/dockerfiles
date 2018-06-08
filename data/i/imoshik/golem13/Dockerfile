FROM golang  
WORKDIR /app  
# copy binary into image  
RUN apt-get update  
RUN apt-get install wget unzip zip -y  
RUN wget https://github.com/yandex/tomita-
parser/releases/download/v1.0/libmystem_c_binding.so.linux_x64.zip  
RUN unzip libmystem_c_binding.so.linux_x64.zip  
RUN cp libmystem_c_binding.so /usr/lib/  
RUN ln -s /usr/lib/libmystem_c_binding.so /usr/lib/libmystem_c_binding.so.1  
RUN go get github.com/go-sql-driver/mysql && \  
go get github.com/technoweenie/multipartstreamer && \  
go get github.com/go-telegram-bot-api/telegram-bot-api && \  
go get github.com/dveselov/mystem && \  
go get gopkg.in/telegram-bot-api.v4 && \  
go get github.com/getsentry/raven-go && \  
go get github.com/jmoiron/sqlx && \  
go install github.com/go-sql-driver/mysql && \  
go install github.com/technoweenie/multipartstreamer && \  
go install github.com/go-telegram-bot-api/telegram-bot-api && \  
go install gopkg.in/telegram-bot-api.v4 && \  
go install github.com/dveselov/mystem && \  
go install github.com/getsentry/raven-go && \  
go install github.com/jmoiron/sqlx  
COPY . /app/  
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -o bot  
ENTRYPOINT ["/app/bot"]  

