FROM alpine:3.6 AS builder  
RUN apk add --no-cache binutils nasm  
COPY src/hang.asm /hang.asm  
RUN nasm -f elf64 -o hang.o hang.asm && ld -s -o hang hang.o  
  
FROM scratch  
COPY \--from=builder /hang /hang  
ENTRYPOINT ["/hang"]  

