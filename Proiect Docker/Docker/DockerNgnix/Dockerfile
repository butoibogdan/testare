FROM nginx:latest

WORKDIR /usr/share/nginx/html

COPY index.html index.html

# Expunem portul 80 din container
EXPOSE 80

# Comanda implicită pentru a porni Nginx
CMD ["nginx", "-g", "daemon off;"]
