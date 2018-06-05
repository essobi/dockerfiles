FROM draffensperger/docker-builds:alacritty-build as alacritty-build  
FROM scratch  
COPY --from=alacritty-build /root/vendored-
crates/alacritty/target/release/alacritty /  

