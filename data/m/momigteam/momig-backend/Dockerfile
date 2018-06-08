FROM buildpack-deps:xenial as build  
  
ENV RUSTUP_HOME=/usr/local/rustup \  
CARGO_HOME=/usr/local/cargo \  
PATH=/usr/local/cargo/bin:$PATH  
  
RUN set -eux; \  
\  
url="https://static.rust-lang.org/rustup/dist/x86_64-unknown-linux-gnu/rustup-
init"; \  
wget "$url"; \  
chmod +x rustup-init; \  
./rustup-init -y --no-modify-path --default-toolchain nightly; \  
rm rustup-init; \  
chmod -R a+w $RUSTUP_HOME $CARGO_HOME; \  
mkdir /usr/src/app;  
  
RUN apt-get update && apt-get install -y \  
cmake clang \  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR /usr/src/app  
  
#COPY Cargo.toml Cargo.toml  
#COPY Cargo.lock Cargo.lock  
#RUN cargo build --release || true  
COPY . .  
  
RUN rustup override set nightly-2018-02-23 # https://github.com/rust-lang-
nursery/rust-clippy/issues/2482  
  
RUN cargo build --release; \  
rm -rf src/;  
  
# ---------------------------  
# frontend container  
FROM quay.io/vgteam/vg:v1.6.0-213-gc0c19fe5-t126-run  
ARG BUILD_DATE  
ARG VCS_REF  
  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/MoMI-G/MoMI-G/" \  
org.label-schema.schema-version="1.0.0-rc1"  
  
# Add dependency  
RUN apt-get update && apt-get install -y \  
ruby \  
&& rm -rf /var/lib/apt/lists/*  
  
# Create app directory  
WORKDIR /vg  
  
ADD proto/graph-helper* /vg/proto/  
COPY \--from=build /usr/src/app/target/release/graph-genome-browser-backend
/vg/  
  
RUN mkdir /vg/tmp; \  
mkdir /vg/tmp/xg; \  
mkdir /vg/static; \  
wget -O - https://www.dropbox.com/s/56r7zadwcc1etmr/chm1.tar.gz?dl=0 | tar xzv
-C /vg/static; \  
wget -O -
ftp://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_human/release_27/gencode.v27.basic.annotation.gff3.gz
| gunzip -c | grep -v "#" > static/gencode.v27.basic.annotation.gff3; \  
wget -O -
ftp://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_human/release_27/GRCh37_mapping/gencode.v27lift37.basic.annotation.gff3.gz
| gunzip -c | grep -v "#" > static/gencode.v27lift37.basic.annotation.gff3;  
  
ADD sample/chm1/config.yaml /vg/static  
  
EXPOSE 8081  
ENV RUST_LOG info  
  
CMD ["./graph-genome-browser-backend", "--config=static/config.yaml", "--
interval=1500000", "--http=0.0.0.0:8081", "--api=/api/v2/"]  

