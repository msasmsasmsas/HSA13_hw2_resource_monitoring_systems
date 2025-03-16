docker-compose up --build
# docker-compose down && docker-compose up --build -d
# siege -c 100 -r 100 http://localhost/

#Чтобы установить curl внутри контейнера FastAPI, попробуйте выполнить:

#docker exec -it fastapi bash
#apt update && apt install -y curl
#curl -X GET http://elasticsearch:9200

#Если не хотите устанавливать дополнительные утилиты, используйте Python:

#docker exec -it fastapi python3 -c "import requests; print(requests.get('http://elasti


#4. Поиск IP-адреса Elasticsearch в Windows (PowerShell)

#Так как команда grep не работает в PowerShell, используйте следующую команду для поиска IP-адреса Elasticsearch:

#docker inspect elasticsearch | Select-String "IPAddress"

#Если IP-адрес найден, попробуйте подключиться к нему:

#curl -X GET http://<IPAddress>:9200

#переопределение пароля еластик
#docker exec -it elasticsearch /usr/share/elasticsearch/bin/elasticsearch-reset-password -u elastic -i