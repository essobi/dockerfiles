FROM fstab/go  
MAINTAINER Fabian Stäber, fabian@fstab.de  
  
ENV LAST_UPDATE=2015-10-17  
USER root  
RUN apt-get install -y make  
USER go  
  
RUN go get golang.org/x/net/http2  
RUN go get camlistore.org/pkg/googlestorage; exit 0  
RUN sed -i s,"future/mime/multipart","mime/multipart",g
/home/go/src/camlistore.org/pkg/httputil/multipart.go  
  
WORKDIR /home/go/src/golang.org/x/net/http2/h2demo/  
  
# CONFIGURE SERVER IP ADDRESS: 192.168.99.100 HARD CODED  
RUN sed -i 's;"https_addr", "localhost:4430";"https_addr", "0.0.0.0:4430";g'
h2demo.go  
RUN sed -i 's;"http_addr", "";"http_addr", "0.0.0.0:8080";g' h2demo.go  
RUN sed -i 's;"http_host", "";"http_host", "192.168.99.100:8080";g' h2demo.go  
RUN sed -i 's;"https_host", "";"https_host", "192.168.99.100:4430";g'
h2demo.go  
  
# REPLACE LOADING https://blog.golang.org/go-programming-language-turns-
two_gophers.jpg WITH LOCAL FILE  
RUN curl -o go-programming-language-turns-two_gophers.jpg
https://blog.golang.org/go-programming-language-turns-two_gophers.jpg  
RUN sed -i '/https:\/\/blog.golang.org\/go-programming-language-turns-
two_gophers.jpg/,+7 s.^.//.' h2demo.go  
RUN sed -i 's;slurp, err := ioutil.ReadAll(res.Body);slurp, err :=
ioutil.ReadFile("go-programming-language-turns-two_gophers.jpg");g' h2demo.go  
RUN sed -i 's;^\tres.Body.Close();\t//res.Body.Close();' h2demo.go  
  
RUN make  
  
EXPOSE 4430 8080  
CMD ./h2demo.linux  

