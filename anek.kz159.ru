upstream anek {
   server 127.0.0.1:8080;
}
server {
        listen 80;
	server_name anek.kz159.ru;
	root /var/www/anek.kz159.ru;

#        location /static/  {
#            root /var/www/anek.kz159.ru/public/;
#        }

        location / {
            proxy_pass         http://anek;
            proxy_redirect     off;
            proxy_set_header   Host $host;
            proxy_set_header   X-Real-IP $remote_addr;
            proxy_set_header   X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header   X-Forwarded-Host $server_name;
        }
}
