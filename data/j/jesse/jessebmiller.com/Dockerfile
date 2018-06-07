from alpine:latest  
maintainer jesse@jessebmiller.com  
  
run apk update && apk add python3  
  
run mkdir /ui  
  
add index.html /ui/index.html  
add reset.css /ui/reset.css  
add style.css /ui/style.css  
  
workdir /ui  
  
cmd python3 -m http.server

